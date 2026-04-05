from google import genai
import asyncio
import os
from mcp.client.stdio import stdio_client
from mcp.client.stdio import StdioServerParameters
from mcp.client.session import ClientSession


class PPTGenieAgent:
    """
    PPTGenieAgent represents the AI Agent (brain).

    Agent = LLM reasoning + MCP tool execution
    """

    def __init__(self):
        # --------------------------------------------------------
        # Gemini LLM Initialization
        # --------------------------------------------------------
        self.client = genai.Client(api_key="AIzaSyCsRd5bPndh6O3dPh-Y7jDXttCpqLACKL4")

    # ------------------------------------------------------------
    # MCP Tool Caller
    # ------------------------------------------------------------
    
    def call_tool(self, tool_name, args=None):
     """
     Calls MCP tool using proper session-based client.
     """

     if args is None:
        args = {}

     async def _call():
        server = StdioServerParameters(
            command="python",
            args=["-m", "mcp_server.server"]
        )

        async with stdio_client(server) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool_name, args)
                return result

     return asyncio.run(_call())
    # ------------------------------------------------------------
    # LLM Call
    # ------------------------------------------------------------
    def ask_llm(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    # ------------------------------------------------------------
    # Planning
    # ------------------------------------------------------------
    def plan_slides(self, user_input, slide_count=5):

        print("[Planning] Asking LLM to generate slide outline...")

        prompt = f"""
        Create a {slide_count}-slide presentation outline for:
        "{user_input}"

        Return ONLY a Python list of titles.
        """

        response = self.ask_llm(prompt)

        try:
            slide_titles = eval(response)
        except:
            slide_titles = [
                f"Introduction to {user_input}",
                f"Core Concepts of {user_input}",
                f"Applications of {user_input}",
                f"Challenges of {user_input}",
                "Conclusion"
            ]

        print(f"[Planning] Generated Slides: {slide_titles}")
        return slide_titles

    # ------------------------------------------------------------
    # Content Generation
    # ------------------------------------------------------------
    def generate_content(self, title):

        return [
            f"{title} involves key concepts",
            f"It explains important ideas clearly",
            f"It has real-world applications",
            f"It is widely used in practice"
        ]

    # ------------------------------------------------------------
    # Image Decision
    # ------------------------------------------------------------
    def should_add_image(self, title):

        keywords = ["concept", "application", "architecture"]

        return any(word in title.lower() for word in keywords)

    # ------------------------------------------------------------
    # MAIN EXECUTION LOOP
    # ------------------------------------------------------------
    def run(self, user_input):

     async def _run():

        server = StdioServerParameters(
            command="python",
            args=["-m", "mcp_server.server"]
        )

        async with stdio_client(server) as (read, write):
            async with ClientSession(read, write) as session:

                await session.initialize()

                print("[Agent] Creating new presentation...")
                await session.call_tool("create_presentation", {})

                slide_titles = self.plan_slides(user_input)

                print("\n[Agent] Starting execution...\n")

                for i, title in enumerate(slide_titles):

                    print(f"\n[Agent] Step {i+1}: {title}")

                    print("[Decision] Adding slide...")
                    await session.call_tool("add_slide", {"title": title})

                    print("[Decision] Generating content...")

                    # Generate content using LLM (agent side)
                    content_list = self.ask_llm(f"""
                        Generate 4 bullet points for a PPT slide on: {title}

                        Rules:
                        - Be specific
                        - No generic phrases
                        - Short and clear
                        """).split("\n")
                    content = "\n".join(content_list)
                    image_needed = self.should_add_image(title)

                    print("[Action] Writing content...")
                    await session.call_tool(
                      "write_content",
                        {
                          "bullet_points": content_list,
                          "has_image": image_needed
                        }
                    )

                    if image_needed:
                        print("[Decision] Adding image...")
                        img = await session.call_tool("generate_image", {"title": title})
                        await session.call_tool("add_image_to_slide", {"image_path": img})
                    else:
                        print("[Decision] Skipping image")

                print("\n[Agent] Saving presentation...")
                result = await session.call_tool("save_presentation", {})

         # --------------------------------------------------------
        # Extract actual file name from MCP response
        # --------------------------------------------------------
        file_text = result.content[0].text  # Extract message

        # Example: "Presentation saved as PPTGenie_20260405_215308.pptx"
        file_name = file_text.split(" as ")[-1]

        # Get absolute path
        file_path = os.path.abspath(file_name)

        print(f"[Agent] Presentation saved at: {file_path}")

        return file_path

     return asyncio.run(_run())
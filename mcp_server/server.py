from mcp.server.fastmcp import FastMCP
from mcp_server.ppt_tools import PPTTools

# ------------------------------------------------------------
# MCP Server Initialization
# ------------------------------------------------------------
# FastMCP creates a lightweight MCP-compliant server
# that exposes Python functions as tools
mcp = FastMCP("PPTGenie Server")

# ------------------------------------------------------------
# Tool Layer Initialization
# ------------------------------------------------------------
# PPTTools contains all PowerPoint-related operations
# This acts as the backend execution layer
ppt = PPTTools()


# ------------------------------------------------------------
# TOOL 1: Create Presentation
# ------------------------------------------------------------
@mcp.tool()
def create_presentation():
    """
    Initializes a new PowerPoint presentation.

    Purpose:
    - Starts a fresh PPT file
    - Must be called before adding slides

    Returns:
    - Confirmation message
    """
    ppt.create_presentation()
    return "Presentation created"


# ------------------------------------------------------------
# TOOL 2: Add Slide
# ------------------------------------------------------------
@mcp.tool()
def add_slide(title: str):
    """
    Adds a new slide with the given title.

    Parameters:
    - title (str): Title of the slide

    Returns:
    - Confirmation message
    """
    ppt.add_slide(title)
    return f"Slide added with title: {title}"


# ------------------------------------------------------------
# TOOL 3: Write Content
# ------------------------------------------------------------
@mcp.tool()
def write_content(title: str, content: str, has_image: bool = False):
    """
    Writes bullet points into the latest slide.
    """

    # Convert content (string) → bullet points (list)
    bullet_points = content.split("\n")

    # Get current slide (last added slide)
    slide = ppt.current_slide

    ppt.write_content(slide, bullet_points, has_image)

    return "Content written successfully"


# ------------------------------------------------------------
# TOOL 4: Generate Summary
# ------------------------------------------------------------
@mcp.tool()
def generate_summary(title: str, content: list):
    """
    Generates a short summary for a slide.

    Parameters:
    - title (str): Slide title
    - content (list): Bullet points

    Returns:
    - Summary text
    """
    return ppt.generate_summary(title, content)


# ------------------------------------------------------------
# TOOL 5: Add Summary to Footer
# ------------------------------------------------------------
@mcp.tool()
def add_summary_to_footer(summary: str):
    """
    Adds summary text to the slide footer.

    Parameters:
    - summary (str): Summary text

    Returns:
    - Confirmation message
    """
    ppt.add_summary_to_footer(summary)
    return "Summary added to footer"


# ------------------------------------------------------------
# TOOL 6: Generate Image
# ------------------------------------------------------------
@mcp.tool()
def generate_image(title: str):
    """
    Generates an image based on slide title.

    Parameters:
    - title (str): Slide topic

    Returns:
    - Image file path
    """
    return ppt.generate_image(title)


# ------------------------------------------------------------
# TOOL 7: Add Image to Slide
# ------------------------------------------------------------
@mcp.tool()
def add_image_to_slide(image_path: str):
    """
    Adds an image to the current slide.

    Parameters:
    - image_path (str): Path to generated image

    Returns:
    - Confirmation message
    """
    ppt.add_image_to_slide(image_path)
    return "Image added to slide"


# ------------------------------------------------------------
# TOOL 8: Save Presentation
# ------------------------------------------------------------
@mcp.tool()
def save_presentation():
    """
    Saves the PowerPoint presentation.

    Returns:
    - File path of saved PPT
    """
    return ppt.save_presentation()


# ------------------------------------------------------------
# MCP Server Entry Point
# ------------------------------------------------------------
# Starts the MCP server and exposes all registered tools
if __name__ == "__main__":
    mcp.run()
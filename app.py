import streamlit as st
from agent.agent_ppt import PPTGenieAgent
import os

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------
st.set_page_config(page_title="PPTGenie", page_icon="📊")

# ------------------------------------------------------------
# Title
# ------------------------------------------------------------
st.title("📊 PPTGenie AI")
st.subheader("Generate PowerPoint Presentations from a Single Prompt")

# ------------------------------------------------------------
# User Input
# ------------------------------------------------------------
user_input = st.text_input("Enter your topic:")

# ------------------------------------------------------------
# Generate Button
# ------------------------------------------------------------
if st.button("Generate PPT"):

    if user_input.strip() == "":
        st.warning("Please enter a topic")
    else:
        st.info("Generating your presentation... Please wait ⏳")

        # Initialize agent
        agent = PPTGenieAgent()

        # Run agent
        file_path = agent.run(user_input)

        st.success("Presentation generated successfully 🎉")

        # --------------------------------------------------------
        # Show file path
        # --------------------------------------------------------
        st.write("Saved at:")
        st.code(file_path)

        # --------------------------------------------------------
        # Download Button
        # --------------------------------------------------------
        with open(file_path, "rb") as f:
            st.download_button(
                label="Download PPT",
                data=f,
                file_name=os.path.basename(file_path),
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )

        # --------------------------------------------------------
        # Auto open (optional)
        # --------------------------------------------------------
        try:
            os.startfile(file_path)
        except:
            pass
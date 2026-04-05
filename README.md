# 🎯 PPTGenie – AI-Powered Presentation Generator

## 📌 Overview

PPTGenie is an AI-powered agent system that automatically generates PowerPoint presentations from user prompts. It leverages LLM capabilities along with tool-calling to create structured slides, add content, and format presentations dynamically.

---

## 🚀 Features

* 🧠 AI-generated slide content
* 📄 Automatic slide creation
* 📝 Bullet point generation for each slide
* 🖼️ (Planned) Image integration support
* ⚙️ Tool-based architecture using MCP
* 📊 Structured and scalable design

---

## 🏗️ System Architecture

User Prompt → LLM → Agent → Tool Calls → PowerPoint Generation

### Flow:

1. User provides a topic
2. LLM generates slide titles and content
3. Agent processes response
4. MCP tools:

   * Create slides
   * Insert content
   * (Future) Add images
5. Final PPT is generated

---

## 🛠️ Tech Stack

* Python
* MCP (Model Context Protocol)
* LLM (via API)
* python-pptx (PowerPoint generation)

---

## 📂 Project Structure

```
PPTGenie/
│
├── mcp_server/        # Tool implementations
├── agent/             # Agent logic
├── utils/             # Helper functions
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/PPTGenie.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the project:

```
python main.py
```

---

## ⚠️ Current Limitations

* Text not properly inserted into slides (placeholder issue)
* Layout handling needs improvement
* Image and text separation not fully implemented

---

## 🔮 Future Improvements

* Fix content placement in slides
* Add image + text layout separation
* Improve UI/UX of generated slides
* Add customization options (themes, fonts)
* Integrate multi-modal input (image + text)

---

## 👩‍💻 Author

Swetha Battula

---

## ⭐ Notes

This project demonstrates understanding of:

* Agent workflows
* Tool calling
* LLM integration
* Debugging real-world system issues

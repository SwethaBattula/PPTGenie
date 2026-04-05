# 🧪 PPTGenie – Debugging & Issue Resolution Report

## 🎯 Objective

To build an AI agent capable of generating structured PowerPoint presentations using LLM outputs and tool-based execution.

---

## ❌ Issue 1: Content Not Appearing in Slides

### 🔍 Problem

Generated slides showed:

* "Click to add text"
* No bullet points inserted

### 🧠 Root Cause

* Content was not being written to the correct placeholder
* Wrong or missing reference to slide object
* Text frame not properly accessed

### ✅ Solution

* Accessed correct placeholder:
  slide.placeholders[1]
* Used text_frame to insert content
* Cleared default placeholder text before adding bullets

---

## ❌ Issue 2: Incorrect Slide Layout

### 🔍 Problem

Slides did not contain content areas

### 🧠 Root Cause

* Wrong layout index used (e.g., title-only layout)

### ✅ Solution

* Used correct layout:
  prs.slide_layouts[1] (Title + Content)

---

## ❌ Issue 3: Tool Not Receiving Slide Object

### 🔍 Problem

Content function failed silently

### 🧠 Root Cause

* Slide object not passed correctly to tool

### ✅ Solution

* Ensured function signature:
  write_content(slide, bullet_points)

---

## ❌ Issue 4: Agent-Tool Integration Gap

### 🔍 Problem

LLM generated correct content but slides remained empty

### 🧠 Root Cause

* Tool execution pipeline failed to apply generated data

### ✅ Solution

* Debugged agent flow:
  LLM → Agent → Tool → PPT
* Ensured data passed correctly between components

---

## ❌ Issue 5: GitHub Repository Missing Code

### 🔍 Problem

Only README and requirements were pushed

### 🧠 Root Cause

* Files not added before commit
* Possible wrong working directory

### ✅ Solution

* Used:
  git add .
  git commit
  git push

---

## 📊 Key Learnings

* Importance of correct placeholder handling in python-pptx
* Agent systems require strict data flow validation
* Debugging tool-calling systems requires step-by-step tracing
* Small integration issues can break entire pipelines

---

## 🚀 Conclusion

The project successfully demonstrates:

* Agent-based architecture
* LLM + tool integration
* Real-world debugging skills
* Problem-solving approach

Further improvements will enhance robustness and usability.

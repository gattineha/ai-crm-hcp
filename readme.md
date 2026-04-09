# AI-First CRM HCP Module

## Overview
The **AI-First CRM HCP Module** is a full-stack application designed to manage and enhance interactions with Healthcare Professionals (HCPs).  

This system goes beyond traditional CRM functionality by integrating **AI-driven insights**, enabling intelligent summarization, better decision-making, and improved productivity for field representatives in the life sciences domain.

---

## Objective
To design and implement a **Log Interaction Screen** that allows users to:
- Capture HCP interaction data efficiently
- Edit and manage interaction records
- Generate AI-powered summaries
- Simulate an AI-first CRM workflow using agent-based architecture

---

## AI-First Approach
This project follows an **AI-first design philosophy**, where AI is deeply integrated into the workflow:

- Converts unstructured input into structured data
- Generates intelligent summaries
- Assists in decision-making and follow-ups
- Reduces manual effort for users

---

## Architecture
Frontend (React) → Backend (FastAPI) → Database (SQLite)
↓
AI Agent (LangGraph - Conceptual)
↓
LLM (Groq / LLaMA)


---

## Tech Stack

### Frontend
- React.js
- Axios
- Custom Styling (Inter Font)

### Backend
- FastAPI (Python)
- REST APIs

### Database
- SQLite (Lightweight relational database)

### AI & Agent Framework (Conceptual)
- LangGraph (Agent orchestration)
- Groq LLM (Gemma / LLaMA models)

---

## Key Features

### Log Interaction
- Capture meeting details (doctor, date, time, attendees, objective)
- Store structured data in database

### Edit Interaction
- Update existing interaction records
- Maintain accurate and up-to-date information

### Retrieve Interactions
- Fetch all stored meetings
- Display data dynamically in UI

### AI Summary
- Generate structured summaries of meetings
- Highlight key points and action items

---

## LangGraph Agent & Tools

The system is designed around a **LangGraph agent**, which manages workflows and invokes tools based on user input.

### Tools Implemented (Conceptual)

1. **Log Interaction Tool**
   - Captures structured and unstructured meeting data
   - Uses AI for entity extraction and formatting

2. **Edit Interaction Tool**
   - Modifies existing records
   - Ensures data accuracy

3. **Summarize Interaction Tool**
   - Generates concise summaries using LLMs
   - Extracts key insights

4. **Retrieve Interaction History Tool**
   - Fetches past interactions for better tracking

5. **Suggest Next Action Tool**
   - Recommends follow-ups based on previous interactions

---

## Workflow

1. User enters meeting details in the UI  
2. Frontend sends data via API to backend  
3. Backend stores data in SQLite database  
4. User can edit or retrieve interactions  
5. AI agent processes data to generate summaries  

---

## Real-World Use Case

This system is designed for **Life Sciences CRM workflows**, where:

- Field representatives interact with doctors (HCPs)
- Interaction tracking is critical
- AI helps summarize discussions and suggest next steps

---

## ▶How to Run the Project

### Backend
```bash
cd backend
uvicorn main:app --reload

### frontend
```bash
cd frontend
npm install
npm start


---
Author

Neha Gatti

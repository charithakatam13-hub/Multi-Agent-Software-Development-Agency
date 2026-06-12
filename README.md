# AI Software Agency

A Multi-Agent Software Development Agency built using LangGraph.

This project simulates how a real software company operates by assigning specialized AI agents to different stages of software planning and architecture design.

The system automatically analyzes requirements, identifies project types, generates architecture plans, designs backend systems, creates database structures, performs QA planning, reviews outputs, and produces a final project report.

---

## Architecture

```text
User Requirement
        │
        ▼
Requirement Analyzer
        │
        ▼
Project Classifier
        │
        ├──────────────┐
        │              │
        ▼              ▼
 AI Architect    Frontend Architect
        │              │
        └──────┬───────┘
               ▼
        Backend Agent
               ▼
        Database Agent
               ▼
           QA Agent
               ▼
        Reviewer Agent
               ▼
      Final Report Agent
```

---

## Agents

### Requirement Analyzer Agent

Responsibilities:

* Analyze user requirements
* Extract features
* Identify users
* Estimate project complexity

---

### Project Classifier Agent

Classifies projects into:

* AI Projects
* Web Projects
* Enterprise Projects

Uses rule-based routing inside LangGraph.

---

### AI Architect Agent

Creates architecture for:

* LLM Applications
* RAG Systems
* AI Assistants
* Machine Learning Platforms

Suggested Stack:

* LangChain
* OpenAI/Gemini
* Vector Databases

---

### Frontend Architect Agent

Designs web applications.

Suggested Stack:

* React
* Next.js
* Tailwind CSS

Generates:

* UI Modules
* Frontend Architecture
* Navigation Structure

---

### Enterprise Architect Agent

Designs enterprise-grade applications.

Suggested Stack:

* Spring Boot
* Microservices
* Kafka

Generates:

* Service Architecture
* Business Modules
* Integration Strategy

---

### Backend Agent

Creates:

* API Design
* Authentication Strategy
* Folder Structure
* Service Layer Design

---

### Database Agent

Creates:

* Database Schema
* Relationships
* Indexing Strategy
* Storage Design

---

### QA Agent

Generates:

* Test Cases
* Validation Rules
* Edge Cases
* QA Checklist

---

### Reviewer Agent

Reviews all outputs and determines:

* APPROVED
* NEEDS_REVISION

---

### Final Report Agent

Compiles:

* Project Type
* Architecture Plan
* Backend Design
* Database Design
* QA Plan
* Review Status

---

## Features

* Multi-Agent Architecture
* Conditional Routing
* LangGraph Workflows
* Software Requirement Analysis
* Architecture Generation
* Backend Design
* Database Design
* QA Planning
* Automated Review System

---

## Project Structure

```text
ai-software-agency/
│
├── main.py
├── state.py
├── requirements.txt
│
├── agents/
│   ├── requirement_analyzer.py
│   ├── project_classifier.py
│   ├── ai_architect.py
│   ├── frontend_architect.py
│   ├── enterprise_architect.py
│   ├── backend_agent.py
│   ├── database_agent.py
│   ├── qa_agent.py
│   ├── reviewer_agent.py
│   └── final_report_agent.py
│
└── workflow/
    └── graph.py
```

---

## Installation

```bash
pip install langgraph
pip install langchain
pip install langchain-core
```

or

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

Example Input:

```text
Build an AI-powered customer support chatbot using RAG and vector databases.
```

Example Output:

```text
PROJECT TYPE:
AI

ARCHITECTURE:
- LangChain
- Gemini
- Qdrant

BACKEND:
- FastAPI
- JWT Authentication

DATABASE:
- PostgreSQL
- Vector Store

QA:
- Functional Testing
- Edge Case Testing

REVIEW:
APPROVED
```

---

## Concepts Demonstrated

* Multi-Agent Systems
* LangGraph State Management
* Conditional Routing
* Agent Collaboration
* Workflow Orchestration
* Software Architecture Planning

---

## Future Improvements

* LLM-based Requirement Analysis
* Cost Estimation Agent
* DevOps Agent
* UI Wireframe Generator
* Architecture Diagram Generation
* Streamlit Frontend
* Deployment Planner

---

## Author

Charitha Katam

AI Engineering | LangGraph | Multi-Agent Systems

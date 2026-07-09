# ResearchOS AI

**Enterprise Multi-Agent AI Research Platform**

ResearchOS AI is a production-style multi-agent AI platform that automates technical research using specialized AI agents orchestrated through LangGraph. Instead of relying on a single chatbot, the system decomposes a research task into multiple stages including planning, web research, GitHub repository analysis, technical review, and professional report generation.

The project demonstrates modern AI engineering concepts such as agent orchestration, workflow management, tool integration, and report synthesis using a modular architecture.

---

## Features

* Multi-Agent workflow using LangGraph
* Planner Agent for task decomposition
* Web Search Agent powered by DDGS
* GitHub Repository Analysis Agent
* Reviewer Agent for technical synthesis
* Report Agent for structured research generation
* FastAPI backend
* Streamlit dashboard
* Professional report export in Markdown and PDF
* GitHub repository analysis
* Source reference panel
* Modular and scalable architecture

---

## Architecture

```
                    User
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
               FastAPI Backend
                      │
                      ▼
             LangGraph Workflow
                      │
      ┌──────────┬──────────┬──────────┬──────────┐
      ▼          ▼          ▼          ▼
   Planner     Search     GitHub    Reviewer
      │
      ▼
   Report Agent
      │
      ▼
 Final Technical Report
```

---

## Workflow

```
User Query
     │
     ▼
Planner Agent
     │
     ▼
Search Agent
     │
     ▼
GitHub Agent
     │
     ▼
Reviewer Agent
     │
     ▼
Report Agent
     │
     ▼
Final Report
```

---

## Project Structure

```
ResearchOS-AI/

├── app/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── graph/
│   ├── prompts/
│   ├── schemas/
│   ├── services/
│   ├── tools/
│   └── ui/
│
├── tests/
├── assets/
├── requirements.txt
└── README.md
```

---

## Technology Stack

### AI & Agent Frameworks

* LangGraph
* LangChain
* Google Gemini

### Backend

* FastAPI
* Pydantic

### Frontend

* Streamlit

### External Services

* GitHub REST API
* DDGS (DuckDuckGo Search)

### Other Libraries

* ReportLab
* Requests

---

## Agent Responsibilities

### Planner Agent

* Understands the research objective
* Breaks the task into smaller execution steps

### Search Agent

* Searches the web
* Collects relevant technical sources

### GitHub Agent

* Finds relevant repositories
* Extracts repository metadata
* Provides project insights

### Reviewer Agent

* Consolidates collected information
* Removes redundancy
* Produces structured research notes

### Report Agent

* Generates a professional research report
* Organizes findings into well-defined sections

---

## Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/ResearchOS-AI.git

cd ResearchOS-AI
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Linux

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Configure environment variables.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Running the Project

Start the backend.

```bash
export PYTHONPATH=$PWD

uvicorn app.main:app --reload
```

Start the frontend.

```bash
export PYTHONPATH=$PWD

streamlit run app/ui/streamlit_app.py
```

---

## Example Research Topics

* Compare LangGraph and CrewAI
* Introduction to Machine Learning
* Vision Transformers vs CNNs
* MLOps Best Practices
* Explainable AI
* Retrieval-Augmented Generation
* Reinforcement Learning
* Large Language Models

---

## Current Capabilities

* Research planning
* Technical web search
* GitHub repository discovery
* Repository analysis
* Technical review
* Structured report generation
* Markdown export
* PDF export

---



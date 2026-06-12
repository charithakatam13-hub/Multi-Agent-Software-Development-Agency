```python
from langgraph.graph import StateGraph, END

from state import SoftwareAgencyState

from agents.requirement_analyzer import requirement_analyzer
from agents.project_classifier import project_classifier

from agents.ai_architect import ai_architect
from agents.frontend_architect import frontend_architect
from agents.enterprise_architect import enterprise_architect

from agents.backend_agent import backend_agent
from agents.database_agent import database_agent
from agents.qa_agent import qa_agent

from agents.reviewer_agent import reviewer_agent
from agents.final_report_agent import final_report_agent


def route_project(state):

    project_type = state["project_type"]

    if project_type == "AI":
        return "ai_architect"

    elif project_type == "Web":
        return "frontend_architect"

    else:
        return "enterprise_architect"


def create_workflow():

    workflow = StateGraph(SoftwareAgencyState)

    # Core Agents
    workflow.add_node(
        "requirement_analyzer",
        requirement_analyzer
    )

    workflow.add_node(
        "project_classifier",
        project_classifier
    )

    # Architecture Agents
    workflow.add_node(
        "ai_architect",
        ai_architect
    )

    workflow.add_node(
        "frontend_architect",
        frontend_architect
    )

    workflow.add_node(
        "enterprise_architect",
        enterprise_architect
    )

    # Development Agents
    workflow.add_node(
        "backend_agent",
        backend_agent
    )

    workflow.add_node(
        "database_agent",
        database_agent
    )

    workflow.add_node(
        "qa_agent",
        qa_agent
    )

    # Review Agents
    workflow.add_node(
        "reviewer_agent",
        reviewer_agent
    )

    workflow.add_node(
        "final_report_agent",
        final_report_agent
    )

    # Entry Point
    workflow.set_entry_point(
        "requirement_analyzer"
    )

    # Flow
    workflow.add_edge(
        "requirement_analyzer",
        "project_classifier"
    )

    # Conditional Routing
    workflow.add_conditional_edges(
        "project_classifier",
        route_project,
        {
            "ai_architect": "ai_architect",
            "frontend_architect": "frontend_architect",
            "enterprise_architect": "enterprise_architect",
        }
    )

    # Architecture → Backend
    workflow.add_edge(
        "ai_architect",
        "backend_agent"
    )

    workflow.add_edge(
        "frontend_architect",
        "backend_agent"
    )

    workflow.add_edge(
        "enterprise_architect",
        "backend_agent"
    )

    # Development Pipeline
    workflow.add_edge(
        "backend_agent",
        "database_agent"
    )

    workflow.add_edge(
        "database_agent",
        "qa_agent"
    )

    workflow.add_edge(
        "qa_agent",
        "reviewer_agent"
    )

    workflow.add_edge(
        "reviewer_agent",
        "final_report_agent"
    )

    workflow.add_edge(
        "final_report_agent",
        END
    )

    return workflow.compile()
```

def final_report_agent(state):

    report = f"""
PROJECT TYPE:
{state['project_type']}

====================================

ARCHITECTURE:
{state['architecture_plan']}

====================================

BACKEND:
{state['backend_plan']}

====================================

DATABASE:
{state['database_plan']}

====================================

QA:
{state['qa_plan']}

====================================

REVIEW STATUS:
{state['review_report']}
"""

    return {
        "final_report": report
    }

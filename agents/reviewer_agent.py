def reviewer_agent(state):

    if (
        state.get("architecture_plan")
        and state.get("backend_plan")
        and state.get("database_plan")
        and state.get("qa_plan")
    ):
        result = "APPROVED"
    else:
        result = "NEEDS_REVISION"

    return {
        "review_report": result
    }

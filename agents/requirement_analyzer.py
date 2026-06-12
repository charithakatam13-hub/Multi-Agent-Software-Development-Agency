def requirement_analyzer(state):

    requirement = state["user_requirement"]

    analysis = f"""
Project Requirement:
{requirement}

Features:
- User Management
- Dashboard
- Reports

Users:
- Admin
- End Users

Complexity:
- Medium
"""

    return {
        "architecture_plan": analysis
    }

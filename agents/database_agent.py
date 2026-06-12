def database_agent(state):

    return {
        "database_plan": """
Database Design

Tables:
- Users
- Roles
- Orders

Relationships:
Users -> Orders

Indexes:
- email
- created_at

Database:
- PostgreSQL
"""
    }

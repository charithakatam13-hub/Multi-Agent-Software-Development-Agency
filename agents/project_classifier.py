def project_classifier(state):

    requirement = state["user_requirement"].lower()

    if any(word in requirement for word in
           ["ai", "machine learning", "llm", "rag"]):

        project_type = "AI"

    elif any(word in requirement for word in
             ["website", "portfolio", "ecommerce"]):

        project_type = "Web"

    elif any(word in requirement for word in
             ["erp", "hospital", "bank", "university"]):

        project_type = "Enterprise"

    else:
        project_type = "Web"

    return {
        "project_type": project_type
    }

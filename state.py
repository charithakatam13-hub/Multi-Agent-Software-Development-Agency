from typing import TypedDict


class SoftwareAgencyState(TypedDict):

    user_requirement: str

    project_type: str

    architecture_plan: str
    backend_plan: str
    database_plan: str
    qa_plan: str

    review_report: str
    final_report: str

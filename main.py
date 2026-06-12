```python
from workflow.graph import create_workflow


graph = create_workflow()

requirement = input(
    "Enter your software project requirement:\n"
)

initial_state = {
    "user_requirement": requirement,

    "project_type": "",

    "architecture_plan": "",
    "backend_plan": "",
    "database_plan": "",
    "qa_plan": "",

    "review_report": "",
    "final_report": ""
}

result = graph.invoke(initial_state)

print("\n" + "=" * 60)
print("AI SOFTWARE AGENCY REPORT")
print("=" * 60)

print(result["final_report"])
```

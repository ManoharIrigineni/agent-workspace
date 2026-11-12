def planner_node(state):
    task = state["task"]

    return {
        "plan": f"Plan generated for: {task}"
    }
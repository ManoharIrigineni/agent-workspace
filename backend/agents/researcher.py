def researcher_node(state):

    task = state["task"]

    return {
        "research": f"Research completed for: {task}"
    }
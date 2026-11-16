def writer_node(state):

    plan = state["plan"]
    research = state["research"]

    return {
        "final_output":
        f"""
Plan:
{plan}

Research:
{research}

Final document generated.
"""
    }
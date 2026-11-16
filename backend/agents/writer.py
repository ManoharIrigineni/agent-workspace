from services.llm_service import ask_llm


def writer_node(state):

    task = state["task"]
    plan = state["plan"]
    research = state["research"]

    final_document = ask_llm(
        f"""
        Create a final professional document.

        Task:
        {task}

        Plan:
        {plan}

        Research:
        {research}

        Produce a polished final output.
        """
    )

    return {
        "final_output": final_document
    }
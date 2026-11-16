from services.llm_service import ask_llm


def researcher_node(state):

    task = state["task"]
    plan = state["plan"]

    research = ask_llm(
        f"""
        You are a research agent.

        Task:
        {task}

        Plan:
        {plan}

        Provide supporting information,
        risks, recommendations,
        and useful resources.
        """
    )

    return {
        "research": research
    }
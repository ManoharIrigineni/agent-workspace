from services.llm_service import llm


def planner_node(state):

    task = state["task"]

    response = llm.invoke(
        f"""
        Create a detailed execution plan for:

        {task}

        Return only the plan.
        """
    )

    plan_text = response.content

    # Handle Gemini structured response
    if isinstance(plan_text, list):
        plan_text = plan_text[0]["text"]

    return {
        "plan": plan_text
    }
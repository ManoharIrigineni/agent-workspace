from typing import TypedDict


class AgentState(TypedDict):
    task: str
    plan: str
    research: str
    final_output: str
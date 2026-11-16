from fastapi import FastAPI
from langgraph.graph import StateGraph, START, END
from state.agent_state import AgentState
from agents.planner import planner_node
from agents.researcher import researcher_node
from agents.writer import writer_node
app = FastAPI()

graph_builder = StateGraph(AgentState)

graph_builder.add_node("planner", planner_node)
graph_builder.add_node("researcher", researcher_node)
graph_builder.add_node("writer", writer_node)

graph_builder.add_edge(START, "planner")
graph_builder.add_edge("planner", "researcher")
graph_builder.add_edge("researcher", "writer")
graph_builder.add_edge("writer", END)

graph = graph_builder.compile()

@app.get("/")
def health():
    return {"status": "running"}


@app.post("/run")
def run_agent(task: str):

    result = graph.invoke(
        {
            "task": task
        }
    )

    return result

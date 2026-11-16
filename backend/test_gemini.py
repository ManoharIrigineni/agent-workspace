from services.llm_service import llm

response = llm.invoke(
    "Create a 5 step plan to learn AWS."
)

print(response.content)
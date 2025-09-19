import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()

ENDPOINT = os.getenv("AI_FOUNDRY_ENDPOINT")

def delete_all_agents(project_client: AIProjectClient):
    print("Listing agents...")
    is_empty = True
    agents_list = project_client.agents.list()
    for agent in agents_list:
        is_empty = False
        print(f"Deleting agent: {agent.id} ({agent.name})")
        project_client.agents.delete(agent.id)
    if is_empty:
        print("No agents found.")

def delete_all_threads(project_client: AIProjectClient):
    print("Listing threads...")
    # Note: returns a pageable; you can pass limit/order/before/after for fine-grained pagination
    threads = project_client.agents.threads.list()
    is_empty = True
    for th in threads:
        is_empty = False
        name = getattr(th, "name", None) or ""
        print(f"Deleting thread: {th.id} {f'({name})' if name else ''}")
        project_client.agents.threads.delete(th.id)
    if is_empty:
        print("No threads found.")

def main():
    credential = DefaultAzureCredential()
    project_client = AIProjectClient(endpoint=ENDPOINT, credential=credential)

    delete_all_agents(project_client)
    delete_all_threads(project_client)
    print("Process finished.")

if __name__ == "__main__":
    main()

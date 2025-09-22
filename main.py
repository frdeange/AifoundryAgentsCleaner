import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()

ENDPOINT = os.getenv("AI_FOUNDRY_ENDPOINT")

def delete_all_agents(project_client: AIProjectClient):
    print("Listing agents...")
    agents_list = list(project_client.agents.list_agents())  # Convert to static list
    
    if not agents_list:
        print("No agents found.")
        return
    
    print(f"Found {len(agents_list)} agent(s) to delete.")
    for agent in agents_list:
        try:
            print(f"Deleting agent: {agent.id} ({agent.name})")
            project_client.agents.delete_agent(agent.id)
        except Exception as e:
            print(f"Warning: Could not delete agent {agent.id}: {e}")

def delete_all_threads(project_client: AIProjectClient):
    print("Listing threads...")
    # Note: returns a pageable; convert to static list to avoid pagination issues
    threads = list(project_client.agents.threads.list())  # Convert to static list
    
    if not threads:
        print("No threads found.")
        return
    
    print(f"Found {len(threads)} thread(s) to delete.")
    for th in threads:
        try:
            name = getattr(th, "name", None) or ""
            print(f"Deleting thread: {th.id} {f'({name})' if name else ''}")
            project_client.agents.threads.delete(th.id)
        except Exception as e:
            print(f"Warning: Could not delete thread {th.id}: {e}")

def main():
    credential = DefaultAzureCredential()
    project_client = AIProjectClient(endpoint=ENDPOINT, credential=credential)

    delete_all_agents(project_client)
    delete_all_threads(project_client)
    print("Process finished.")

if __name__ == "__main__":
    main()

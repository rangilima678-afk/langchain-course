
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

from langsmith import Client

client = Client()
client.delete_project(project_name="agents-under-the-hood")
print("Project deleted successfully!")
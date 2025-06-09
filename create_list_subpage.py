import sys
from dotenv import load_dotenv
from shared.notion_client_wrapper import NotionClientWrapper
from shared.list_reworker import filter_checked_todos
from datetime import datetime

# Load environment variables from .env
load_dotenv()

from shared.notion_automations import create_sublist

if __name__ == "__main__":
    print("Running Notion automation script locally...")
    automation_result = create_sublist()
    print(f"Local automation finished with result: {automation_result}")
    if automation_result.get("status") == "error":
        sys.exit(1) # Indicate failure for local script
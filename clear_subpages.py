import sys
from dotenv import load_dotenv
from shared.notion_client_wrapper import NotionClientWrapper

load_dotenv()

from shared.notion_automations import clear_notion_subpages

if __name__ == "__main__":
    print("Running Notion automation script locally...")
    automation_result = clear_notion_subpages()
    print(f"Local automation finished with result: {automation_result}")
    if automation_result.get("status") == "error":
        sys.exit(1) # Indicate failure for local script

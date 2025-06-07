import os
from dotenv import load_dotenv
from notion_client_wrapper import NotionClientWrapper

# Load environment variables from .env
load_dotenv()

# Get Notion token and page ID from .env
notion_token = os.getenv("NOTION_TOKEN")
notion_page_id = os.getenv("NOTION_PAGE_ID")

# Initialize the wrapper
notion_wrapper = NotionClientWrapper(auth_token=notion_token)

# Clear subpages from the specified page
notion_wrapper.clear_blocks_by_type(page_id=notion_page_id, block_type="child_page")

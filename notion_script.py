import os
from dotenv import load_dotenv
from notion_client_wrapper import NotionClientWrapper
from list_reworker import filter_checked_todos
from datetime import datetime

# Load environment variables from .env
load_dotenv()

# Get Notion token and page ID from .env
notion_token = os.getenv("NOTION_TOKEN")
notion_page_id = os.getenv("NOTION_PAGE_ID")

# Initialize the wrapper
notion_wrapper = NotionClientWrapper(auth_token=notion_token)

# Fetch blocks from the page
blocks = notion_wrapper.get_blocks(page_id=notion_page_id)

# Filter the blocks to include only checked to_do blocks and other block types
filtered_blocks = filter_checked_todos(blocks, excluded_types={"child_page"})

# Create a new page with the filtered blocks
parent_page_id = notion_page_id  # You can specify a different parent page ID if needed
new_page_title = f"Filtered Tasks - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

new_page = notion_wrapper.create_page(
    parent_id=parent_page_id,
    title=new_page_title,
    children=filtered_blocks
)

print(f"New page created: {new_page.get('url')}")
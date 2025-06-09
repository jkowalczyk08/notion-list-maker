import os
import logging
from datetime import datetime

from shared.notion_client_wrapper import NotionClientWrapper
from shared.list_reworker import filter_checked_todos

def create_sublist():
    notion_token = os.getenv("NOTION_TOKEN")
    notion_page_id = os.getenv("NOTION_PAGE_ID")

    if not notion_token:
        raise ValueError("NOTION_TOKEN is required.")
    if not notion_page_id:
        raise ValueError("NOTION_PAGE_ID is required.")

    notion_wrapper = NotionClientWrapper(auth_token=notion_token)

    try:
        blocks = notion_wrapper.get_blocks(page_id=notion_page_id)

        filtered_blocks = filter_checked_todos(blocks, excluded_types={"child_page"})

        if not filtered_blocks:
            return {"status": "success", "message": "No new page created, no relevant tasks found."}

        parent_page_id = notion_page_id
        new_page_title = f"Filtered Tasks - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        new_page = notion_wrapper.create_page(
            parent_id=parent_page_id,
            title=new_page_title,
            children=filtered_blocks
        )
        page_url = new_page.get('url', 'N/A')
        return {"status": "success", "message": f"New page created: {page_url}"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def clear_notion_subpages():
    notion_token = os.getenv("NOTION_TOKEN")
    notion_page_id = os.getenv("NOTION_PAGE_ID")

    if not notion_token:
        raise ValueError("NOTION_TOKEN is required.")
    if not notion_page_id:
        raise ValueError("NOTION_PAGE_ID is required.")

    notion_wrapper = NotionClientWrapper(auth_token=notion_token)

    try:
        notion_wrapper.clear_blocks_by_type(page_id=notion_page_id, block_type="child_page")
        return {"status": "success", "message": "Successfully cleared child pages."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
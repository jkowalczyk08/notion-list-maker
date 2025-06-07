from typing import List, Dict, Any
from notion_client import Client
from concurrent.futures import ThreadPoolExecutor

class NotionClientWrapper:
    def __init__(self, auth_token: str):
        """
        Initialize the Notion client wrapper with authentication token.
        
        :param auth_token: The authentication token for the Notion API.
        """
        self.client = Client(auth=auth_token)

    def get_blocks(self, page_id: str) -> List[Dict[str, Any]]:
        blocks = []
        response = self.client.blocks.children.list(block_id=page_id)
        blocks.extend(response.get("results", []))
        
        while response.get("has_more"):
            response = self.client.blocks.children.list(block_id=page_id, start_cursor=response["next_cursor"])
            blocks.extend(response.get("results", []))
        
        return blocks
    
    def create_page(self, parent_id: str, title: str, children: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create a new Notion page under the specified parent with the given title and children.

        :param parent_id: The ID of the parent page or workspace.
        :param title: The title of the new page.
        :param children: The blocks to include as children of the new page.
        :return: The response from the Notion API.
        """
        page_data = {
            "parent": {"page_id": parent_id},
            "properties": {
                "title": [{"type": "text", "text": {"content": title}}]
            },
            "children": children
        }
        return self.client.pages.create(**page_data)

    def clear_blocks_by_type(self, page_id: str, block_type: str):
        """
        Deletes all blocks of a specific type from the specified Notion page.

        :param page_id: The ID of the Notion page.
        :param block_type: The type of blocks to delete (e.g., "child_page").
        """
        blocks = self.get_blocks(page_id=page_id)
        for block in blocks:
            if block.get("type") == block_type:
                block_id = block.get("id")
                self.client.blocks.delete(block_id=block_id)
                print(f"Deleted {block_type} block with ID: {block_id}")
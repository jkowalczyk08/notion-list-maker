from typing import List, Dict, Any, Set

def filter_checked_todos(blocks: List[Dict[str, Any]], excluded_types: Set[str] = None) -> List[Dict[str, Any]]:
    """
    Filters and reworks a list of blocks. Blocks of specified types are excluded,
    and for to_do blocks, only checked ones are included unless excluded.

    :param blocks: List of blocks retrieved from a Notion page.
    :param excluded_types: Set of block types to exclude from the filtered result.
    :return: A new list of blocks with the filtered content.
    """
    if excluded_types is None:
        excluded_types = set()

    filtered_blocks = []

    for block in blocks:
        block_type = block.get("type")

        if block_type == "to_do":
            # Check if the to_do block is marked as checked
            is_checked = block.get("to_do", {}).get("checked", False)
            if is_checked and "to_do" not in excluded_types:
                # Make the to_do block unchecked
                block["to_do"]["checked"] = False
                filtered_blocks.append(block)
        elif block_type not in excluded_types:
            # Include blocks not in excluded types
            filtered_blocks.append(block)

    return filtered_blocks
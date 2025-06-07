# Notion List Maker

## What is this?
A Python script for lazy people that don't want to create the same lists over and over again. It helps you create repetitive lists from a reusable template.

## Use cases:
* Groceries list - keep a single list template with all items you might want to buy. Select all you need for this week, run the script, and create a separate list just for this groceries run.
* Trip packing list - select only things you will need on this trip, run the script, and get only what you have to pack this time

## What can it do?
- Fetch all blocks from a Notion page.
- Filter out completed tasks (to_do blocks) and keep everything else.
- Create a new Notion page with the filtered content.
- Let you exclude certain block types if you want (e.g., dividers, headers).

## How to set it up

### What you need:
- Python 3.8 or higher
- pip to install dependencies

### Steps:
1. Clone this repo
2. Install the required Python libraries:
```sh
pip install -r requirements.txt
```
3. Setup notion integration with access to the page with your note template https://developers.notion.com/docs/authorization
4. Create a .env file in the project folder and add your Notion API token and page ID:
```
NOTION_TOKEN=your_notion_api_token
NOTION_PAGE_ID=your_page_id
```

## How to use it
Run the script:
```sh
python notion_script.py
```
The script will:
* Fetch blocks from your Notion page.
* Filter out checked tasks and keep everything else that is not a subpage.
* Create a new subpage with the filtered blocks. All tasks will be unchecked.

To clear all created subpages run:
```sh
python clear_subpages.py
```
import azure.functions as func
import json

from shared.notion_automations import create_sublist, clear_notion_subpages

app = func.FunctionApp()

@app.route(route="create_list_subpage")
def create_list_subpage(req: func.HttpRequest) -> func.HttpResponse:
    try:
        result = create_sublist()
        
        status_code = 200 if result.get("status") == "success" else 500
        return func.HttpResponse(
            json.dumps(result),
            mimetype="application/json",
            status_code=status_code
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"status": "error", "message": f"Internal server error: {str(e)}"}),
            mimetype="application/json",
            status_code=500
        )



@app.route(route="clear_subpages", auth_level=func.AuthLevel.FUNCTION)
def clear_subpages(req: func.HttpRequest) -> func.HttpResponse:
    try:
        result = clear_notion_subpages()
        
        status_code = 200 if result.get("status") == "success" else 500
        return func.HttpResponse(
            json.dumps(result),
            mimetype="application/json",
            status_code=status_code
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"status": "error", "message": f"Internal server error: {str(e)}"}),
            mimetype="application/json",
            status_code=500
        )
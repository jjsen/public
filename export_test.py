import requests
import json

# Configuration
JIRA_URL = "https://your-jira-instance.atlassian.net"
ISSUE_KEY = "ISSUE-123"  
JIRA_API_ENDPOINT = f"/rest/api/2/issue/{ISSUE_KEY}"
AUTH = ('your_email@example.com', 'your_api_token')  
OUTPUT_FORMAT = 'json'  # Change to 'csv' if you prefer CSV

# Function to fetch a specific issue from JIRA
def fetch_issue():
    url = f"{JIRA_URL}{JIRA_API_ENDPOINT}"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, auth=AUTH)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.text)
        return None

# Function to export issue data to JSON
def export_to_json(data):
    with open('issue_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Main script execution
if __name__ == "__main__":
    issue_data = fetch_issue()
    if issue_data:
        export_to_json(issue_data)
        print("Issue data exported to issue_data.json")
    else:
        print("No data to export.")

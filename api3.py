import requests
from getpass import getpass

# Configuration
jira_url = "https://your-domain.atlassian.net"  # Your JIRA domain
test_issue_key = "XRAY-123"  # Specific test issue key
api_token = getpass("Enter your JIRA API token: ")
email = input("Enter your JIRA email: ")

# API Headers
auth = requests.auth.HTTPBasicAuth(email, api_token)
headers = {
    "Accept": "application/json"
}

def fetch_xray_test_data(test_key):
    """Fetch all Xray test data for a specific test issue key."""
    page = 0
    all_data = []

    while True:
        # Update the endpoint URL with pagination & test issue key
        url = f"{jira_url}/rest/raven/1.0/api/test/{test_key}/testruns?page={page}"
        response = requests.get(url, headers=headers, auth=auth)
        
        if response.status_code == 200:
            data = response.json()
            all_data.extend(data)
            page += 1
            # Check if there is more data to fetch
            if "isLast" in data and data["isLast"]:
                break
        else:
            print("Failed to fetch data:", response.status_code, response.text)
            break

    return all_data

# Main execution
if __name__ == "__main__":
    test_data = fetch_xray_test_data(test_issue_key)
    if test_data:
        print("Fetched data:", test_data)
    else:
        print("No data to display.")


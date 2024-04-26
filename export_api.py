import requests
import csv
from getpass import getpass

# Configuration
jira_url = "https://your-domain.atlassian.net"  # Change to your JIRA domain
email = input("Enter your JIRA email: ")
api_token = getpass("Enter your JIRA API token: ")
test_key = "TEST-123"  # Replace with your actual test key

# API Headers
auth = requests.auth.HTTPBasicAuth(email, api_token)
headers = {
    "Accept": "application/json"
}

# XRAY API Endpoint to get test runs for a specific test
url = f"{jira_url}/rest/raven/1.0/api/test/{test_key}/testruns"

def export_test_runs_to_csv():
    response = requests.get(url, headers=headers, auth=auth)
    if response.status_code == 200:
        test_runs = response.json()
        # Define the filename
        csv_file = f"{test_key}_test_runs.csv"
        # Define CSV fields from the JSON structure you expect
        fields = ['id', 'status', 'executedBy', 'assignedTo', 'executionTime', 'defects', 'comments']  # Adjust these fields based on your actual data structure
        
        # Write to CSV
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for test_run in test_runs:
                writer.writerow({field: test_run.get(field, '') for field in fields})
        
        print("Test runs exported successfully to CSV.")
    else:
        print("Failed to fetch data:", response.status_code, response.text)

# Execute the function
export_test_runs_to_csv()

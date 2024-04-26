import requests
import csv
from getpass import getpass

# API Credentials and Endpoint
api_url = "https://yourserver/rest/raven/1.0/testruns"
username = input("Enter your JIRA username: ")
password = getpass("Enter your JIRA password: ")
auth = (username, password)

# Specify the parameters for the API request
params = {
    'testExecKey': 'DEMO-67',  # Example, replace with actual test execution key
    # Uncomment and use the appropriate parameter
    # 'testPlanKey': 'TESTPLAN-87',
    # 'savedFilterId': '1376',
    'includeTestFields': 'summary,customfield_1000',  # Optional
    'limit': 100,  # Optional
    'page': 1  # Optional
}

# Make the API request
response = requests.get(api_url, auth=auth, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Define the CSV file name
    filename = 'test_execution_results.csv'
    
    # Open the CSV file and write the data
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header based on your needs
        writer.writerow(['Test Key', 'Status', 'Type', 'Start', 'Finish', 'Executed By', 'Defects'])

        # Write data rows
        for item in data:
            writer.writerow([
                item.get('testKey'),
                item.get('status'),
                item.get('type'),
                item.get('start'),
                item.get('finish'),
                item.get('executedBy'),
                ", ".join(item.get('defects', []))  # Assuming 'defects' is a list of URLs or identifiers
            ])
    print("Data exported successfully to", filename)
else:
    print("Failed to fetch data:", response.status_code, response.text)

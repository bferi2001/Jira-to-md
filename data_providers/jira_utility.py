from requests.auth import HTTPBasicAuth
import requests, json
import decorators
import requests, json

class JiraUtility:
    
    def __init__(self, user, jira_pat) -> None:
        self.url = 'https://barnafeco.atlassian.net/rest/api/2/search?jql='
        self.auth = HTTPBasicAuth(user, jira_pat)
        
    
        
    @decorators.return_json_to_file 
    def get_jira_ticket(self) -> str:
        x = 0
        total_tickets = None
        all_tickets_details=list()
        while(not total_tickets or (x*50<total_tickets)):
            response = requests.get(
                    f"{self.url}", 
                    headers={"Accept": "application/json"},
                    auth=self.auth
                    ).json()
            total_tickets=response["total"]
            for ticket in list(response["issues"]):
                all_tickets_details.append(ticket)
            x+=1
        return all_tickets_details

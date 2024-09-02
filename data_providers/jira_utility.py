from requests.auth import HTTPBasicAuth
import requests, json
import decorators

class JiraUtility:
    
    def __init__(self, user, jira_pat) -> None:
        self.url = 'https://barnafeco.atlassian.net/rest/api/2/search?jql='
        self.auth = HTTPBasicAuth(user, jira_pat)
        self.getJiraTickets()
        
    
        
    @decorators.return_json_to_file 
    def getJiraTickets(self) -> None:
        x = 0
        total_tickets = None
        while(not total_tickets or (x*50<total_tickets)):
            response = json.loads(
            requests.get(
                    f"{self.url}", 
                    headers={"Accept": "application/json"},
                    auth=self.auth
                    ).text
            )
            total_tickets=response["total"]
            x+=1
        return response
            
        
    
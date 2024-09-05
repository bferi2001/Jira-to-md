from requests.auth import HTTPBasicAuth
import requests, json
import decorators
import requests, json

class JiraUtility:
    
    def __init__(self, user, jira_pat) -> None:
        self.url = 'https://barnafeco.atlassian.net/rest/api/2/search?jql='
        self.auth = HTTPBasicAuth(user, jira_pat)
        
        
    def get_tickets(self, filter:str) -> list:
        x = 0
        total_tickets = None
        all_tickets_details=list()
        while(not total_tickets or (x*50<total_tickets)):
            response = requests.get(
                    f"{self.url}{filter}", 
                    headers={"Accept": "application/json"},
                    auth=self.auth
                    ).json()
            total_tickets=response["total"]
            for ticket in list(response["issues"]):
                all_tickets_details.append(ticket)
            x+=1
        return all_tickets_details
    
    def get_story_tickets(self) -> list:
        return self.get_tickets("type=Story")
    
    @decorators.return_json_to_file
    def get_stories_to_path(self, path:str)->list:
        tickets=self.get_story_tickets()
        tickets_with_good_path=list()
        for ticket in tickets:
            if ticket["fields"]["customfield_10143"]:
                if any(e.startswith(path) for e in ticket["fields"]["customfield_10143"]):
                    tickets_with_good_path.append(ticket)
        return tickets_with_good_path
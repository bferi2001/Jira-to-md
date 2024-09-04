from requests.auth import HTTPBasicAuth
import requests, json

class JiraUtility:
    
    def __init__(self, user, jira_pat) -> None:
        self.url = 'https://barnafeco.atlassian.net/rest/api/2/search?jql='
        self.filter=''
        self.auth = HTTPBasicAuth(user, jira_pat)
        with open("asda.json", "w", encoding="utf-8") as file:
            response = requests.get(
                    f"{self.url}{self.filter}", 
                    headers={"Accept": "application/json"},
                    auth=self.auth
                    ).json()
            json.dump(response, file)
    
    def get_jira_ticket(self):
        response = requests.get(
                f"{self.url}{self.filter}", 
                headers={"Accept": "application/json"},
                auth=self.auth
                ).json()
        return response["issues"]

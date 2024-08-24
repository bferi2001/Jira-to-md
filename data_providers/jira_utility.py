from requests.auth import HTTPBasicAuth
import requests

class JiraUtility:
    
    def __init__(self, user, jira_pat) -> None:
        self.url = 'https://barnafeco.atlassian.net/rest/api/2/search?jql='
        self.filter=''
        auth = HTTPBasicAuth(user, jira_pat)
        print(f"{self.url}{self.filter}")
        with open("asda.json", "w", encoding="utf-8") as file:
            response = requests.get(
                    f"{self.url}{self.filter}", 
                    headers={"Accept": "application/json"},
                    auth=auth
                    ).text
            file.write(str(response))

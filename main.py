from data_providers.jira_utility import JiraUtility as JU
import converters.ticket_to_md as ttmd
def read_creds():
    creds=dict()
    with open("creds.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line=line.strip()
            creds[line.split("=")[0]]=line.split("=", 1)[1]
    return creds

creds = read_creds()
jira=JU(creds["user"], creds["jira_pat"])
ttmd.tickets_details_to_table(jira.get_stories_to_path("main.py"))
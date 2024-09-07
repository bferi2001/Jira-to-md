from data_providers.jira_utility import JiraUtility as JU
import converters.ticket_to_md as ttmd
import os, decorators

@decorators.print_return
def get_all_path():
    paths=list()
    not_walked_dirs=list()
    not_walked_dirs.append(os.getcwd())
    x=1
    while not_walked_dirs:
        actual_dir=not_walked_dirs.pop(0)
        paths.append(actual_dir)
        [paths.append(os.path.join(actual_dir, f)) for f in os.listdir(actual_dir) if os.path.isfile(os.path.join(actual_dir, f))]
        [not_walked_dirs.append(os.path.join(actual_dir, f)) for f in os.listdir(actual_dir) if (os.path.isdir(os.path.join(actual_dir, f)) and os.path.split(f)[1] not in [".git", "__pycache__"])]
    return paths
        


def read_creds():
    creds=dict()
    with open("creds.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line=line.strip()
            creds[line.split("=")[0]]=line.split("=", 1)[1]
    return creds

get_all_path()

#creds = read_creds()
#jira=JU(creds["user"], creds["jira_pat"])
#ttmd.tickets_details_to_table(jira.get_stories_to_path("main.py"))
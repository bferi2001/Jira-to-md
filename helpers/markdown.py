import converters.ticket_to_md as ttmd
from data_providers.jira_utility import JiraUtility as JU
import os

def create_markdown(path:str=".", content:str="") -> None:
    filepath=os.path.join(os.getcwd(), "_generated", "tickets", os.path.relpath(path, os.getcwd()))
    os.makedirs(filepath)
    with open(os.path.join(filepath, "tickets.md"), "w") as file:
        file.write(content)

def table_from_matrix(matrix) -> None:
    md_str=""
    for line in matrix:
        md_str+="| "
        for element in line:
            md_str+=f"{element} | "
        md_str+="\n"
    return md_str


def create_ticketlist_markdown_to_path(path:str, jira:JU)->None:
    relpath=os.path.relpath(path, os.getcwd())
    tickets_details=jira.get_stories_to_path(relpath)
    tickets_matrix=ttmd.tickets_details_to_matrix(tickets_details)    
    table=table_from_matrix(tickets_matrix)
    create_markdown(path=path, content=table)

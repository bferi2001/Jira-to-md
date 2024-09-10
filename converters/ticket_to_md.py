def tickets_details_to_matrix(tickets_details)->None:
    matrix = [["ID", "Summary", "Type", "Status", "Created", "Updated", "Reporter", "Assignee", "Paths"],
              ["-", "-", "-", "-", "-", "-", "-", "-", "-"]]
    for ticket in tickets_details:
        matrix.append(_ticket_details_to_array(ticket))
    return matrix


def _ticket_details_to_array(ticket_details:dict)->list:
    id=ticket_details["key"]
    summary=ticket_details["fields"]["summary"]
    type=ticket_details["fields"]["issuetype"]["name"]
    status=ticket_details["fields"]["status"]["name"]
    created=ticket_details["fields"]["created"]
    updated=ticket_details["fields"]["updated"]
    reporter=ticket_details["fields"]["reporter"]["self"]
    assignee="Unassigned"
    if ticket_details["fields"]["assignee"]:
        assignee=ticket_details["fields"]["assignee"]["self"]
    if ticket_details["fields"]["customfield_10143"]:
        path=""
        for e in ticket_details["fields"]["customfield_10143"]:
            path+=f"{e} <br />"
        
    return [id, summary, type, status, created, updated, reporter, assignee, path]
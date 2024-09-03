import helpers.markdown as md

def tickets_details_to_table(tickets_details)->None:
    matrix = [["ID", "Summary", "Type", "Status", "Created", "Updated", "Reporter", "Assignee"],
              ["-", "-", "-", "-", "-", "-", "-", "-"]]
    for ticket in tickets_details:
        matrix.append(_ticket_details_to_array(ticket))
    table=md.table_from_matrix(matrix)
    md.create_markdown(content=table)


def _ticket_details_to_array(ticket_details:dict())->list:
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
    return [id, summary, type, status, created, updated, reporter, assignee]
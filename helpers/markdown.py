def create_markdown(path:str=".", content:str="") -> None:
    with open(f"{path}/tickets.md", "w") as file:
        file.write(content)

def table_from_matrix(matrix) -> None:
    md_str=""
    for line in matrix:
        md_str+="| "
        for element in line:
            md_str+=f"{element} | "
        md_str+="\n"
    return md_str
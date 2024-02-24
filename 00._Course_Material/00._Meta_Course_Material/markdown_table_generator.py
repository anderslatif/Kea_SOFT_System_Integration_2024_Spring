import os
from pathlib import Path

table_data = [
    {
        "Title": "Introduction",
        "Date": "Feb. 1st", 
        "Description": """
            - Intro: This course

            - File types and data formats.

            - Everything but REST
        """,
        "Learning Goals": """
            - Alternatives to REST API.

            - Data formats. TXT, JSON, YAML, CSV, XML

            - Can parse files in these formats after the homework.
        """,
        "Resources and Activities": [
            "[Do this: [Individual] Azure for Students](00._Course_Material/01._Assignments/01._Introduction_Data_Formats/00._[Individual]_Azure_For_Students.md)",          
            "[Do this: [Individual] Install Node.js](00._Course_Material/01._Assignments/01._Introduction_Data_Formats/00._[Individual]_Install_Node.js.md)",          
            "[01a [Individual] Data Parsing](00._Course_Material/01._Assignments/01._Introduction_Data_Formats/01a._[Individual]_Data_Parsing.md)",
        ]
    },
    {
        "Title": "Data",
        "Date": "Feb. 8th", 
        "Description": """
            - Intro: The exam

            - Data encoding 

            - Hashing, serializing, marshalling

            - Python modules

            - Environment Setup

            - Packages eco system in Node and Python

            - Servers
        """,
        "Learning Goals": """

            - Can argue about different build tools for Python and understands their pros and cons. 

            - Can use poetry. 

            - Understands encoding, serializing and marshalling. Knows about charsets and encoding types.
        """,
        "Resources and Activities": [
            "[00 [Individual] Data format translation servers - Part II](00._Course_Material/01._Assignments/02._Data/00._[Individual]_Data_parsing_server_-_Part_I.md)",
            "[[Optional] Serialize / Marshall data](00._Course_Material/01._Assignments/02._Data/00._[Optional]_Serialize__Marshall_data.md)",          
        ]
    },
    {
        "Title": "Server to server / Real-time communication - Part I",
        "Date": "Feb. 15th", 
        "Description": """
            - Communication

            - Protocols (TCP / UDP)

            - Making a server act as a client to another server.

            - Environment Variables (OS level, Runtime environment level)
        """,
        "Learning Goals": """

            - Knows about different communication protocols on a superficial level.

            - Knows how to make a HTTP requests between languages. 

            - Understand the different levels of environment variables and how they differ. 

            - Knows how to define environment variables in different languages.
        """,
        "Resources and Activities": [
            "[03a [Individual]_Data parsing server - Part II](00._Course_Material/01._Assignments/03._Server_to_server_Real-time_communication_-_Part_I/03a._[Individual]_Data_parsing_server_-_Part_II.md)",          
        ]
    },
    {
        "Title": "Real-time communication - Part II",
        "Date": "Feb. 22th", 
        "Description": """
            - ngrok 

            - Date

            - Client polling, short polling, long polling.

            - Server-sent events

            - Webhooks
        """,
        "Learning Goals": """
            - Can use ngrok

            - Understand how date affects systems and communication between services.

            - Understands challenges and edge cases when working with date and why this is important during integration.

            - Understands client polling, short polling, long polling and the pros and cons of each approach.

            - Understands SSE and can explain how to implement it. Has an example ready. 
        """,
        "Resources and Activities": [
            "[04a [Individual] SSE example](00._Course_Material/01._Assignments/04._Real-time_communication_-_Part_II/04a._[Individual]_SSE_example.md)", 
            "[04b [Pair] Database granular access](00._Course_Material/01._Assignments/04._Real-time_communication_-_Part_II/04b._[Pair]_Database_granular_access.md)",          
        ]
    },
    {
        "Title": "No Lecture",
        "Date": "February 29th", 
        "Description": """
            Work on the homework. 
        """,
        "Learning Goals": """
        """,
        "Resources and Activities": [
        ]
    },
    {
        "Title": "Real-time communication - Part III / Documentation",
        "Date": "March 7th", 
        "Description": """
            - Websockets

            - Webhooks 

            - Backing up MySQL

            - Documenting MySQL 

            - OpenAPI

            - Swagger + Express/FastAPI/Spring

            - Architecture Diagrams
        """,
        "Learning Goals": """
            - Understands the pros and cons of SSE and can compare it to Websockets. 

            - Can recall how we did Github Wehooks without having to be able to do it on the fly. Can illustrate exactly how it works by drawing a diagram.

            - Understands how to approach building a custom webhook system.
            
            - Can document and backup MySQL

            - Has considered how to document the databases they are familiar with.

            - Understands the what and why of OpenAPI

            - Can generate OpenAPI documentation in their favorite(s) frameworks.

            - Can do architecture diagrams in their favorite tool.
        """,
        "Resources and Activities": [
            "[05a [Individual] Create OpenAPI Documentation](00._Course_Material/01._Assignments/05._Documentation/05a._[Individual]_Create_OpenAPI_Documentation.md)", 
            "[05b [Pair] Expose and integrate with a webhook system](00._Course_Material/01._Assignments//05._Documentation/05b._[Pair]_Expose_and_integrate_with_a_webhook_system.md)"
            "[Resource: Video on OpenAPI](https://www.youtube.com/watch?v=pRS9LRBgjYg)",
    
        ]
    },
    {
        "Title": "",
        "Date": "March 14th", 
        "Description": """
        """,
        "Learning Goals": """
        """,
        "Resources and Activities": [
        ]
    },
    {
        "Title": "",
        "Date": "March 21st", 
        "Description": """
        """,
        "Learning Goals": """
        """,
        "Resources and Activities": [
            "[**MANDATORY I DEADLINE**](00._Course_Material/01._Assignments/00._Mandatories/01._Mandatory_I.md)",          
        ]
    },
]


def generate_markdown_table(data, readme_file_path):
    headers = data[0].keys()

    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"

    table_rows = [header_row, separator_row]

    absolute_path = readme_file_path.replace("README.md", "")

    for row in data:
        row_values = []
        for key in headers:
            if key == "Resources and Activities":
                for markdown_link in row[key]:
                    check_if_filepath_is_valid(absolute_path, markdown_link)
                resources_str = "<br><br>".join(row[key])
                row_values.append(resources_str)
            else:
                formatted_value = row[key].replace("\n", "<br>")
                row_values.append(formatted_value)
        row_str = "| " + " | ".join(row_values) + " |"
        table_rows.append(row_str)

    return "\n".join(table_rows)


def replace_section_in_file(file_path, section_title, new_content):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Identify the section to replace
    section_start = None
    for i, line in enumerate(lines):
        if line.strip() == f"## {section_title}":
            section_start = i + 1
            break

    if section_start is None:
        return  # Section title not found

    # Find the end of the section
    section_end = None
    for i in range(section_start, len(lines)):
        if lines[i].startswith("## "):
            section_end = i
            break

    # Replace the section content
    if section_end is not None:
        lines[section_start:section_end] = [new_content + '\n']
    else:  # If the section goes until the end of the file
        lines[section_start:] = [new_content + '\n']

    # Write back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)


# to enable running this file from anywhere within a repository
# it will keep trying one level higher until it finds a README.md file
def find_readme_file(start_dir):
    current_dir = start_dir
    while True:
        readme_path = os.path.join(current_dir, 'README.md')
        if os.path.isfile(readme_path):
            return readme_path
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # reached the root directory
            return None
        current_dir = parent_dir


def check_if_filepath_is_valid(absolute_path, markdown_link):
     # Extract relative path from markdown link
    start = markdown_link.find('(') + 1
    end = markdown_link.find(')')
    relative_path = markdown_link[start:end]

    if relative_path.startswith("http"):
        return
    
    full_path = os.path.join(absolute_path, relative_path)
    
    is_valid = Path(full_path).exists()

    if not is_valid:
        # print red text
        print(f"\033[31m{full_path}\033[0m")



current_script_path_absolute = os.path.abspath(__file__)
readme_file_path = find_readme_file(current_script_path_absolute)
markdown_table = generate_markdown_table(table_data, readme_file_path)
replace_section_in_file(readme_file_path, 'Semester Plan', "\n\n" + markdown_table)

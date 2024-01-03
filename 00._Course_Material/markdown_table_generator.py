# todo add Google Drive link to slides and Github link in Teams
table_data = [
    {
        "Title": "Introduction + Data Formats",
        "Date": "Feb. 1st", 
        "Description": """
            - Data encoding 

            - Hashing, serializing, marshalling

            - Packages eco system in Node and Python

            - REST APIs
        """,
        "Learning Goals": """

            - Can argue about different build tools for Python and understands their pros and cons. 

            - Can use poetry. 

            - Understands encoding, serializing and marshalling. Knows about charsets and encoding types.
        """,
        "Resources and Activities": [
            "[01a [Individual] File formats bonanza!](00._Course_Material/00._assignments/01._Introduction_Data_Formats/01._[Individual]_File_formats_bonanza!.md)",
            "[[Individual] Azure for Students](00._Course_Material/00._assignments/01._Introduction_Data_Formats/00._[Individual]_Azure_For_Students.md)",
          
        ]
    },
    {
        "Title": "Data",
        "Date": "Feb. 8th", 
        "Description": """
            - Intro / This course

            - Environment Setup

            - File types and data formats.

            - Python Modules

            - Starting with Node and Express

            = Weekly Grubler: Cheap static deployment.
        """,
        "Learning Goals": """
            - Alternatives to REST API.

            - Data formats. TXT, JSON, YAML, CSV, XML

            - Can parse files in these formats after the homework.

            - Can run files with Node and Python.

            - Can work with modules in Python / Javascript (frontend and backend).
        """,
        "Resources and Activities": [
            "[[02a [Individual] Data format translation servers - Part II](00._Course_Material/00._assignments/02._Data/02a._[Individual]_Data_format_translation_servers_-_Part_II.md)",
            "[[Optional] Serialize / Marshall data](00._Course_Material/00._assignments/02._Data/00._[Optional]_Serialize__Marshall_data.md)",
          
        ]
    },
    {
        "Title": "Server to server / Real-time communication - Part I",
        "Date": "Feb. 15th", 
        "Description": """
            - Date

            - Communication

            - Making a server act as a client to another server.

            - ngrok 

            - Environment Variables (OS level, Runtime environment level)
        """,
        "Learning Goals": """
            - Understand how date affects systems and communication between services.

            - Understands challenges and edge cases when working with date and why this is important during integration.

            - Knows about different communication protocols on a superficial level.

            - Knows how to make a HTTP requests between languages. 

            - Can use ngrok

            - Understand the different levels of environment variables and how they differ. 

            - Knows how to define environment variables in different languages.
        """,
        "Resources and Activities": [
            "03. [Pair] Database granular access](00._Course_Material/00._assignments/03._Server_to_server_Real-time_communication_-_Part_I/03a._[Pair]_Database_granular_access.md)",          
        ]
    },
    {
        "Title": "Documentation",
        "Date": "Feb. 22nd", 
        "Description": """
            - Backing up MySQL

            - Documenting MySQL 

            - OpenAPI

            - Swagger + Express/FastAPI/Spring

            - Architecture Diagrams

            - Azure Virtual Machines
        """,
        "Learning Goals": """
            - Can document and backup MySQL

            - Has considered how to document the databases they are familiar with.

            - Understands the what and why of OpenAPI

            - Can generate OpenAPI documentation in their favorite(s) frameworks.

            - Can do architecture diagrams in their favorite tool.

            - Can create virtual machines without aid on your favorite hosting platform.
        """,
        "Resources and Activities": [
            "04a [Individual] Create OpenAPI Documentation](00._Course_Material/00._assignments/04._Documentation/04a._[Individual]_Create_OpenAPI_Documentationss.md)", 
            "[Resource: Video on OpenAPI](https://www.youtube.com/watch?v=pRS9LRBgjYg)"         
        ]
    },
    {
        "Title": "Real-time communication - Part II",
        "Date": "Feb. 29th", 
        "Description": """
            - Client polling, short polling, long polling.

            - Server-sent events

            - Webhooks
        """,
        "Learning Goals": """
            - Understands client polling, short polling, long polling and the pros and cons of each approach.

            - Understands SSE and can explain how to implement it. Has an example ready. 

            - Understands the pros and cons of SSE and can compare it to Websockets. 

            - Can recall how we did Github Wehooks without having to be able to do it on the fly. Can illustrate exactly how it works by drawing a diagram.

            - Understands how to approach building a custom webhook system.
        """,
        "Resources and Activities": [
            "05a [Individual] SSE example](00._Course_Material/00._assignments/05._Real-time_communication_-_Part_II/05a._[Individual]_SSE_example.md)", 
            "05b [Pair] Expose and integrate with a webhook system](00._Course_Material/00._assignments/05._Real-time_communication_-_Part_II/05b._[Pair]_Expose_and_integrate_with_a_webhook_system.md", 
        ]
    },
    {
        "Title": "Cloud",
        "Date": "March 7th", 
        "Description": """
                Azure:
                - Virtual Machines
                - Blob Storage
                - Functions

                Terraform
        """,
        "Learning Goals": """
            - Can create serverless functions (AWS Lambda, Azure Functions, Vercel etc).
        """,
        "Resources and Activities": [
        ]
    },
    {
        "Title": "No Lecture",
        "Date": "March 14th", 
        "Description": """
            Work on the homework. 
        """,
        "Learning Goals": """
        """,
        "Resources and Activities": [
        ]
    },
]


def generate_markdown_table(data):
    headers = data[0].keys()

    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"

    table_rows = [header_row, separator_row]

    for row in data:
        row_values = []
        for key in headers:
            if key == "Resources and Activities":
                resources_str = "<br><br>".join(row[key])
                row_values.append(resources_str)
            else:
                formatted_value = row[key].replace("\n", "<br>")
                row_values.append(formatted_value)
        row_str = "| " + " | ".join(row_values) + " |"
        table_rows.append(row_str)

    return "\n".join(table_rows)


markdown_table = generate_markdown_table(table_data)

print(markdown_table)
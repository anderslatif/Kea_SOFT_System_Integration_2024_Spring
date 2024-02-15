from dotenv import dotenv_values, load_dotenv

# Example 1
environment_variables = dotenv_values()
print(environment_variables["MYSQL_PASSWORD"])

# Example 2
import os

load_dotenv()
print(os.getenv("MYSQL_PASSWORD"))


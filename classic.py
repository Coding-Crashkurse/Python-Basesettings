import os

# set mysql_password=test

print(os.environ.get("MYSQL_USER", "user"))
print(os.environ.get("MYSQL_PASSWORD"))
print(os.environ.get("MYSQL_DATABASE"))

from dotenv import load_dotenv
load_dotenv()

print(os.environ.get("MYSQL_USER", "user"))
print(os.environ.get("MYSQL_PASSWORD"))
print(os.environ.get("MYSQL_DATABASE"))

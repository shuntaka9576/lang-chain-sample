# https://python.langchain.com/v0.1/docs/use_cases/sql/quickstart/
from langchain_openai import ChatOpenAI, OpenAI
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
import os


with open(".OPEN_AI_API_KEY", "r") as f:
    os.environ["OPENAI_API_KEY"] = f.read().strip()


db = SQLDatabase.from_uri("sqlite:///Chinook.db")
# print(db.dialect)
# print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "Aから始まるアーティストは？"})

print(response)

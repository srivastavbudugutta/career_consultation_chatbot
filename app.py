import json
import random
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
import psycopg, os
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
import psycopg, os
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
import psycopg2
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI
# from langchain.agent import create_sql_agent
from sqlalchemy import create_engine
# from langchain.toolkits import SQLDatabaseToolkit




def chatbot_response(msg):

    engine = create_engine(conn_str)
    db = SQLDatabase(engine)
    # Instantiate the ChatOpenAI model
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k-0613")

    # Initialize the SQLDatabaseToolkit with the SQLAlchemy engine
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    # Create the agent executor with the SQL toolkit and ChatOpenAI model
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
    )

    res = agent_executor.run(f"{msg}")
    print(f"Function avaialble for response are {res}")
    print("This is the response")
    print(res)
    return res


from flask import Flask, render_template, request

app = Flask(__name__)
app.template_folder = 'templates'
app.static_folder = 'templates'

os.environ['OPENAI_API_KEY'] = "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"
db_user = "postgres"
db_password = "postgres"
db_host = "apan5400db.cv57tdjwt2lt.us-east-1.rds.amazonaws.com"
db_name = "postgres"
conn_str = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}"
# Create a SQLAlchemy engine



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


if __name__ == "__main__":
    app.run()
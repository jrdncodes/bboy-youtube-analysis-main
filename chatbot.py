# text_to_sql_chatbot.py
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase

# --- Connect to your database ---
db = SQLDatabase.from_uri(
    "postgresql://USERNAME:PASSWORD@HOST:PORT/youtube_analysis"
)

# --- Initialize OpenAI Chat model ---
chat = ChatOpenAI(
    temperature=0,  # deterministic answers
    model_name="gpt-3.5-turbo"  # or "gpt-4"
)

# --- Create the Text-to-SQL agent ---
agent = create_sql_agent(chat, db, verbose=True)

# --- Chat loop ---
print("B-boy Video Analytics Chatbot (type 'exit' to quit)")
while True:
    user_input = input("Ask a question: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    try:
        response = agent.run(user_input)
        print("\nAnswer:\n", response, "\n")
    except Exception as e:
        print("Error:", e)
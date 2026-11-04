from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b",temperature=0,max_tokens=10,)
response = model.invoke("Write a joke on AI")
print(response.content)
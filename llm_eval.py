# from opik.integrations.openai import track_openai
# from openai import OpenAI
# import json

# os.environ["OPIK_PROJECT_NAME"] = "langchain-integration-demo"
# client = OpenAI()

# openai_client = track_openai(client)

# prompt = """
# Create 20 different example questions a user might ask based on the Chinook Database.

# These questions should be complex and require the model to think. They should include complex joins and window functions to answer.

# Return the response as a json object with a "result" key and an array of strings with the question.
# """

# completion = openai_client.chat.completions.create(
#     model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
# )

# print(completion.choices[0].message.content)

from opik import track
# from opik.integrations.openai import track_openai
# from openai import OpenAI
import os 
os.environ["OPIK_PROJECT_NAME"] = "langchain-integration-demo"
# Wrap your OpenAI client
# openai_client = OpenAI()
# openai_client = track_openai(openai_client)
from langchain_groq import ChatGroq

llm = ChatGroq(model="mixtral-8x7b-32768")
print(llm.invoke("How are you"))


# Create your chain
# @track
# def llm_chain(input_text):
#     context = retrieve_context(input_text)
#     response = generate_response(input_text, context)

#     return response

# llm_chain("Hello, how are you?")
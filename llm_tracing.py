# from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from opik.integrations.langchain import OpikTracer
from langchain_ollama.llms import OllamaLLM
import opik
import os

# opik.configure()

opik_tracer = OpikTracer()


llm = OllamaLLM(model="llama3.2")

prompt_template = PromptTemplate(
    input_variables=["input"],
    template="Answer the question thoughtfully and professionally: {input}"
    # template=(
    #     "You are a highly knowledgeable and friendly assistant designed to help users. "
    #     "Answer the question thoughtfully and professionally: {input}"
    # )
)


llm_chain = prompt_template | llm.with_config({"callbacks": [opik_tracer]})

res = llm_chain.invoke({"input": "what is machine learning"}, callbacks=[opik_tracer])


print(res)


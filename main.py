from config import *
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain  # Used to make LLM chain for the prompt.

cities = ["New York City", "Los Angeles", "Chicago", "Australia"]

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)
prompt = PromptTemplate.from_template("What is the capital of {location} ?")
chain = LLMChain(llm=llm, prompt=prompt)
for city in cities:
    result = chain.run(city)  # Providing the parameter for which response will be generated.
    print(result)

from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

prompt = PromptTemplate(
    template="wrie a summary for the following poem - \n {poem}",
    input_variables=["poem"]
)

parser = StrOutputParser()


loader = TextLoader("cricket.txt",encoding="utf-8")
docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({"poem":docs[0].page_content}))
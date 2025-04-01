from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text -\n{text}",
    input_variables=["question","text"]
)

parser = StrOutputParser()

url = 'https://theprint.in/politics/why-modis-visit-to-rss-headquarters-a-first-for-an-indian-pm-is-significant/2571326/'

loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | model | parser

res = chain.invoke({"question":"summarize this text","text":docs})
print(res)
from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

loader = PyPDFLoader("dl-curriculum.pdf")
docs = loader.load()

print(docs[0].page_content)
print(len(docs))
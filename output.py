from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def get_json_output(document_text: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
    )

    prompt = PromptTemplate(
        template="""
You are an intelligent assistant. The following is OCR extracted text from a document.

Extract the information and return a structured JSON object with relevant key-value pairs.

Only output valid JSON.

OCR TEXT:
{ocr_chunk}
""",
        input_variables=["ocr_chunk"]
    )

    parser = JsonOutputParser()

    chain: Runnable = prompt | llm | parser

    result = chain.invoke({"ocr_chunk": document_text})

    return result

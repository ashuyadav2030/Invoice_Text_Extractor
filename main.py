from fastapi import FastAPI, UploadFile, File
from ocr import get_document_text
from output import get_json_output
import shutil
from pathlib import Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the OCR and LLM API!"}


@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    temp_file_path = Path(f"temp_{file.filename}")
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document_text = get_document_text(str(temp_file_path))

    json_output = get_json_output(document_text)

    temp_file_path.unlink(missing_ok=True)

    return json_output

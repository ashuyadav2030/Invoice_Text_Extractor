# 🧠 OCR-to-JSON API with PaddleOCR + Gemini AI

A modular OCR pipeline that extracts text from documents using **PaddleOCR**, converts the raw output to structured JSON using **LangChain + Gemini AI**, and serves everything via a **FastAPI** endpoint.

---

## 📁 Project Structure

```
ocr_project/
├── ocr.py         # Uses PaddleOCR to extract raw text from uploaded images
├── output.py      # Converts raw text into structured JSON using LangChain + Gemini AI
├── main.py        # FastAPI API to run the entire OCR + JSON conversion pipeline
├── requirements.txt
└── README.md
```

---

## 🚀 Features

- ✅ Extracts text using deep learning-based OCR (PaddleOCR)
- 🤖 Converts raw text into structured JSON via Google Gemini API using LangChain
- ⚡ FastAPI endpoint for image-based text-to-JSON processing
- 🐳 Easily deployable and customizable

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ashuyadav2030/Invoice_Text_Extractor.git
cd ocr-json-api
```

### 2. Create Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Your Gemini API Key

```bash
export GEMINI_API_KEY="your_gemini_api_key_here"  # or set in .env file
```

### 4. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Server will start at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 API Endpoint

### `POST /ocr-json`

Upload an image to receive raw text + AI-structured JSON.

#### Form-Data Parameters:

| Field  | Type   | Required | Description                 |
|--------|--------|----------|-----------------------------|
| file   | image  | ✅       | The image to be processed   |

#### Example cURL:

```bash
curl -X POST "http://localhost:8000/ocr-json" \
  -F "file=@sample_invoice.jpg"
```

#### Example JSON Response:

```json
{
  "raw_text": [
    "Invoice No: 12345",
    "Date: 2024-07-15",
    "Item: Biscuit Pack - ₹30"
  ],
  "structured_json": {
    "invoice_number": "12345",
    "date": "2024-07-15",
    "items": [
      {
        "name": "Biscuit Pack",
        "price": 30
      }
    ]
  }
}
```

---

## ⚙️ How It Works

- **`ocr.py`**:  
  Uses PaddleOCR to extract all visible text from the uploaded image.

- **`output.py`**:  
  Uses LangChain to send the extracted text to Gemini AI and prompt it to return structured JSON.

- **`main.py`**:  
  Hosts a FastAPI endpoint that chains both steps and returns both raw and structured outputs.

---

## 📦 Dependencies

Make sure these packages are listed in `requirements.txt`:

```
fastapi
uvicorn
paddleocr
langchain
google-generativeai
python-multipart
pydantic
```

---

## 🔐 Environment Variables

| Variable         | Description                 |
|------------------|-----------------------------|
| `GEMINI_API_KEY` | Your Google Gemini API key  |

Use a `.env` file or export manually before running.

---

## 🧠 Use Cases

- Invoice data extraction
- Product catalog reading
- Retail shelf tag digitization
- Bill/receipt digitization

---

## 📍 Author

**Ashu Kumaar**  
AI Engineer | OCR & Computer Vision Specialist  
📍 India

---

## 📜 License

Licensed under the [MIT License](LICENSE).

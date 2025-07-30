from paddleocr import PaddleOCR
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)

def get_document_text(image_path):
    pipeline = ocr

    result = pipeline.predict(
        input=image_path,
    )

    ocr_texts = result[0]['rec_texts']
    document_text = "\n".join(ocr_texts)
    
    return document_text
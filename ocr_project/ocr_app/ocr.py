import cv2
from pytesseract import pytesseract
from django.conf import settings

# Set the Tesseract OCR path from settings.py
pytesseract.tesseract_cmd = settings.TESSERACT_CMD

def extract_text(image_path):
    image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image)
    return text

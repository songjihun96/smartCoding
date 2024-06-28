import pytesseract
from PIL import Image

img_path = "OCR\img1.PNG"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(Image.open(img_path), lang="kor")

print(text)

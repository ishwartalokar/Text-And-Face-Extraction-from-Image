from flask import Flask, render_template, request, redirect, url_for, flash
from PIL import Image
import pytesseract
import os
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


app = Flask(__name__)
app.config['imageCollection'] = './static/uploads'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def textExtract(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img,lang='mar+hin+eng')
    return text

def faceDetect(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        return None

    (x, y, w, h) = faces[0]
    cropped_face = img[y:y+h, x:x+w]

    cropped_face_path = os.path.join(app.config['imageCollection'], 'cropped_face.jpg')
    cv2.imwrite(cropped_face_path, cropped_face)

    return cropped_face_path

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('File Not Found')
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == '':
            flash('No any selected file')
            return redirect(request.url)

        if file:
            filename = file.filename
            filepath = os.path.join(app.config['imageCollection'], filename)
            file.save(filepath)
            extracted_text = textExtract(filepath)
            
            cropped_face_path = faceDetect(filepath)
            
            return render_template('output.html', text=extracted_text, cropped_face_path=cropped_face_path, os=os)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

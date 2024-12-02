
# The Text and Face Extraction From Image

This project is designed to process images by performing two key functions:

1. **Text Extraction**: Extract any text present in the input image and display it as output.  
2. **Face Detection**: Detect faces present in the image and display the detected faces visually.

## Features

- Extract text from images using Optical Character Recognition (OCR).  
- Detect and highlight faces using face detection algorithms.  
- Simple and efficient workflow for processing input images.  
- Display results (extracted text and detected faces) clearly.

---

## Installation

1. Clone this repository to your local system:
   ```bash
   git clone https://github.com/your-username/text-and-face-extraction.git
   cd text-and-face-extraction
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the following tools installed on your system:
   - Python 3.8 or higher
   - `Tesseract-OCR` (required for text extraction)

---

## Usage

1. **Input Image**: Provide an image containing text and/or faces.  
2. Run the script:
   ```bash
   python main.py --image path/to/image.jpg
   ```

3. **Output**:
   - The extracted text will be displayed in the terminal.  
   - A visual output file will be generated with detected faces highlighted.

---

## Example

### Input  
![Example Input](https://github.com/ishwartalokar/Text-And-Face-Extraction-from-Image/blob/main/idimage.jpg)

### Output
- **Extracted Text**:  
  ```
  This is an example text extracted from the image.
  ```
- **Detected Faces**:  
  ![Example Output](path/to/example-output.jpg)

---

## Dependencies

This project uses the following libraries and tools:

- **OpenCV**: For face detection and image processing.  
- **Pytesseract**: For Optical Character Recognition (OCR).  
- **NumPy**: For efficient array manipulation.  

To install `Tesseract-OCR`, follow the instructions for your operating system:  
- **Windows**: [Tesseract for Windows](https://github.com/tesseract-ocr/tesseract)  
- **Linux**: Use your package manager (e.g., `sudo apt install tesseract-ocr`).  
- **Mac**: Install via Homebrew (`brew install tesseract`).

---

## Folder Structure

```
project/
│
├── main/
│   ├── static/                  # Static files for the project
│   │   ├── css/                 # Stylesheets
│   │   └── uploads/             # Uploaded images or files
│   │
│   ├── templates/               # HTML templates for the web app
│   │   ├── index.html           # Main input page for the user
│   │   └── output.html          # Output page to display results
│   │
│   └── main.py                  # Main Python script for running the project
│
└── README.md                    # Project documentation
```

---

## Future Enhancements

- Support for multi-language text extraction.  
- Improve face detection accuracy using advanced deep learning models.  
- Batch processing for multiple images.

---

## Acknowledgments

- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) for text extraction.  
- [OpenCV](https://opencv.org/) for face detection and image processing.  

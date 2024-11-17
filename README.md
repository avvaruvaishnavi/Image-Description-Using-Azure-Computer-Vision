# Image-Description-Using-Azure-Computer-Vision

# Description

This Python script uses Azure's Computer Vision API to describe an image and output captions with confidence scores. The program analyzes an image URL and identifies the image and provides a description and their confidence levels.

## Setup Instructions

1. **Install Dependencies**:
   Install the required Python libraries by running:
   ```bash
   pip install azure-cognitiveservices-vision-computervision msrest
   ```

2. **Create `cred.py` File**:
   In your project directory, create a file called `cred.py` and store your Azure **API key** and **Endpoint URL** there.
   ```python
   # cred.py
   url = "your-azure-endpoint-url"
   key = "your-azure-api-key"
   ```

3. **Modify the Image URL**:
   Change the `img` variable in the script to the URL of the image you want to analyze.
   ```python
   img = "https://example.com/your-image-url.jpg"  # Replace with your image URL

 4. **Run the Script**:
   After setting up `cred.py` and modifying the image URL, run the Python script:
   ```bash
   python main.py
   ```

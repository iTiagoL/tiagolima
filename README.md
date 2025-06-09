# Denodo Metadata Reporter

This repository contains a small Flask application that connects to Denodo,
fetches metadata information and generates a Word report.

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser at `http://localhost:5000` and provide your Denodo
   connection details. A Word document containing metadata information will be
   generated for download.

The metadata extraction function contains placeholder code. Adjust it to match
your Denodo installation and authentication method.

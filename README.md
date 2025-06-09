# Denodo Metadata Reporter

This repository contains a small Flask application that parses a Denodo
configuration file and generates a Word report with extracted metadata.

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser at `http://localhost:5000` and upload a configuration
   file. A Word document containing metadata information (such as heap memory
   configuration) will be generated for download.

The metadata extraction logic contains simple pattern matching for the heap
memory setting. Adjust it to match your configuration format.

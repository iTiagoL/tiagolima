from flask import Flask, render_template, request, send_file
from src.metadata_reporter import fetch_denodo_metadata, generate_word_report
import tempfile
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files.get('metadata_file')
        if not uploaded_file:
            return render_template('index.html', error='No file provided')

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            uploaded_file.save(tmp.name)
            file_path = tmp.name

        output_path = 'denodo_report.docx'
        metadata = fetch_denodo_metadata(file_path)
        generate_word_report(metadata, output_path)

        os.remove(file_path)
        return send_file(output_path, as_attachment=True)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

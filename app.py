from flask import Flask, render_template, request, send_file
from src.metadata_reporter import fetch_denodo_metadata, generate_word_report
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        host = request.form['host']
        user = request.form['user']
        password = request.form['password']
        output_path = 'denodo_report.docx'

        metadata = fetch_denodo_metadata(host, user, password)
        generate_word_report(metadata, output_path)

        return send_file(output_path, as_attachment=True)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

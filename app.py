import os
import tempfile
from io import BytesIO
from zipfile import BadZipFile

from docx.opc.exceptions import PackageNotFoundError
from flask import Flask, request, render_template, send_file
from document_processor import process_document

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error='No file selected.'), 400

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error='No file selected.'), 400

    if not file.filename.lower().endswith('.docx'):
        return render_template('index.html', error='Please upload a .docx file.'), 400

    input_tmp = None
    output_tmp = None
    try:
        input_tmp = tempfile.NamedTemporaryFile(suffix='.docx', delete=False)
        file.save(input_tmp.name)
        input_tmp.close()

        if os.path.getsize(input_tmp.name) == 0:
            return render_template('index.html', error='The uploaded file is empty.'), 400

        output_tmp = tempfile.NamedTemporaryFile(suffix='.docx', delete=False)
        output_tmp.close()

        process_document(input_tmp.name, output_tmp.name)

        original_name = os.path.splitext(file.filename)[0]
        download_name = f'branded_{original_name}.docx'

        # Read into memory so we can clean up temp files immediately
        with open(output_tmp.name, 'rb') as f:
            output_data = BytesIO(f.read())

        return send_file(
            output_data,
            as_attachment=True,
            download_name=download_name,
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        )

    except (BadZipFile, PackageNotFoundError):
        return render_template(
            'index.html',
            error='The uploaded file does not appear to be a valid Word document.',
        ), 400
    except Exception:
        return render_template(
            'index.html',
            error='An error occurred while processing your document. Please try again.',
        ), 500
    finally:
        if input_tmp and os.path.exists(input_tmp.name):
            os.unlink(input_tmp.name)
        if output_tmp and os.path.exists(output_tmp.name):
            os.unlink(output_tmp.name)


@app.errorhandler(413)
def file_too_large(e):
    return render_template(
        'index.html',
        error='File too large. Maximum size is 16 MB.',
    ), 413


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

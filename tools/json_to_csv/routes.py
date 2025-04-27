from flask import render_template, request, send_file
import json
from . import json_to_csv_bp
from .logic import convert_json_to_excel

@json_to_csv_bp.route('/', methods=['GET', 'POST'])
def json_to_csv():
    error = None

    if request.method == 'POST':
        json_data = None

        # Check if file was uploaded
        uploaded_file = request.files.get('json_file')
        if uploaded_file and uploaded_file.filename.endswith('.json'):
            try:
                json_data = json.load(uploaded_file)
            except json.JSONDecodeError:
                error = "Uploaded file contains invalid JSON."
        else:
            # Fallback to textarea input
            raw_input = request.form.get('json_data')
            if raw_input:
                try:
                    json_data = json.loads(raw_input)
                except json.JSONDecodeError:
                    error = "Invalid JSON format in text input."

        if json_data and not error:
            try:
                excel_data = convert_json_to_excel(json_data)
                return send_file(
                    excel_data,
                    mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    as_attachment=True,
                    download_name='data.xlsx'
                )
            except Exception as e:
                error = f"An error occurred: {e}"

    return render_template('json_to_csv.html', error=error)

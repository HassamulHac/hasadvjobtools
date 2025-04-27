from flask import render_template, request
from . import url_tool_bp
from .logic import encode_url, decode_url

@url_tool_bp.route('/', methods=['GET', 'POST'])
def url_tool():
    encoded_url = None
    decoded_url = None

    if request.method == 'POST':
        action = request.form.get('action')
        url_input = request.form.get('url_input')

        if action == 'encode' and url_input:
            encoded_url = encode_url(url_input)
        elif action == 'decode' and url_input:
            decoded_url = decode_url(url_input)

    return render_template('url_tool.html', encoded_url=encoded_url, decoded_url=decoded_url)

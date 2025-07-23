from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from analyzer import analyze_colors

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/analyze', methods=['Post'])
def analyzer():
    if 'image' not in request.files:
        return jsonify({'error occured': 'Image file required'}), 400
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No filename'}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    file.save(filepath)
    
    result = analyze_colors(filepath)
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)
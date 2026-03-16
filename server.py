from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "Нет файла"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Пустое имя файла"}), 400
    
    if file:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        # Формируем ссылку для скачивания на основе текущего хоста
        download_link = request.host_url.rstrip('/') + '/' + file.filename
        return jsonify({
            "link": download_link,
            "status": "success"
        })

@app.route('/<path:filename>')
def download_file(filename):
    """Раздача загруженных файлов"""
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
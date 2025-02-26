from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import yt_dlp
import os

app = Flask(__name__)
CORS(app)  # 🔥 Esto habilita CORS en todas las rutas

DOWNLOADS_FOLDER = "downloads"
os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    format = data.get('format')

    if not url:
        return jsonify({"error": "No se proporcionó una URL"}), 400

    filename = f"video.{format}"
    filepath = os.path.join(DOWNLOADS_FOLDER, filename)

    options = {
        'format': 'bestaudio' if format == 'mp3' else 'bestvideo',
        'outtmpl': filepath,
        'ffmpeg_location': 'C:\\ffmpeg\\bin\\ffmpeg.exe',  # 🔥 Especifica la ruta completa
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}] if format == 'mp3' else []
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        
        return jsonify({"file": f"http://localhost:5000/{filename}"})  # 🔥 Devuelve la URL de descarga

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/<filename>', methods=['GET'])
def serve_file(filename):
    return send_file(os.path.join(DOWNLOADS_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

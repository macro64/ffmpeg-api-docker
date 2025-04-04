from flask import Flask, request, send_file, jsonify
import subprocess
import os
import uuid

app = Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture():
    data = request.get_json()
    stream_url = data.get('stream')
    duration = data.get('duration', 10)  # Standard: 10 Sekunden

    if not stream_url:
        return jsonify({"error": "Missing 'stream' parameter"}), 400

    # Erzeuge einen eindeutigen Dateinamen
    filename = f"/tmp/{uuid.uuid4().hex}.mp4"

    cmd = [
        "ffmpeg",
        "-y",
        "-i", stream_url,
        "-t", str(duration),
        "-r", "30",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-pix_fmt", "yuv420p",
        "-an",  # keine Audioverarbeitung, falls nicht vorhanden
        filename
    ]

    try:
        subprocess.run(cmd, check=True)
        return send_file(filename, mimetype="video/mp4")
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

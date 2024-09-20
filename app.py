from flask import Flask, request, render_template, send_file
from redvid import Downloader
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    filename = "downloaded_video"

    dl = Downloader()
    dl.overwrite = True
    dl.max = True
    dl.url = url
    dl.filename = filename

    dl.download()

    file_path = f"{filename}.mp4"
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

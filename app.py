from __future__ import unicode_literals
from flask import Flask, render_template, request
import os
import youtube_dl

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    path = request.form.get("path")
    link = request.form.get("link")

    try:
        ydl_opts = {}
        os.chdir(path)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return render_template('index.html', status_text='Downloaded successfully!')
    except Exception as e:
        print(e)
        return render_template('index.html', status_text='Invalid input or error occurred!')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

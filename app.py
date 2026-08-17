from flask import Flask, render_template, request
import os
import sys
import webview
import yt_dlp

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder,
    static_folder=static_folder)
else:    
    app = Flask(__name__)

@app.route('/download', methods=['POST'])
def  download():
    voltar = '<br><b><a href="/">Voltar</a></b>'
    try:
        url = request.form.get('url')
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            return f"Download concluído!{voltar}"
    except Exception as e:
        return f"Erro ao tentar baixar o vídeo: {str(e)}.{voltar}" 
    
if __name__ == '__main__':
     window = webview.create_window(
        title="Download de videos",
        url=app,
        width=1000,
        height=700
    )

webview.start()     
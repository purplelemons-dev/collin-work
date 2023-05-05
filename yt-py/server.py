import openai
import json
from yt_dlp import YoutubeDL
from os import remove
from http.server import BaseHTTPRequestHandler, HTTPServer

openai.api_key = ...

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
        'preferredquality': '128',
    }],
    "outtmpl": "audio.m4a"
}

ytdl = YoutubeDL(ydl_opts)

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/getscript":
            # get the json body
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            body = json.loads(body)
            # body["url"] is the url of the youtube video
            print(body["url"])
            # download the audio
            ytdl.download([body["url"]])

            # get the audio file
            with open("./audio.m4a", "rb") as f:
                transcript:str = openai.Audio.transcribe(
                    file=f,
                    model="whisper-1"
                )["text"]
            # send the transcript back
            self.send_response(200)
            self.end_headers()
            self.wfile.write(transcript.encode("utf-8"))
            # delete the video file
            remove("./audio.m4a")

            return
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        # Try serving out of ./public first
        try:
            if self.path == "/":
                self.path = "/index.html"
            with open("./public" + self.path, "rb") as f:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f.read())
                return
        except FileNotFoundError:
            # open ./public/error404.html
            with open("./public/error404.html", "rb") as f:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(f.read())
            return


server = HTTPServer(("localhost", 10006), Handler)
print("Server started at http://localhost:10006")
server.serve_forever()

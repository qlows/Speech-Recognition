from concurrent.futures import thread
import re
from django.shortcuts import redirect
from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("Form Data Received")

        # If the file isn't there return to home
        if "file" not in request.files:
            return redirect(request.url)

        # If the file is empty return to home
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        # Take the audio file analyze it with speech recognizing module and transcribe it
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key = None)

    return render_template("index.html", transcript = transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 09:13:23 2021

@author: arianna.parisi
"""

"""
pip install SpeechRecognition
pip install flask
"""

from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file .filename == "":
            return redirect(request.url)
        
        if file:
            recognizer = sr.Recognizer()
            audio = sr.AudioFile(file)
            with audio as f:
                data = recognizer.record(f)
            text = recognizer.recognize_google(data, language="en-US", key=None) #"en-US"
            
    return render_template("index.html", trascription=text)

if __name__ == "__main__":
    app.run(debug = True, threaded = True)
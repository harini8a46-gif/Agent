import os, urllib.parse, urllib.request, render_template
from app.youtube import youtube_bp

Gemini_apo_key = "Gemini_API_key_2";

def home():
  return render_template ("index.html")

def create_app():
  appp = Flask(_name_)
  app.register_blueprint(youtube_bp, url_prefix="/youtube")

@app.route("/html")
def html():
  return render_template("index.html")
  
  return app;

import os

from flask import Flask, request, jsonify, render_template
from flask_cor import CORS

from app.gmail import (
  is_email_command,
  extract_email,
  create_gmail_url,
generate_emailo_with_gemini
)

from app.youtube import youtube_bp

def create_app():

  app = Flask(__name__)
  CORS(app)

#Youtube
app.register_blueprint(
    youtube_bp,
    url_prefix= "/youtube"
)

#Home
@app.route("/")
def home():
    return render_template("index.html")

#Html
@app.route("/html")
def html():
  return render_template("index.html")

#Health
@app.route("/health")
def health():
  return jsonify({
    "status":"ok",
    "service": "Nova AI Agent"

  })

#Gmail AI agent
@app.route("/agent", methods=["POST"])
def agent():
https://github.com/harini8a46-gif/Agent/tree/main
  try:
    data = request.get_json(silent=true) or {}
    command = data.get("command",""),strip()

if not command:
  return jsonify({
    "success": False,
    "message": "command is required"
  }), 400

recipient = extract_email(command)
email = generate_email_with_gemini(command)

return jsonify({
  "success": True,
  "type": "email",
  "email_generated": recipient,
  "subject": email["subject"],
  "body": email["body"],
  "gmail_url": create_gmail_url(
    email["subject"],
  )
})

expect exception as e:

return jsonify({
  "success": False,
  "message": str(e)
}), 500

return app
  

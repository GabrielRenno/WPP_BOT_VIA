# app.py
import os
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from langchain_bot import get_answer  # from the file we created in Step 3

load_dotenv()

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    """
    This endpoint will be called by Twilio whenever a message is received on WhatsApp.
    """
    incoming_message = request.form.get("Body", "")
    sender = request.form.get("From", "")

    # Generate response from your LangChain + OpenAI setup
    bot_response = get_answer(incoming_message)

    # Create a Twilio MessagingResponse to reply to the user
    twilio_response = MessagingResponse()
    msg = twilio_response.message()
    msg.body(bot_response)

    return str(twilio_response)

if __name__ == "__main__":
    # For local testing, run the Flask app
    app.run(port=8080, debug=True)

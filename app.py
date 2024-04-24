from flask import Flask, render_template, request, jsonify
from PIL import Image
import os
import random
from datetime import datetime
import mysql.connector
from credentials import db_credentials, google_credentials
import google.generativeai as genai

app = Flask(__name__)

# Establish a connection to the database
db = mysql.connector.connect(**db_credentials)

# Assuming you have a module named 'google.generativeai'
genai.configure(api_key=google_credentials["GOOGLE_API_KEY"])

# Ensure using gemini-pro model
chosen_model_name = "gemini-pro"
chosen_model = genai.GenerativeModel(chosen_model_name)

# Complete list of tarot cards (Major Arcana)
tarot_cards = [
    # Include your tarot card list here...
]

logo_path = "images/logo.jpg"
absolute_logo_path = os.path.abspath(logo_path)
print(f"Absolute path to logo: {absolute_logo_path}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    question = request.form.get('question')

    if not question:
        return jsonify({"error": "Please enter a question."})

    try:
        similar_question = get_similar_question(question)
        if similar_question:
            response_text = f"Similar question found in the database. Using the same response:\n{similar_question['response']}"
            past_input, present_input, future_input = similar_question['past_card'], similar_question['present_card'], similar_question['future_card']
        else:
            past_input, present_input, future_input = generate_unique_tarot_cards()
            prompt = f"Q: {question}\nPast card is {past_input}\nPresent card is {present_input}\nFuture card is {future_input} explain it"

            chat = chosen_model.start_chat(history=[])
            response = chat.send_message(prompt, stream=True)

            response_text = ""
            for chunk in response:
                response_text += chunk.text

            save_to_database(question, response_text, past_input, present_input, future_input)

        past_img_path, present_img_path, future_img_path = display_card_images(past_input, present_input, future_input)

        return render_template('result.html', response_text=response_text,
                               past_img=past_img_path, present_img=present_img_path, future_img=future_img_path)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_unique_tarot_cards():
    while True:
        past_input, present_input, future_input = random.sample(tarot_cards, 3)
        used_combination = check_used_combination(past_input, present_input, future_input)
        if not used_combination:
            return past_input, present_input, future_input

def check_used_combination(past_card, present_card, future_card):
    date = datetime.now().strftime("%Y-%m-%d")
    cursor = db.cursor()
    cursor.execute('''
        SELECT * FROM tarot_responses
        WHERE date = %s AND past_card = %s AND present_card = %s AND future_card = %s
    ''', (date, past_card, present_card, future_card))
    result = cursor.fetchone()
    cursor.close()
    return result is not None

def get_similar_question(question):
    date = datetime.now().strftime("%Y-%m-%d")
    cursor = db.cursor()
    cursor.execute('''
        SELECT * FROM tarot_responses
        WHERE date = %s AND question = %s
    ''', (date, question))
    result = cursor.fetchone()
    cursor.close()
    if result:
        column_names = [desc[0] for desc in cursor.description]
        return dict(zip(column_names, result))
    else:
        return None

def display_card_images(past_card, present_card, future_card):
    images_folder = "images"
    past_image_path = os.path.join(images_folder, f"{past_card.lower().replace(' ', '_')}_card.jpg")
    present_image_path = os.path.join(images_folder, f"{present_card.lower().replace(' ', '_')}_card.jpg")
    future_image_path = os.path.join(images_folder, f"{future_card.lower().replace(' ', '_')}_card.jpg")

    try:
        past_img = Image.open(past_image_path).resize((100, 150))
        present_img = Image.open(present_image_path).resize((100, 150))
        future_img = Image.open(future_image_path).resize((100, 150))

        # You can save the resized images if necessary
        # past_img.save("resized_past_card.jpg")
        # present_img.save("resized_present_card.jpg")
        # future_img.save("resized_future_card.jpg")

        return past_img, present_img, future_img
    except Exception as e:
        raise e

def save_to_database(question, response, past_card, present_card, future_card):
    date = datetime.now().strftime("%Y-%m-%d")
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO tarot_responses (question, date, response, past_card, present_card, future_card)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (question, date, response, past_card, present_card, future_card))
    db.commit()
    cursor.close()

if __name__ == "__main__":
    app.run(debug=True)

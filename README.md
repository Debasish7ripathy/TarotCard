**README**

**Project Name:** Tarot Card Reading with Generative AI

**Description**

This Flask application leverages Google GenerativeAI to create a tarot card reading experience. Users can enter a question, and the app will:

- Generate a unique three-card spread (past, present, future) from the provided `tarot_cards` list.
- Check the database for a similar question asked on the same day. If a match is found, it retrieves the previously generated response and card readings.
- If no match is found, it prompts the chosen generative AI model (`gemini-pro`) to craft a narrative based on the question and card spread.
- Display the generated text response and images of the three tarot cards.
- Store the question, response, and card spread in the database (`tarot_responses`) for potential future reuse.

**Requirements**

- Python 3.x
- Flask
- Pillow (PIL Fork)
- PyMySQL (or a compatible MySQL connector)
- A Google Cloud account with GenerativeAI API enabled
- Credentials for database connection and Google Cloud (stored securely in `credentials.py`)

**Setup**

1. Install dependencies:

   ```bash
   pip install Flask Pillow PyMySQL google-cloud-aiplatform
   ```

2. Create a `credentials.py` file with your database credentials and Google Cloud API key:

   ```python
   db_credentials = {
       "host": "your_database_host",
       "user": "your_database_user",
       "password": "your_database_password",
       "database": "your_database_name"
   }

   google_credentials = {
       "GOOGLE_API_KEY": "your_google_cloud_api_key"
   }
   ```

3. Replace the placeholder values in `credentials.py` with your actual credentials.

4. (Optional) Update the `tarot_cards` list in `app.py` to include your preferred tarot cards.

**Running the Application**

1. Start the development server:

   ```bash
   python app.py
   ```

2. Access the application in your web browser at `http://127.0.0.1:5000/` (or the port specified by `app.run`).

**Database Schema**

The application expects a database table named `tarot_responses` with the following columns:

| Column Name     | Data Type | Description                                          |
|----------------|------------|-------------------------------------------------------|
| question        | text       | User-entered question                                 |
| date            | date       | Date the question was asked (YYYY-MM-DD)               |
| response        | text       | Generated response from the AI model                  |
| past_card        | text       | Past tarot card in the reading                         |
| present_card    | text       | Present tarot card in the reading                      |
| future_card     | text       | Future tarot card in the reading                       |

**Additional Notes**

- Error handling is implemented to provide informative messages to the user in case of issues.
- Image resizing is included for potential optimization, but commented out for flexibility. You can uncomment the relevant lines if desired.
- Consider implementing security measures (e.g., input validation, user authentication) for a production environment.

I hope this enhanced README provides a clear and comprehensive guide to using the application!

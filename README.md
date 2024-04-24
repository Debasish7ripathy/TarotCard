**README**

**Project Name:** Tarot Card Reading with Generative AI

**Description**

Welcome to the Tarot Card Reading with Generative AI project! This Flask application offers an immersive tarot card reading experience powered by Google GenerativeAI. Users can pose questions and receive personalized three-card spreads, comprising past, present, and future insights. The application employs a blend of tarot symbolism and AI-generated narratives to provide unique and thought-provoking responses.

**Features**

- **Personalized Readings**: Users can input their questions, prompting the app to generate a tailored three-card spread.
  
- **Historical Context**: The application checks for similar questions asked on the same day and retrieves previous responses if available, offering continuity and insight into recurring themes.

- **Generative AI Integration**: Leveraging the `gemini-pro` model from Google GenerativeAI, the app crafts narrative responses based on user questions and card spreads.

- **Interactive Interface**: Users can visualize their readings with accompanying images of the drawn tarot cards, enhancing the immersive experience.

- **Database Integration**: All questions, responses, and card spreads are stored in a MySQL database (`tarot_responses`) for potential reuse and analysis.

**Requirements**

- **Python 3.x**
- **Flask**: Web framework for building the application.
- **Pillow (PIL Fork)**: Python Imaging Library for image processing.
- **PyMySQL (or a compatible MySQL connector)**: Database connector for MySQL.
- **Google Cloud account with GenerativeAI API enabled**: Required for accessing the generative AI model.
- **Credentials for database connection and Google Cloud**: Ensure secure storage in `credentials.py`.

**Setup**

1. **Install Dependencies**: Use `pip` to install the necessary Python packages:

   ```bash
   pip install Flask Pillow PyMySQL google-cloud-aiplatform
   ```

2. **Set Up Credentials**: Create a `credentials.py` file with your database and Google Cloud API credentials:

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

   Replace placeholder values with your actual credentials.

3. **Customize Tarot Deck**: Optionally, update the `tarot_cards` list in `app.py` with your preferred tarot cards.
   
## Getting Started

To run the application, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Debasish7ripathy/TarotCard.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API key:

   - Sign up for the Google Cloud Platform and create a new project.
   - Enable the "Cloud AI Platform" and "Cloud AI Platform Notebooks" APIs.
   - Create an API key and replace `your_api_key_here` in `app.py` with your actual API key.

4. Run the Flask application:

   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://localhost:5000` to access the Reader interface.
   

**Running the Application**

1. **Using `main.py`**: Alternatively, you can run the application using `main.py`. Execute the following command:

   ```bash
   python main.py
   ```

2. **Access the Application**: Open your web browser and navigate to `http://127.0.0.1:5000/` (or the specified port).

**Database Schema**

Ensure your MySQL database includes a table named `tarot_responses` with the following columns:

| Column Name  | Data Type | Description                            |
|--------------|-----------|----------------------------------------|
| question     | text      | User-entered question                  |
| date         | date      | Date of question (YYYY-MM-DD)          |
| response     | text      | Generated AI response                  |
| past_card    | text      | Past tarot card in the reading         |
| present_card | text      | Present tarot card in the reading      |
| future_card  | text      | Future tarot card in the reading       |

**Additional Notes**

- **Error Handling**: The application includes robust error handling to provide informative messages in case of issues.
  
- **Image Resizing**: Image resizing functionality is available for potential optimization, but it's commented out for flexibility. Uncomment relevant lines if desired.
  
- **Security Considerations**: For production environments, consider implementing additional security measures such as input validation and user authentication.

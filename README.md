# Basic Flask Page
A basic Flask web page with dynamic content and a button interaction. Built as part of learning Flask for Infosys Springboard.
## Features
- Displays a greeting message.
- Button click updates the message dynamically.
- Clean HTML/CSS template with responsive design.
- Simple Flask backend handling GET/POST requests.
## How It Works
app.py:
- Initializes a Flask app.
- Uses a global variable message to store the greeting.
- Handles POST requests when the button is clicked.
- Renders the index.html template with the updated message.
  ##
index.html:
- Uses Jinja2 templating to display {{ message }}.
- Includes CSS for styling and a form with a submit button.

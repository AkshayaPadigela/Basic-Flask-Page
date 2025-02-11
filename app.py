from flask import Flask, render_template, request

     # Create a Flask application
app = Flask(__name__)

     # Initial message
message = "Hello, Flask!"

     # Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
   global message
   if request.method == 'POST':
             # Change the message when the button is clicked
       message = "You clicked the button!"
   return render_template('index.html', message=message)

     # Run the application
if __name__ == '__main__':
   app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = request.args.get('message', "Hello, Flask!")  # Default message

    if request.method == 'POST':
        # Redirect with the updated message as a query parameter
        return render_template('index.html', message="You clicked the button!")

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

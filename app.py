from flask import Flask, render_template, request
from src import Gmaps

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_input = request.form['query']

    try:
        result = Gmaps.places([user_input], max=10)

        if result:
            return render_template('result.html', places=result)
        else:
            return render_template('result.html', message="No results found.")
    except Exception as e:
        return render_template('result.html', message=f"Error executing query: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

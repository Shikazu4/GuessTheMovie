from flask import Flask, render_template, request, jsonify
# import json

app = Flask(__name__)

# Load movie names from movies.json
# with open('movies.json', 'r') as f:
#     movies_data = json.load(f)
# movie_names = [movies_data]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_guess', methods=['POST'])
def check_guess():
    movie_name = request.form['guess'].upper()
    correct_name = 'HELLO'  # Set the correct movie name here

    response = {
        'correct': movie_name == correct_name,
        'next_image': '/static/imageuploads/' + '1' + '.jpg',
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

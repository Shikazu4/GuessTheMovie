from flask import Flask, render_template, request, jsonify
import os
import shutil
# import json

app = Flask(__name__)
UPLOAD_FOLDER = 'static/imageuploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Load movie names from movies.json
# with open('movies.json', 'r') as f:
#     movies_data = json.load(f)
# movie_names = [movies_data]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/custom.html')
def custom():
    return render_template('custom.html')

@app.route('/check_guess', methods=['POST'])
def check_guess():
    movie_name = request.form['guess'].upper()
    # correct_name = 'HELLO'  # Set the correct movie name here
    correct_name = request.form['query'].upper()
    print('Hello World')

    response = {
        'correct': movie_name == correct_name,
        'next_image': '/static/imageuploads/' + '1' + '.jpg',
    }

    return jsonify(response)

@app.route('/upload', methods=['POST'])
def upload():
    name = request.form['name']
    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        
    os.makedirs(folder_path)

    for i in range(1, 6):
        file = request.files['image{}'.format(i)]
        if file:
            filename = '{}.jpg'.format(i)
            file.save(os.path.join(folder_path, filename))

    url = request.host_url + os.path.join('uploads', name)
    return url


if __name__ == '__main__':
    app.run(debug=True)

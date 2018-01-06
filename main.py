from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form method="post" action="/encrypt">
            <div>
                <label for="rot">Rotation:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text"></textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/encrypt")
def encrypt():
    text = request.args.get('text')
    rot_str = request.args.get('rot')
    rot = int(rot_str)
    encrypted = rotate_string(text, rot)
    return '<h1>' + encrypted + '</h1>'

app.run()
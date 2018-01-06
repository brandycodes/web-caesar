from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form method="post" action="/encrypt">
            <label for="rot">Rotation:</label>
            <input type="text" name="rot" value="0" />
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/encrypt", methods=['POST'])
def encrypt():
    text = request.form.get('text')
    rot = int(request.form.get('rot'))
    encrypted = rotate_string(text, rot)
    return form.format(encrypted)

app.run()
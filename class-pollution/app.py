import json
from flask import Flask, render_template, request
import os

app = Flask(__name__)
debug_level = 2

class User():
    name = ""
    login = ""
    pass_hash = ""
    email = ""
    def __init__(self):
        pass

class Comment(User):
    comment = ""

class Error(User):
    error = ""

class Admin(User):
    is_admin = False

def merge(src_dict, dst_obj):    # Recursively copy dict input to an object
    for key, value in src_dict.items():
        if hasattr(dst_obj, '__getitem__'):
            if dst_obj.get(key) and type(value) == dict:
                merge(value, dst_obj.get(key))
            else:
                dst_obj[key] = value
        elif hasattr(dst_obj, key) and type(value) == dict:
            merge(value, getattr(dst_obj, key))
        else:
            setattr(dst_obj, key, value)

def get_code():
    with open('./app.py', 'r') as f:
        return f.read()

def get_vars():
    return str({"flag":os.getenv("FLAG")})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def run():
    global debug_level
    debug_level = 2

    error = Error()
    comment = Comment()
    try:
        input = request.form
        content_type = request.content_type
        if content_type != "application/x-www-form-urlencoded":
            input = request.json

        merge(input, comment)
        error = None    # all good no errors
    except Exception as e:
        error.error = e

    return_text = f"Thank you for your comment {comment.name}!"
    if error and debug_level > 1:     # debug is still on for bug fixing - to be removed (set to 0)
        return_text = get_code()
    elif debug_level > 2:
        return_text += "\n\n" + get_vars()

    return render_template("thankyou.html", value=return_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8081))
    app.run(debug=False,host='0.0.0.0',port=port)

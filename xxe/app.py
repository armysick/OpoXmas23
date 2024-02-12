import os

from lxml import etree
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", hasError=False, messages=[], submission=None)


@app.route("/submit", methods=["POST"])
def submit():
    if (
        not request.files.get("file") or
        not request.form.get("first-name") or
        not request.form.get("last-name")
        ):
        return render_template("index.html",
                    hasError=False,
                    messages=["endpoint requires a file, first name and last name to be filed in"],
                    submission=None
                ), 400

    fName = request.form.get("first-name")
    lName = request.form.get("last-name")
    file = request.files["file"]

    destination_file = f'/tmp/{file.filename}'
    file.save(destination_file)

    experiences = []
    with open(destination_file, mode='r') as f:
        parser = etree.XMLParser(load_dtd=True, no_network=False)
        tree = etree.parse(f, parser=parser)
        experiences = tree.getroot().findall("experience")

    os.remove(destination_file)
    return render_template("index.html",
                hasError=False,
                messages=[f"Thank you for your submission {fName} {lName}. Here are your experiences: "],
                submission=[experience.text for experience in experiences]
    ), 200



if __name__=="__main__":
    app.run(debug=False)

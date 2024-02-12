from flask import Flask, jsonify, render_template, request, redirect, make_response
from werkzeug.middleware.proxy_fix import ProxyFix

import uuid
import os
import random
import base64

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

MT_GUID = '00000000-0000-0000-0000-000000000000'

kudos_dict = {}

# Lists of common first names and last names
first_names = ["John", "Jane", "Michael", "Emily", "William", "Olivia", "James", "Sophia", "David", "Emma"]
last_names = ["Smith", "Johnson", "Brown", "Lee", "Williams", "Davis", "Wilson", "Taylor", "Miller", "Jones"]


def generate_random_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    guid = MT_GUID
    while guid == MT_GUID:
      guid = uuid.uuid4()

    guid = "{"+str(guid)+"}"
    guid = base64.b64encode(guid.encode()).decode()

    return f"{first_name} {last_name}", guid


@app.route('/')
def employee():
    name, guid = generate_random_name()
    data = {"guid": guid, "name": name}
    return render_template('employee.html', data=data)


@app.route('/api/employee/details/<string:guid>', methods=['GET'])
def get_details(guid):
    if base64.b64decode(guid).decode() == "{"+MT_GUID+"}":
        return jsonify({"details": f"{os.getenv('FLAG_GUID')}"})
    else:
        return jsonify({"details": "This user does not have what you are looking for"})



@app.route('/get_data/', methods=['GET'])
def get_data():
    return render_template('employee_details.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

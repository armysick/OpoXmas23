from flask import Flask, jsonify, render_template, request, redirect, make_response
from werkzeug.middleware.proxy_fix import ProxyFix
import uuid
import os
import random

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

kudos_dict = {}


@app.route('/kudos/002a9ee8d4fd/', methods=['GET'])
def approve_all_kudos():
    resp = make_response(render_template('kudos_admin.html', data={k: v for k, v in kudos_dict.items() if not v["approved"]}))
    resp.set_cookie('flag', f"{os.getenv('FLAG_XSS')}")

    for kudo in kudos_dict.keys():
        kudos_dict[kudo]["approval_message"] = "Manager approved!"
        kudos_dict[kudo]["approved"] = True

    return resp


@app.route('/kudos/')
def kudos():
    kudos_points = [600, 1200, 3000]
    return render_template('kudos.html', kudos_points=kudos_points)


@app.route('/kudos_status/<string:uuid>', methods=['GET'])
def kudos_status(uuid):
    if not kudos_dict.get(uuid, False):
        resp = make_response(render_template('kudos_status.html', data={"message": "Kudos not found"}))
        resp.set_cookie('flag', 'not the flag')
        return resp

    kudos_message = ""
    if not kudos_dict[uuid].get("approved", False):
        kudos_dict[uuid]["approval_message"] = "Thanks for submitting kudos! Awaiting manager approval..."


    resp = make_response(render_template('kudos_status.html', data=kudos_dict[uuid]))
    resp.set_cookie('flag', 'not the flag')

    return resp


@app.route('/give_kudos/', methods=['POST'])
def give_kudos():
    receiver = request.form['receiver']
    points = int(request.form['points'])
    message = request.form['message']

    kudos = {
        'receiver': receiver,
        'points': points,
        'message': message,
        'approved': False,
        'approval_message': ""
    }

    id = str(uuid.uuid4())
    kudos_dict[id] = kudos

    return redirect(f'/kudos_status/{id}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

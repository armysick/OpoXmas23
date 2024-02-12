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
    if kudos_dict[uuid].get("approved", False):
        if kudos_dict[uuid].get("receiver", "").lower() in ("simpson","simps0n"):
            points = kudos_dict[uuid].get("points", 0)
            if 3000 < points <= 999999:
                kudos_message = "But SiMpS0N is not yet impressed with the amount of kudos points!"
            elif points > 999999:
                kudos_message = f"{os.getenv('FLAG_KUDOS')}"
            else:
                kudos_message = "But SiMpS0N is not impressed with your kudos points!"
        else:
            kudos_message = "But SiMpS0N wants Kudos!"

    kudos_dict[uuid]["approval_message"] = kudos_message

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
        'approved': True,
        'approval_message': ""
    }

    id = str(uuid.uuid4())
    kudos_dict[id] = kudos

    return redirect(f'/kudos_status/{id}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

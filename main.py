from flask import Flask, jsonify, url_for, redirect
from time import gmtime, strftime
import socket

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='images/favicon.ico'))

@app.route("/service/<service_number>")
def index(service_number):
    return jsonify({
        "success": True,
        "time": strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname())
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False, threaded=True)
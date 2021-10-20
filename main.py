from flask import Flask, jsonify, url_for, redirect
from time import gmtime, strftime

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='images/favicon.ico'))

@app.route("/")
def index():
    return jsonify({
        "success": True,
        "message": "hello world",
        "time": strftime("%Y-%m-%d %H:%M:%S", gmtime())
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False, threaded=True)
import flask
import requests
import base64

app = flask.Flask(__name__)


@app.route("/json/<url>")
def json_req(url):
    resp= flask.jsonify(requests.get(
        base64.b64decode(url.encode("utf-8")).decode("utf-8")
    ).json())
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

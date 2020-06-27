import flask
app = flask.Flask(__name__)
app.config["Debug"] = True


@app.route("/", methods=['GET'])
def home():
    return "<h1>123</h1>"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8999))
    app.run(host='0.0.0.0', port=port)

import flask
app = flask.Flask(__name__)
app.config["Debug"] = True

@app.route("/", methods=['GET'])
def home():
    return "<h1>123</h1>"

app.run()
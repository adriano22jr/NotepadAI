import flask

app = flask.Flask(__name__, template_folder = "templateFiles", static_folder = "staticFiles")

@app.route("/", methods = ["GET", "POST"])
def index():
    return flask.render_template("index.html", logged = True, profile_name = "adriano22_")

@app.route("/notebook-regular", methods = ["GET", "POST"])
def notebook_regular():
    return flask.render_template("notebook_regular.html")

@app.route("/notebook-markdown", methods = ["GET", "POST"])
def notebook_markdown():
    return flask.render_template("notebook_markdown.html")

if __name__ == "__main__":
    app.run(port = 8080, debug=True)
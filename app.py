from flask import Flask, render_template, request, redirect, url_for
from transformers import pipeline

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
	
@app.route("/login", methods = ["POST", "GET"])
def login():
	if request.method == "POST":
		text = request.form["paragraph_text"]
		return redirect(url_for("answer", txt = text))
	else:
		return render_template("index.html")
		
@app.route("/<txt>")
def answer(txt):
	classifier = pipeline("ner", model=r'C:\Users\ett\projects\demo-app\py39venv\Scripts\NLP_Model\my_nlp_model')
	text_answer = classifier(txt)
	lists = {}
	for element in text_answer:
		wd = element["word"]
		typ = element["entity"]
		key = typ
		if key in lists:
			lists[key] += [wd]
		else:
			lists[key] = [wd]
	return f"<h1>{lists}</h1>"
	
@app.route("/taskpane")
def taskpane():
    return render_template("taskpane.html")

@app.route("/commands")
def commands():
    return render_template("commands.html")

@app.route("/assets/icon-16.png")
def icon16():
    return send_file("./static/assets/icon-16.png",mimetype='image/png')

@app.route("/assets/icon-32.png")
def icon32():
    return send_file("./static/assets/icon-32.png",mimetype='image/png')

@app.route("/assets/icon-64.png")
def icon64():
    return send_file("./static/assets/icon-64.png",mimetype='image/png')

@app.route("/assets/icon-80.png")
def icon128():
    return send_file("./static/assets/icon-80.png",mimetype='image/png')

@app.route("/assets/logo-filled.png")
def iconlogofilled():
    return send_file("./static/assets/logo-filled.png",mimetype='image/png')
	
if __name__ == "__main__":
    app.run(debug=True)
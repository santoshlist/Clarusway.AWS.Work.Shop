from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def head():
    return render_template("index.html", number1 = 12, number2 = 34)

@app.route("/ikinci")
def second():
    return render_template("yeni.html", hazirlayan = "Mustafa")
if __name__ == "__main__":
    app.run(debug = True)
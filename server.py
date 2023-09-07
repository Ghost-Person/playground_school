from flask import Flask, render_template


app = Flask(__name__)

@app.route('/play')
def three_blue():
    return render_template("index.html", num = 3, color = "cyan")

@app.route('/play/<int:num>')
def many_blue(num):
    return render_template("index.html", num = num, color = "cyan")

@app.route('/play/<int:num>/<string:color>')
def whatev(num, color):
    return render_template("index.html", num = num, color = color)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)

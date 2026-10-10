from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/model/<path:arquivo>")
def arquivos_modelo(arquivo):
    return send_from_directory("model", arquivo)

if __name__ == "__main__":
    app.run(debug=True)
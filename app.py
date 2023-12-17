from flask import Flask, request, render_template
import subprocess
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_script", methods=["POST"])
def run_script():
    query = request.form.get("query")
    data_file = request.files.get("dataFile")

    if not query or not data_file:
        return "Please enter a query and select a data file."

    data_file.save("data.txt")

    try:
        result = subprocess.check_output([r"C:\Users\Subhang Ladha\AppData\Local\Programs\Python\Python310\python.exe", "chatgpt.py", query], text=True, cwd=os.getcwd())
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)

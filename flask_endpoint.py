from flask import Flask, request, send_file
import googleai
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/csv_generator",methods=["POST"])
def csv_generator():
    file_location=googleai.generate_csv(request.get_json()["user_input"])
    print(file_location)
    return file_location
@app.route("/csv_provider",methods=["GET"])
def csv_provider():
    file_name=request.args.get("file_name")
    return send_file(os.getcwd()+"/"+file_name,as_attachment=True)
if __name__ == "__main__":
    app.run(port=8000)


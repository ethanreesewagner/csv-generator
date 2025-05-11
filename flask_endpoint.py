from flask import Flask, request
import csv_flask_logic
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/csv_generator",methods=["POST"])
def csv_generator():
    file_location=csv_flask_logic.generate_csv(request.get_json()["user_input"])
    print(file_location)
    return file_location
if __name__ == "__main__":
    app.run(port=8000)


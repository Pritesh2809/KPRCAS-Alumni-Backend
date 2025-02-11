from flask import Flask, jsonify
from flask_cors import CORS
import google_sheets

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route("/alumni", methods=["GET"])
def alumni_list():
    try:
        data = google_sheets.get_alumni_data()
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

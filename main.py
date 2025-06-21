from flask import Flask, jsonify, request
from src.axcelerate_client import AxcelerateClient, AxcelerateConfig
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Initialize Axcelerate client with environment variables
config = AxcelerateConfig(
    web_service_token=os.getenv('AXCELERATE_WEB_SERVICE_TOKEN'),
    api_token=os.getenv('AXCELERATE_API_TOKEN')
)
axcelerate_client = AxcelerateClient(config)


@app.route("/")
def root():
    return jsonify({
        "Message": "Axcelerate API webhook service running"
    })


@app.route("/axcelerate/student", methods=["POST"])
def student_lookup():
    """Endpoint to search for a student in Axcelerate."""
    data = request.get_json()
    search_term = data.get("search_term")
    
    if not search_term:
        return jsonify({"error": "search_term is required"}), 400
    
    try:
        students = axcelerate_client.search_contacts(search_term)
        return jsonify({"students": students})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/axcelerate/assessment", methods=["POST"])
def update_assessment():
    """Endpoint to update a student's assessment."""
    data = request.get_json()
    
    required_fields = ["enrolment_id", "outcome_code", "status"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Missing required fields: {required_fields}"}), 400
    
    try:
        result = axcelerate_client.update_assessment(
            enrolment_id=data["enrolment_id"],
            outcome_code=data["outcome_code"],
            status=data["status"],
            comments=data.get("comments")
        )
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/axcelerate/enrolments/<int:contact_id>", methods=["GET"])
def get_enrolments(contact_id: int):
    """Endpoint to get all enrolments for a student."""
    try:
        enrolments = axcelerate_client.get_course_enrolments(contact_id)
        return jsonify({"enrolments": enrolments})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
from flask import Flask, request, jsonify
from utils import extract_skills, score_resume

app = Flask(__name__)

@app.route("/")
def home():
    return "Resume Analyzer Running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    resume_text = data.get("text", "")

    skills = extract_skills(resume_text)
    score = score_resume(resume_text)

    return jsonify({
        "skills": skills,
        "score": score
    })

if __name__ == "__main__":
    app.run(debug=True)

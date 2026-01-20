from flask import Flask, render_template, request
from resume_parser import extract_text_from_pdf
from skills import extract_skills, SKILLS
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume = request.files["resume"]
        job_desc = request.form["job_desc"].lower()

        resume.save("temp.pdf")
        resume_text = extract_text_from_pdf("temp.pdf")

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_desc)

        matched = set(resume_skills).intersection(set(job_skills))
        missing = set(job_skills) - set(resume_skills)

        score = int((len(matched) / len(job_skills)) * 100) if job_skills else 0

        return render_template(
            "result.html",
            matched=matched,
            missing=missing,
            score=score
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

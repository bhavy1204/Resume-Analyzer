SKILLS = [
    "python", "java", "javascript", "react", "node",
    "sql", "mongodb", "html", "css", "git",
    "machine learning", "data analysis"
]
def extract_skills(text):
    found_skills = []
    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)
    return found_skills

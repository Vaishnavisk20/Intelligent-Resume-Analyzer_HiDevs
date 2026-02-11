import re
from pypdf import PdfReader
from src.models import Candidate, Job


def extract_text_from_pdf(file) -> str:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def parse_resume(text: str) -> Candidate:
    name_match = re.search(r"([A-Z][A-Z\s]+)", text)
    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)

    experience_match = re.findall(r"(\d+)\s*(?:years|year)", text, re.I)

    skills_keywords = [
        "Python", "SQL", "Machine Learning", "Data Science", "FastAPI",
        "Flask", "NLP", "OCR", "LangChain", "Docker", "Git",
        "Streamlit", "PostgreSQL", "MySQL", "Pandas", "NumPy"
    ]

    skills_found = [skill for skill in skills_keywords if skill.lower() in text.lower()]

    education_match = re.search(
        r"B\.?Tech|Bachelor|Master|CSE|Computer Science", text, re.I
    )

    return Candidate(
        name=name_match.group(1).strip() if name_match else "Unknown",
        email=email_match.group(0) if email_match else "Not Found",
        skills=skills_found,
        experience=max(map(int, experience_match)) if experience_match else 0,
        education=education_match.group(0) if education_match else "Not Mentioned"
    )


def parse_job_description(text: str) -> Job:
    title_match = re.search(r"Job Title[:\-]?\s*(.*)", text, re.I)
    experience_match = re.search(r"(\d+)\s*(?:years|year)", text, re.I)

    skills_match = re.search(r"Skills[:\-]?\s*(.*)", text, re.I)
    skills = [s.strip() for s in skills_match.group(1).split(",")] if skills_match else []

    education_match = re.search(r"Education[:\-]?\s*(.*)", text, re.I)

    return Job(
        title=title_match.group(1) if title_match else "Unknown Role",
        required_skills=skills,
        min_experience=int(experience_match.group(1)) if experience_match else 0,
        education=education_match.group(1) if education_match else "Any"
    )
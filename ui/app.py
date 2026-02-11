import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.parser import extract_text_from_pdf, parse_resume, parse_job_description
from src.matcher import match_candidate

st.set_page_config(page_title="Intelligent Resume Analyzer", layout="wide")
st.title("📄 Intelligent Resume Analyzer")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_text = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if resume_file and job_text:
        resume_text = extract_text_from_pdf(resume_file)

        candidate = parse_resume(resume_text)
        job = parse_job_description(job_text)

        result = match_candidate(candidate, job)

        st.subheader("👤 Candidate Profile")
        st.json(candidate.__dict__)

        st.subheader("📊 Match Result")
        st.metric("Match Score", f"{result['score']} / 100")

        st.write("✅ Matched Skills:", result["matched_skills"])
        st.write("❌ Missing Skills:", result["missing_skills"])

        st.subheader("📌 Recommendation")
        st.success(result["recommendation"])
    else:
        st.warning("Upload resume PDF and paste job description.")
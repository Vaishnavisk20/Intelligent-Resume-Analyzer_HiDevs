Intelligent Resume Analyzer

Project Overview

The "Intelligent Resume Analyzer" is a Python-based application that automates resume screening.
It parses PDF resumes, extracts candidate details, matches them against job requirements, and generates a hiring recommendation with a match score.

This project demonstrates real-world use of "Python, text processing, file handling, and basic AI logic" used in HR technology.

Features:
* Upload and analyze PDF resumes
* Extracts:
  * Name
  * Email
  * Skills
  * Experience
  * Education
* Matches candidate profile with job description
* Calculates match score (0–100)
* Displays hiring recommendation
* Simple and interactive Streamlit UI


Technologies Used:
* Python
* Streamlit – User Interface
* PyPDF– PDF text extraction
* Regex – Data parsing
* Dataclasses – Structured data models



Project Structure:
Intelligent-Resume-Analyzer/
│
├── src/
│   ├── models.py
│   ├── parser.py
│   ├── matcher.py
│
├── ui/
│   └── app.py
│
├── requirements.txt
└── README.md


How to Run the Project:

1.Install Dependencies
pip install -r requirements.txt
2.Run the Application
streamlit run ui/app.py

How It Works:
1. Upload a "PDF resume"
2. Paste the "job description"
3. Click "Analyze Resume"
4. View:

   * Candidate profile
   * Match score
   * Matched & missing skills
   * Final recommendation


Match Scoring Logic:

* Skill match: +10 per matched skill
* Experience match: +30
* Education match: +20
* Maximum score: "100"



Use Cases:

* Resume screening automation
* HR technology solutions
* Academic AI/ML projects
* Python portfolio project



Outcome:
A complete **Intelligent Resume Analysis System** that:
* Automates candidate screening
* Improves hiring efficiency
* Demonstrates industry-level Python application design


Future Enhancements:
* AI-based skill extraction
* Multiple resume ranking
* Resume report export (PDF/Excel)
* Fuzzy skill matching
* Interview question generation


Project Demo Video

Watch the demo of the Intelligent Resume Analyzer here:  
👉 https://youtu.be/qO1nHYCwA4M?si=tIuLLJx_rYlQHsmS

The demo shows:
- Uploading a PDF resume
- Entering a job description
- Resume parsing and skill extraction
- Match score calculation
- Final hiring recommendation





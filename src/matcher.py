from src.models import Candidate, Job


def match_candidate(candidate: Candidate, job: Job) -> dict:
    matched_skills = set(candidate.skills) & set(job.required_skills)
    missing_skills = set(job.required_skills) - set(candidate.skills)

    score = len(matched_skills) * 10

    if candidate.experience >= job.min_experience:
        score += 30

    if candidate.education.lower() in job.education.lower():
        score += 20

    score = min(score, 100)

    recommendation = (
        "STRONGLY RECOMMENDED" if score >= 80 else
        "RECOMMENDED" if score >= 60 else
        "MAYBE" if score >= 40 else
        "NOT RECOMMENDED"
    )

    return {
        "score": score,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "recommendation": recommendation
    }
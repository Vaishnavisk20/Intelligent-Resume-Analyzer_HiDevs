def explain(candidate, job, result):
    explanation = f"""
Candidate Evaluation Summary:

Candidate Name: {candidate.name}
Applied Role: {job.title}

Matched Skills: {', '.join(result['matched_skills'])}
Experience: {candidate.experience} years (Required: {job.min_experience})
Education Match: {candidate.education == job.education}

Final Score: {result['score']}
Decision: {result['decision']}

Reasoning:
The candidate was evaluated based on skill matching, experience level,
and educational qualification. The final recommendation is derived
from a weighted scoring mechanism.
"""
    return explanation
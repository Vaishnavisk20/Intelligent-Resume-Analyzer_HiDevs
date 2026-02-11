from dataclasses import dataclass
from typing import List

@dataclass
class Candidate:
    name: str
    email: str
    skills: List[str]
    experience: int
    education: str


@dataclass
class Job:
    title: str
    required_skills: List[str]
    min_experience: int
    education: str
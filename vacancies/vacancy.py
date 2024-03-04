from dataclasses import dataclass


@dataclass
class Vacancy:
    position: str
    url: str
    salary_from: int
    salary_to: int
    description: str
    must_know: str

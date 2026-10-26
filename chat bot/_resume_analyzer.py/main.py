
# Task 8: Resume Analyzer
# Local keyword-based demo — no API requests required.

SKILLS = [
    "python", "java", "sql", "machine learning", "deep learning",
    "data analysis", "excel", "power bi", "tableau", "communication",
    "teamwork", "project management", "html", "css", "javascript",
    "react", "fastapi", "git", "cloud", "statistics"
]

def analyze_resume(resume):
    text = resume.lower()

    found_skills = [skill for skill in SKILLS if skill in text]
    missing_skills = [skill for skill in SKILLS if skill not in text]

    experience_terms = [
        "internship", "intern", "years of experience",
        "professional experience", "worked at", "employment"
    ]
    experience_matches = [
        term for term in experience_terms if term in text
    ]

    print("\n" + "=" * 45)
    print("RESUME ANALYSIS")
    print("=" * 45)

    print("\nSkills detected:")
    print(", ".join(found_skills) if found_skills else "No listed skills detected.")

    print("\nPotential strengths:")
    if found_skills:
        print("- Your resume mentions", len(found_skills), "skills.")
        print("- Consider adding project examples that demonstrate these skills.")
    else:
        print("- Add a clear skills section with relevant technical and soft skills.")

    print("\nExperience-related keywords:")
    print(", ".join(experience_matches) if experience_matches else
          "No common experience keywords detected. Add relevant experience if applicable.")

    print("\nSkills to consider (not necessarily missing qualifications):")
    print(", ".join(missing_skills[:8]) if missing_skills else
          "All skills in this demo list were detected.")

    print("\nSuggestions:")
    print("1. Tailor your resume to the specific job description.")
    print("2. Describe projects with actions, tools, and measurable results.")
    print("3. Include education, relevant experience, and certifications.")
    print("4. Only list skills and experience you genuinely have.")
    print("\nNote: This demo uses keyword matching, not an AI model.")

print("=" * 45)
print("RESUME ANALYZER")
print("Paste your resume as one line, or type 'exit' to quit.")
print("=" * 45)

while True:
    resume = input("\nResume: ").strip()

    if resume.lower() == "exit":
        print("Goodbye!")
        break

    if not resume:
        print("Please enter resume text.")
        continue

    analyze_resume(resume)

 def get_career_info(career):
    info = {
        "Data Scientist": {
            "skills": ["Python", "ML", "SQL", "Math"],
            "description": "Works with data to extract insights and build predictive models."
        },
        "AI Engineer": {
            "skills": ["Python", "ML", "Deep Learning"],
            "description": "Builds AI systems and intelligent applications."
        },
        "Frontend Developer": {
            "skills": ["HTML", "CSS", "JavaScript"],
            "description": "Designs and builds user interfaces."
        },
        "Backend Developer": {
            "skills": ["Python", "Java", "DSA"],
            "description": "Handles server-side logic and APIs."
        },
        "Full Stack Developer": {
            "skills": ["Frontend", "Backend", "Database"],
            "description": "Works on both frontend and backend."
        },
        "Cloud Engineer": {
            "skills": ["Cloud", "Linux", "Networking"],
            "description": "Manages cloud infrastructure and deployment systems."
        },
        "DevOps Engineer": {
            "skills": ["Linux", "Git", "Cloud"],
            "description": "Automates deployment and manages CI/CD pipelines."
        },
        "Cybersecurity Analyst": {
            "skills": ["Networking", "Linux", "Security"],
            "description": "Protects systems and networks from cyber threats."
        },
        "Software Tester": {
            "skills": ["Testing", "Debugging", "Attention to Detail"],
            "description": "Ensures software quality by identifying bugs and issues."
        },
        "Product Manager": {
            "skills": ["Communication", "Leadership", "Management"],
            "description": "Leads product development and coordinates between teams."
        }
    }

    return info.get(career, {
        "skills": [],
        "description": "No information available for this career."
    })

def skill_gap(user_input, required_skills):
    gap = []

    if required_skills:
        if "Python" in required_skills and user_input["Python"] == 0:
            gap.append("Python")
        if "ML" in required_skills and user_input["ML"] == 0:
            gap.append("Machine Learning")
        if "SQL" in required_skills and user_input["SQL"] == 0:
            gap.append("SQL")

    return gap

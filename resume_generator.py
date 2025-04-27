def generate_resume(name, email, phone, education, experience, skills, jobrole):
    resume = f"""
{name}
{email} | {phone}

Objective:
To secure a position as a {jobrole} where I can apply my skills and grow professionally.

Education:
{education}

Experience:
{experience}

Skills:
{skills}
    """
    return resume.strip()

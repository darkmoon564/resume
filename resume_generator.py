def generate_resume(name, email, phone, education, experience, skills, jobrole):
    resume = f"""
{name.upper()}
Email: {email} | Phone: {phone}

PROFESSIONAL SUMMARY
Results-driven and highly motivated aspiring {jobrole} with a strong academic background in {education}. Demonstrated experience in {experience.split('.')[0]} and equipped with a versatile skill set including {skills.split(',')[0]}. Eager to contribute to real-world projects and grow in a collaborative, fast-paced environment.

EDUCATION
{education}

WORK EXPERIENCE
{experience}

TECHNICAL SKILLS
{', '.join(skill.strip().capitalize() for skill in skills.split(','))}

PROJECTS
• Available on GitHub: https://github.com/darkmoon564

CERTIFICATIONS
• Add relevant certifications here (if any)

ADDITIONAL DETAILS
• Open to relocation and remote roles
• Passionate about continuous learning and innovation in {jobrole}

References available upon request.
"""
    return resume.strip()

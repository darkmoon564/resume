def generate_cover_letter(name , email , phone,education , experience , skills , jobrole , company_name):
    cover_letter= f"""
dear hiring manager at {company_name} ,
I am excited to apply for the {jobrole} position at your esteemed organization. With my background in {education} and hands-on experience in {experience}, I am confident in my ability to contribute effectively to your team.

My skills include {skills}, which I believe align well with the requirements of this role. I am passionate about bringing my expertise and enthusiasm to {company_name}.

Thank you for considering my application. I look forward to the opportunity to discuss how I can contribute to your team.

Sincerely,
{name}
{email}|{phone}
"""
    return cover_letter.strip()
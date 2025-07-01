import streamlit as st
from resume_generator import generate_resume
from cover_letter import generate_cover_letter

st.set_page_config(page_title="AI Resume & Cover Letter Generator", page_icon="📝")

st.title(" AI Resume and Cover Letter Generator")

st.subheader("Enter your information:")

with st.form("user_info_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    education = st.text_area("Education Background")
    experience = st.text_area("Work Experience")
    skills = st.text_area("Skills (comma separated)")
    job_role = st.text_input("Target Job Role")
    company_name = st.text_input("Target Company (for Cover Letter)")

    submitted = st.form_submit_button("Generate")

if submitted:
    st.success("Generating... Please wait!")

    resume_text = generate_resume(name, email, phone, education, experience, skills, job_role)
    cover_letter_text = generate_cover_letter(name, email, phone, education, experience, skills, job_role, company_name)

    st.subheader(" Resume:")
    st.text_area("Resume", resume_text, height=300)

    st.subheader(" Cover Letter:")
    st.text_area("Cover Letter", cover_letter_text, height=300)

    # Download buttons
  # Encode text to bytes (UTF-8)
    resume_bytes = resume_text.encode('utf-8')
    cover_letter_bytes = cover_letter_text.encode('utf-8')

    st.download_button("📄 Download Resume", resume_bytes, file_name="resume.txt", mime="text/plain")
    st.download_button("📄 Download Cover Letter", cover_letter_bytes, file_name="cover_letter.txt", mime="text/plain")


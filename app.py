
import streamlit as st

st.set_page_config(page_title="Resume Generator", layout="centered")
st.title("📝 Resume Generator")

st.subheader("Enter your details below:")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn Profile URL")
website = st.text_input("Portfolio Website")

st.subheader("Education")
university = st.text_input("University Name")
university_city = st.text_input("University City")
university_state = st.text_input("University State")
grad_year = st.text_input("Graduation Year")

st.subheader("Experience")
company = st.text_input("Company Name")
company_city = st.text_input("Company City")
company_state = st.text_input("Company State")
job_duration = st.text_input("Job Duration")

project_name = st.text_input("Project Name")
project_desc = st.text_area("Project Description")
project_achieve = st.text_area("Project Achievement")

st.subheader("Skills and Certifications")
skills = st.text_area("Skills (comma-separated)")
certifications = st.text_area("Certifications (comma-separated)")

if st.button("Generate Resume"):
    st.success("✅ Resume Generated Below")
    with st.expander("📄 View Resume"):
        st.markdown(f"### {name}")
        st.markdown(f"📧 {email} | 📞 {phone} | [LinkedIn]({linkedin}) | [Portfolio]({website})")

        st.markdown("#### 🎓 Education")
        st.markdown(f"**{university}**, {university_city}, {university_state} — {grad_year}")
        st.markdown("*B.Tech in Computer Science and Engineering*")

        st.markdown("#### 💼 Work Experience")
        st.markdown(f"**Software Developer — {company}**")
        st.markdown(f"{company_city}, {company_state} | {job_duration}")
        st.markdown(f"- Worked on **{project_name}** with full-stack tools.")
        st.markdown(f"- {project_desc}")
        st.markdown(f"- {project_achieve}")
        st.markdown(f"- Used Agile methodology and collaborative tools.")

        st.markdown("#### 🛠️ Skills")
        st.markdown(skills)

        st.markdown("#### 🏆 Certifications")
        for cert in certifications.split(','):
            st.markdown(f"- {cert.strip()}")

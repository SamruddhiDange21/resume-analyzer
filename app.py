import streamlit as st
from skills import skills_db

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("Resume Analyzer")
st.markdown("Analyze your resume and identify missing skills.")
st.markdown("---")

# Select role
role = st.selectbox("Select Target Role", ["Data Science", "Web Development"])

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (.txt)", type=["txt"])

if uploaded_file is not None:
    resume_text = uploaded_file.read().decode("utf-8").lower()

    st.subheader("Resume Preview")
    st.text_area("Resume Content", resume_text, height=250)

    # Get skills for selected role
    selected_skills = skills_db[role]

    # Analyze skills
    found = []
    for skill in selected_skills:
        if any(word in resume_text for word in skill.split()):
            found.append(skill)

    missing = [skill for skill in selected_skills if skill not in found]

    # Display results in columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Skills Found")
        st.write(", ".join(found) if found else "None")

    with col2:
        st.subheader("Missing Skills")
        st.write(", ".join(missing) if missing else "None")

    # Score
    score = int((len(found) / len(selected_skills)) * 100)

    st.subheader("Match Score")
    st.progress(score)
    st.metric("Score", f"{score}%")

else:
    st.info("Upload a resume file to begin analysis.")

st.markdown("---")
st.caption("Built using Streamlit | Resume Analyzer Project")
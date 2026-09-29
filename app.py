import streamlit as st
import os

st.set_page_config(
    page_title="AI Placement Readiness Assistant",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Placement Readiness Assistant")
st.write("Check your placement readiness and practice interview questions.")

st.sidebar.header("Your Profile")

name = st.sidebar.text_input("Name")
role = st.sidebar.selectbox(
    "Target Role",
    ["Software Developer", "Data Analyst", "AI/ML Engineer", "Web Developer"]
)

skills = st.sidebar.text_area(
    "Your Skills",
    placeholder="Python, SQL, Git, HTML, Machine Learning..."
)

st.header("📊 Placement Readiness")

if skills:
    skill_list = [s.strip() for s in skills.split(",") if s.strip()]
    score = min(len(skill_list) * 15, 100)

    st.progress(score / 100)
    st.metric("Readiness Score", f"{score}%")

    if score >= 70:
        st.success("Good progress! Keep practicing interviews.")
    elif score >= 40:
        st.warning("You are making progress. Strengthen your technical skills.")
    else:
        st.info("Start with core programming and problem-solving skills.")
else:
    st.info("Enter your skills in the sidebar to calculate your readiness.")

st.divider()

st.header("💬 Interview Practice")

question = st.text_input(
    "Ask an interview question or choose a topic",
    placeholder="Example: Explain OOP in Python"
)

if st.button("Generate Practice Answer"):
    if question:
        st.subheader("Practice Guidance")

        st.write(
            "Prepare your answer using this structure:"
        )

        st.markdown("""
        **1. Definition**  
        Explain the concept in simple words.

        **2. Example**  
        Give a practical example.

        **3. Technical Details**  
        Mention important concepts, advantages, or limitations.

        **4. Interview Tip**  
        Keep your answer clear and concise.
        """)
    else:
        st.warning("Please enter a question first.")

st.divider()

st.header("🚀 Next Steps")

st.markdown("""
- Improve your technical skills
- Practice coding problems
- Prepare project explanations
- Practice HR interview questions
- Review your resume
- Take mock interviews
""")

st.caption("AI Placement Readiness Assistant — Student Project")
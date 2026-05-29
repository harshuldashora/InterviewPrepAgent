import streamlit as st

from agents.resume_parser import extract_resume_text
from agents.jd_analyzer import analyze_jd
from agents.question_generator import (
    generate_questions,
    generate_resume_questions
)
from agents.study_planner import create_study_plan
from agents.skill_gap import skill_gap_analysis

st.title("AI Interview Preparation Agent")

resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze"):

    if resume_file and job_description:

        with st.spinner("Analyzing..."):

            # Extract resume text
            resume_text = extract_resume_text(
                resume_file
            )

            # Analyze Job Description
            jd_analysis = analyze_jd(
                job_description
            )

            # Generate interview questions
            questions = generate_questions(
                jd_analysis
            )

            # Generate resume/project-based questions
            resume_questions = (
                generate_resume_questions(
                    resume_text
                )
            )

            # Generate study plan
            study_plan = create_study_plan(
                jd_analysis
            )

            # Skill Gap Analysis
            gap_report = skill_gap_analysis(
                resume_text,
                job_description
            )

        # Display Results

        st.header("JD Analysis")
        st.write(jd_analysis)

        st.header("Skill Gap Analysis")
        st.write(gap_report)

        st.header("Interview Questions")
        st.write(questions)

        st.header("Project Questions")
        st.write(resume_questions)

        st.header("Study Plan")
        st.write(study_plan)

    else:

        st.warning(
            "Please upload a resume and paste a job description."
        )
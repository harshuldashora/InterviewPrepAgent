from utils.llm import ask_llm

def skill_gap_analysis(resume_text, job_description):

    prompt = f"""
    Compare the following Resume and Job Description.

    Identify:

    1. Matching Skills
    2. Missing Skills
    3. Areas for Improvement
    4. Recommended Topics to Learn

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

    return ask_llm(prompt)
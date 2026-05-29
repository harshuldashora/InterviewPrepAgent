from utils.llm import ask_llm

def generate_questions(skills):

    prompt = f"""
    Based on these skills:

    {skills}

    Generate:

    10 Technical Questions

    10 Behavioral Questions

    5 Coding Questions

    Format clearly.
    """

    return ask_llm(prompt)
def generate_resume_questions(resume_text):

    prompt = f"""
    Analyze this resume.

    Identify projects.

    Generate project-specific interview questions.

    Resume:

    {resume_text}
    """

    return ask_llm(prompt)
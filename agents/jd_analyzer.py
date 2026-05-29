from utils.llm import ask_llm

def analyze_jd(job_description):

    prompt = f"""
    Analyze the following Job Description.

    Extract:

    1. Required Skills
    2. Preferred Skills
    3. Experience Level
    4. Main Responsibilities

    Job Description:

    {job_description}
    """

    return ask_llm(prompt)
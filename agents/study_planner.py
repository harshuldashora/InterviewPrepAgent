from utils.llm import ask_llm

def create_study_plan(skills):

    prompt = f"""
    Create a 7-day interview preparation roadmap.

    Skills:

    {skills}

    Include:

    Day-wise tasks
    Topics to revise
    Practice suggestions
    """

    return ask_llm(prompt)
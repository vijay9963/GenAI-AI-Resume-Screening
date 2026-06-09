from langchain_core.prompts import PromptTemplate

# -------------------------
# 1. EXTRACTION PROMPT
# -------------------------
extraction_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
You are an expert resume parser.

Extract ONLY information explicitly present in the resume.

Return JSON in this format:

{{
  "skills": [],
  "experience": [],
  "education": [],
  "projects": []
}}

Resume:
{text}
"""
)

# -------------------------
# 2. SCORING PROMPT
# -------------------------
scoring_prompt = PromptTemplate(
    input_variables=["resume", "jd"],
    template="""
You are an AI resume screener.

Compare Resume with Job Description and give a score from 0 to 100.

Return ONLY JSON in this format:

{{
  "score": 0,
  "matched_skills": [],
  "missing_skills": []
}}

Resume:
{resume}

Job Description:
{jd}
"""
)
from extraction_chain import extraction_chain
from scoring_chain import scoring_chain
import json
import re
import streamlit as st
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))


# -------------------------
# 🎯 APP TITLE
# -------------------------
st.title("📄 AI Resume Screening System 🤖")

st.markdown("### 🚀 Upload a resume to analyze skills, match score, and hiring potential")

# -------------------------
# JOB DESCRIPTION
# -------------------------
jd = Path("job_description.txt").read_text(encoding="utf-8")

# -------------------------
# UPLOAD RESUME
# -------------------------
uploaded_file = st.file_uploader("📤 Upload Resume (TXT format)", type=["txt"])

if uploaded_file:

    resume = uploaded_file.read().decode("utf-8")

    st.markdown("## 📄 Resume Preview")
    st.info(resume)

    # -------------------------
    # EXTRACTION
    # -------------------------
    st.markdown("## 🧠 Extracted Resume Insights")

    extracted = extraction_chain.invoke({"text": resume})
    st.success(extracted.content)

    # -------------------------
    # SCORING
    # -------------------------
    st.markdown("## 📊 AI Match Score Analysis")

    score_result = scoring_chain.invoke({
        "resume": resume,
        "jd": jd
    })

    st.write("🔍 Raw AI Output:")
    st.code(score_result.content)

    # -------------------------
    # SAFE JSON PARSE
    # -------------------------
    raw = score_result.content
    match = re.search(r"\{.*\}", raw, re.DOTALL)

    if match:
        data = json.loads(match.group())
    else:
        data = {
            "score": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    # -------------------------
    # CLASSIFICATION
    # -------------------------
    score = data["score"]

    if score >= 75:
        category = "🟢 Strong Candidate"
    elif score >= 50:
        category = "🟡 Average Candidate"
    else:
        category = "🔴 Weak Candidate"

    # -------------------------
    # FINAL RESULT
    # -------------------------
    st.markdown("## 🏁 Final Hiring Result")

    st.metric(label="📊 Match Score", value=f"{score}/100")

    st.markdown(f"### {category}")

    st.markdown("### ✅ Matched Skills")
    st.write(data["matched_skills"])

    st.markdown("### ❌ Missing Skills")
    st.write(data["missing_skills"])

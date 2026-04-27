from google import genai
import streamlit as st
import os
import time
from dotenv import load_dotenv
from utils import get_text_from_file

# Page configuration
st.set_page_config(
    page_title="AI Resume ATS Scorer Pro",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API Key not found. Please check your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)
MODEL_ID = "gemini-3-flash-preview"

# Custom CSS for a premium look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background-color: #f8fafc;
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background: linear-gradient(45deg, #2563eb, #3b82f6);
        color: white;
        font-weight: 700;
        border: none;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        background: linear-gradient(45deg, #1d4ed8, #2563eb);
    }
    
    .stTextArea>div>div>textarea {
        border-radius: 10px;
        border: 1px solid #e2e8f0;
    }

    /* Target the container borders to make them look like cards */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        border-radius: 16px !important;
        padding: 10px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d473530393318e422bb7.svg", width=60)
    st.title("ATS Elite")
    st.markdown("---")
    
    with st.expander("ℹ️ About this tool", expanded=True):
        st.write("This application uses **Gemini 3 Flash** to analyze your resume against industry-standard ATS algorithms and specific job requirements.")
    
    st.subheader("Your Journey")
    st.markdown("""
    1. 📤 **Upload**: Send your CV.
    2. 🎯 **Target**: Paste the JD.
    3. ⚡ **Analyze**: Instant feedback.
    4. 📈 **Improve**: Close the gap.
    5. 🏆 **Practice**: Ace the interview.
    """)
    st.markdown("---")
    st.caption("v2.0 | Powered by Google Gemini")

# Header
st.title("🎯 AI Resume Optimizer & Career Coach")
st.markdown("##### Land more interviews by tailoring your resume with AI-driven insights.")

# Layout for Inputs
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    with st.container(border=True):
        st.subheader("📄 Step 1: Your Resume")
        uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"], help="Upload your latest resume version.")
        
        resume_text = ""
        if uploaded_file:
            with st.status("Reading your document...", expanded=False) as status:
                resume_text = get_text_from_file(uploaded_file)
                time.sleep(0.5)
                if resume_text:
                    status.update(label="✅ Resume processed!", state="complete")
                    st.toast("Resume parsed successfully!", icon="✅")
                else:
                    status.update(label="❌ Failed to read document", state="error")

with col2:
    with st.container(border=True):
        st.subheader("💼 Step 2: Job Details")
        job_desc = st.text_area("Job Description", height=230, placeholder="Paste the job description here to compare...")

# Analysis Trigger
st.markdown("<br>", unsafe_allow_html=True)
analyze_btn = st.button("🚀 RUN ATS ANALYSIS")

if analyze_btn:
    if not resume_text or not job_desc:
        st.error("Missing Data: Please ensure both Resume and Job Description are provided.")
    else:
        # Step-by-step progress using st.status
        with st.status("Analyzing your career match...", expanded=True) as status:
            st.write("🔍 Extracting keywords from JD...")
            time.sleep(1)
            
            st.write("⚖️ Comparing skills and experience...")
            # Prompt Construction
            ats_prompt = f"Act as a senior recruiter. Analyze this resume: {resume_text} against this JD: {job_desc}. Provide: 1. Match Percentage (e.g. 'Match: 85%') 2. Top 3 Missing Skills 3. Formatting Feedback. Return as clean Markdown."
            
            st.write("🧠 Consulting Gemini 3 Flash...")
            try:
                ats_response = client.models.generate_content(model=MODEL_ID, contents=ats_prompt)
                
                st.write("📚 Finding upskilling resources...")
                resources_prompt = f"Based on the missing skills between this Resume and JD: Resume: {resume_text}, JD: {job_desc}, suggest 2 specific courses and 1 project idea. Markdown format."
                resources_response = client.models.generate_content(model=MODEL_ID, contents=resources_prompt)
                
                status.update(label="✅ Analysis Complete!", state="complete", expanded=False)
                st.toast("Analysis finished!", icon="🏆")
                
                # Display results in a clean layout
                st.markdown("---")
                st.header("📊 Your Report")
                
                res_col1, res_col2 = st.columns([1, 1])
                
                with res_col1:
                    with st.container(border=True):
                        st.markdown("### 📋 ATS Feedback")
                        st.markdown(ats_response.text)
                
                with res_col2:
                    with st.container(border=True):
                        st.markdown("### 🎓 Upskilling Plan")
                        st.markdown(resources_response.text)
                
                st.session_state.resume_text = resume_text
                st.session_state.job_desc = job_desc
                st.session_state.analysis_done = True
                
            except Exception as e:
                status.update(label="❌ Analysis Failed", state="error")
                st.error(f"Error: {e}")

# Mock Test Section
if st.session_state.get("analysis_done"):
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.subheader("🎤 Ready for the Interview?")
        st.write("Let's practice! I'll generate technical questions based on your profile and this specific job.")
        
        if st.button("✨ START MOCK INTERVIEW"):
            with st.status("Creating your personalized test...", expanded=True) as status:
                q_prompt = f"Generate 3 technical questions for this person (Resume: {st.session_state.resume_text}) applying for this role (JD: {st.session_state.job_desc})."
                questions = client.models.generate_content(model=MODEL_ID, contents=q_prompt)
                st.session_state.mock_questions = questions.text
                status.update(label="✅ Questions Ready!", state="complete")
                
        if st.session_state.get("mock_questions"):
            st.info("💡 Answer the questions below to get an AI evaluation.")
            st.markdown(st.session_state.mock_questions)
            user_answers = st.text_area("Your Answers", height=200, placeholder="Type your answers here...")
            
            if st.button("🏁 FINISH & EVALUATE"):
                with st.status("Scoring your performance...", expanded=True) as status:
                    eval_prompt = f"Evaluate these interview answers: {user_answers} against these questions: {st.session_state.mock_questions}. Give a score out of 10 and 3 tips."
                    evaluation = client.models.generate_content(model=MODEL_ID, contents=eval_prompt)
                    status.update(label="✅ Evaluation Done!", state="complete")
                    st.markdown("### 📈 Evaluation Result")
                    with st.container(border=True):
                        st.markdown(evaluation.text)

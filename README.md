# 🎯 AI Resume Optimizer & Career Coach

An AI-powered ATS (Applicant Tracking System) optimizer that helps candidates tailor their resumes to specific job descriptions using Google's **Gemini 3 Flash** model.

## 🚀 Features
- **ATS Scoring**: Get an instant match percentage between your resume and a job description.
- **Skill Gap Analysis**: Identify missing keywords and skills required for the role.
- **Upskilling Roadmap**: Get personalized course recommendations and project ideas.
- **Mock Interview**: Practice with AI-generated technical questions based on your profile.

---

## 🛠️ Installation & Setup

Follow these steps to get the app running on your local machine.

### 1. Prerequisites
- Python 3.9 or higher installed.
- A Google Gemini API Key (Get it from [Google AI Studio](https://aistudio.google.com/)).

### 2. Clone the Repository
```bash
git clone <your-repo-url>
cd resume-score
```

### 3. Set Up Virtual Environment (Recommended)
```bash
# Create venv
python -m venv venv

# Activate venv (MacOS/Linux)
source venv/bin/activate

# Activate venv (Windows)
# venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a file named `.env` in the root directory and add your API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

---

## 🏃 How to Run

### Start the Web Application
```bash
streamlit run app.py
```
The app will open automatically in your default browser at `http://localhost:8501`.

### Start the CLI Version (Optional)
```bash
python main.py
```

---

## 📂 Project Structure
- `app.py`: The main Streamlit web application.
- `main.py`: Command-line version of the tool.
- `utils.py`: Utility functions for PDF and DOCX text extraction.
- `requirements.txt`: Python package dependencies.
- `.env`: Secret keys and configurations.

---

## 🛡️ Privacy Note
Your resumes are processed in real-time by the Google Gemini API. No data is stored permanently on this local server.

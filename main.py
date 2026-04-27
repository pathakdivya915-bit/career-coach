import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. SETUP & CONFIGURATION
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

class MyGuide:
    def __init__(self):
        # Using gemini-1.5-flash for speed and efficiency
        self.model = genai.GenerativeModel('gemini-3-flash-preview')
        self.resume = ""
        self.job_description = ""

    def show_resume_guidelines(self):
        print("\n" + "="*50)
        print("QUICK GUIDE: GOOD VS. BAD RESUME")
        print("="*50)
        
        print("\n BAD RESUME EXAMPLE:")
        print("- Personal info like age, religion, or parents name included.")
        print("- Vague skills: 'Good at computers', 'Hard worker','intelligent'.")
        print("- Large blocks of text/paragraphs instead of bullet points and unnecessary information.")
        print("- No measurable results (e.g., 'Helped with a project','learn from this course').")

        print("\n GOOD RESUME EXAMPLE:")
        print("- Clear contact info and professional LinkedIn/GitHub links and short precise objective.")
        print("- Quantifiable achievements: 'Increased website speed by 40%'.")
        print("- Action verbs: 'Developed', 'Optimized', 'Led','build','experienced'.")
        print("- Clean formatting with standard sections:objective, Experience, Projects, Skills,certifications.")
        print("="*50 + "\n")

    def start_workflow(self):
        print("--- Welcome to 'My Guide' Career Assistant ---")
        self.show_resume_guidelines()
        
        # [Step 1 & 2]: UPLOAD & ANALYZE [cite: 1, 2]
        self.resume = input("\n[1] Paste your Resume : ")
        self.job_description = input("[2] Paste the Job Description: ")
        
        # [Step 3, 4, 5]: ATS SCORE & MATCH [cite: 3, 4, 5]
        print("\n--- Calculating ATS Score & Match Percentage ---")
        self.get_ats_score()

        # [Step 6, 7]: MISSING SKILLS & COURSES [cite: 6, 7]
        print("\n--- Identifying missing skills &  provide Resources ---")
        self.get_resources()

        # [Step 8, 9, 10]: MOCK TEST & FINAL EVALUATION [cite: 8, 9, 10]
        print("\n--- Starting Mock Written Assessment ---")
        self.run_mock_test()

    def get_ats_score(self):
        prompt = f"""
        Act as an expert ATS (Applicant Tracking System).
        Analyze the following Resume against the Job Description.
        1. Provide a Match Percentage.
        2. Give an ATS Compatibility Score (0-100).
        3. Highlight key alignment areas.
        
        Resume: {self.resume}
        JD: {self.job_description}
        """
        response = self.model.generate_content(prompt)
        print(response.text)

    def get_resources(self):
        prompt = f"""
        Based on this Resume and Job Description, identify:
        1. Missing critical skills.
        2. Missing keywords.
        3. Specific online courses or projects to improve this resume.
        
        Resume: {self.resume}
        JD: {self.job_description}
        """
        response = self.model.generate_content(prompt)
        print(response.text)

    def run_mock_test(self):
        # Generate Questions
        q_prompt = f"Generate 3 technical interview questions based on this resume: {self.resume}"
        questions = self.model.generate_content(q_prompt)
        print(f"\nQUESTIONS:\n{questions.text}")
        
        # Collect User Answers
        user_answers = input("\nYour Answers (type them here): ")
        
        # Final Evaluation [cite: 10]
        eval_prompt = f"Grade these answers and provide a final evaluation score out of 50: {user_answers}"
        final_eval = self.model.generate_content(eval_prompt)
        
        print("\n--- FINAL EVALUATION COMPLETE ---")
        print(final_eval.text)

# RUN THE PROGRAM
if __name__ == "__main__":
    guide = MyGuide()
    guide.start_workflow()
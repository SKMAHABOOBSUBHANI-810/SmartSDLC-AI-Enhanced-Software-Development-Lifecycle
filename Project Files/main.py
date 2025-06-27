from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .code_generator import generate_code

from .ai_story_generator import generate_user_stories
from .code_generator import generate_code
from .bug_resolver import fix_buggy_code
# import other routers similarly

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to SmartSDLC API"}

@app.post("/ai/generate-user-stories")
def user_stories_endpoint(pdf_text: str):
    stories = generate_user_stories(pdf_text)
    return {"user_stories": stories}

@app.post("/ai/generate-code")
def code_generation_endpoint(task_description: str):
    code = generate_code(task_description)
    return {"code": code}

@app.post("/ai/fix-bug")
def bug_fix_endpoint(code_snippet: str):
    fixed_code = fix_buggy_code(code_snippet)
    return {"fixed_code": fixed_code}

@app.post("/ai/generate-test-cases")
def test_case_generator_endpoint(code_or_requirement: str):
    # Dummy implementation; replace with Watsonx integration
    return {
        "test_cases": [
            "def test_login():\n    assert login('user', 'pass') == True",
            "def test_logout():\n    assert logout() == True"
        ]
    }
@app.post("/ai/summarize-code")
def code_summarizer_endpoint(code_snippet: str):
    # Dummy implementation; replace with Watsonx integration
    return {
        "summary": "This function logs in a user by checking their credentials."
    }
@app.post("/ai/chatbot")
def chatbot_endpoint(message: str):
    # Dummy implementation; replace with LangChain/Watsonx integration
    return {
        "response": f"AI Assistant: You asked '{message}'. Here is a helpful answer!"
    }
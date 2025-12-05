# quiz_app.py
import streamlit as st
import time
import random
import pandas as pd
import plotly.express as px

#from quiz_data import quiz_data

st.set_page_config(page_title="Quiz App", layout="centered")

# -------------------------
# Quiz data (example)
# -------------------------
quiz_data = [
    {"question": "What is the capital of France?",
     "options": ["Paris", "London", "Rome", "Berlin"],
     "answer": "Paris"},
    {"question": "Which language is primarily used for data science?",
     "options": ["Python", "C++", "HTML", "Java"],
     "answer": "Python"},
    {"question": "Which of the following is a Python web framework?",
     "options": ["React", "Flask", "Laravel", "Spring"],
     "answer": "Flask"},
    {"question": "What does HTML stand for?",
     "options": [
         "Hyper Text Markup Language",
         "HighText Machine Language",
         "HyperTabular Markup Language",
         "None of these"
     ],
     "answer": "Hyper Text Markup Language"},
    {"question": "Which of the following is used to style web pages?",
     "options": ["HTML", "CSS", "Python", "Java"],
     "answer": "CSS"}
]

# -------------------------
# Helpers
# -------------------------
def shuffle_quiz(q):
    random.shuffle(q)
    for item in q:
        random.shuffle(item["options"])
    return q

def save_result_df(answers):
    df = pd.DataFrame(answers)
    df.index = range(1, len(df) + 1)
    if "is_correct" in df.columns:
        df["is_correct"] = df["is_correct"].replace({True: "Correct✅", False: "Wrong❌"})
    score = (df["is_correct"] == "Correct✅").sum() if "is_correct" in df.columns else 0
    return df, score

# -------------------------
# Session state init
# -------------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = shuffle_quiz(quiz_data.copy())
    st.session_state.q_index = 0
    st.session_state.answer = []  # list of dic: question, selected, correct, is_correct
    st.session_state.finish = False
    st.session_state.start_time = time.time()

# safety defaults
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "answer" not in st.session_state:
    st.session_state.answer = []
if "finish" not in st.session_state:
    st.session_state.finish = False
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
    
if "results_df" not in st.session_state:
    st.session_state.results_df = pd.DataFrame(
        columns=["question", "selected", "correct", "is_correct"]
    )

# -------------------------
# Main UI for User
# -------------------------
st.title("Quiz App Programming")
st.caption("This is a teaching quiz app.")
st.write("Welcome to the Quiz app")
with st.sidebar:
    st.header("Clear Data 🧹")
    if st.button("Restart 🔁"):
        st.session_state.clear()
        st.rerun()
        
     # Footer: attribution
    st.markdown("<hr>", unsafe_allow_html=True)

    footer_part1 = """
    <div style='text-align:left; line-height: 1.6;'>
        <p style='font-size: 20px; font-weight: bold; margin: 0;'>
            Developed by <span style='color:#4CAF50;'>Rao Samad</span>
        </p>
    """

    st.markdown(footer_part1, unsafe_allow_html=True)

    footer_part2 = """
        <p style='margin: 6px 0; font-size: 16px;'>
            📧 <a href='mailto:samadrao@gmail.com' 
                style='text-decoration: none; color: #1E88E5;'>
                samadrao@gmail.com
            </a>
        </p>

        <p style='margin: 6px 0; font-size: 16px;'>
            📞 <a href='tel:+923000000000' 
                style='text-decoration: none; color: #1E88E5;'>
                +92 3046503593
            </a>
        </p>
    """

    st.markdown(footer_part2, unsafe_allow_html=True)

    footer_part3 = """
        <p style='font-size: 13px; color: black; margin-top: 8px;'>
            © 2025 All Rights Reserved
        </p>
    </div>
    """

    st.markdown(footer_part3, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
        
# ------------------------------------
# Prevent IndexError after restart
# ------------------------------------
if "quiz" not in st.session_state or len(st.session_state.quiz) == 0:
    st.session_state.quiz = shuffle_quiz(quiz_data.copy())
    st.session_state.q_index = 0
    st.session_state.answer = []
    st.session_state.finish = False
# -----------------------------------
# If finish -> show result
# -----------------------------------
if st.session_state.finish:
    st.header("Quiz Result")
    st.balloons()

    df, score = save_result_df(st.session_state.answer)
    st.success(f"Your Score : {score} / {len(st.session_state.answer)}")
    st.write(df[["question", "selected", "correct", "is_correct"]])
    st.stop()

# show question
q_index = st.session_state.q_index
q = st.session_state.quiz[q_index]

st.write(f"Question {q_index + 1} of {len(st.session_state.quiz)}")
st.subheader(f"{q_index + 1}: {q["question"]}")

# radio for options
option = st.radio("Choose one option:", q["options"], key=f"q{q_index}")

# layout: left=Next button, right=timer
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Next ➡️", type="primary",key=f"next_{q_index}"):
        # avoid duplicate append: only append if not already answered for this q_index
        # condition: number of saved answers should equal current question index
        if len(st.session_state.answer) == q_index:
            st.session_state.answer.append({
                "question": q["question"],
                "selected": option if option is not None else "No answer",
                "correct": q["answer"],
                "is_correct": option == q["answer"]
            })
        # move to next
        st.session_state.q_index += 1
        st.session_state.start_time = time.time()
        # if finished
        if st.session_state.q_index >= len(st.session_state.quiz):
            st.session_state.finish = True
        st.rerun()

with col2:
    # Timer display and auto-next logic
    duration = 15  # seconds per question
    elapsed = int(time.time() - st.session_state.start_time)
    time_left = max(0, duration - elapsed)
    if time_left > 7:
        st.success(f"⏱️ Time left: {time_left} seconds")
    elif time_left > 3:
        st.warning(f"⏱️ Time left: {time_left} seconds")
        st.toast(f"⏱️ Time left: {time_left} seconds")
    else:
        st.error(f"⏱️ Time left: {time_left} seconds")

    # If time left > 0: wait 1 second and rerun so countdown updates visibly
    if time_left > 0:
        time.sleep(1)
        st.rerun()
    else:
        # time expired -> only append if this question not answered yet
        # check same condition as manual next
        if len(st.session_state.answer) == q_index:
            st.session_state.answer.append({
                "question": q["question"],
                "selected": "⏰ Time's up",
                "correct": q["answer"],
                "is_correct": False
            })
        # move to next question
        st.session_state.q_index += 1
        st.session_state.start_time = time.time()
        if st.session_state.q_index >= len(st.session_state.quiz):
            st.session_state.finish = True
        st.rerun()
        

    
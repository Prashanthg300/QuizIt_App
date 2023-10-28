import streamlit as st
from question_model import Question

from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from input_window import InputWindow
import requests
from random import shuffle
import html

def run_quiz():
    st.text("The quiz has been started.")
    input_window = InputWindow()
    input_window.start()

    topic = input_window.return_value()


    response = requests.get(url="https://opentdb.com/api_category.php")
    topic_data = response.json()
            
    parameters = {
        "amount": 10,
        "type": "multiple",
        "category": int(topic)+8
    }

    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    question_data = response.json()["results"]

    question_bank = []

    for question in question_data:
        choices = []
        question_text = html.unescape(question["question"])
        correct_answer = html.unescape(question["correct_answer"])
        incorrect_answers = question["incorrect_answers"]
        for ans in incorrect_answers:
            choices.append(html.unescape(ans))
        choices.append(correct_answer)
        shuffle(choices)
        new_question = Question(question_text, correct_answer, choices)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_no}")

st.title('Quiz App')
start = st.button('Start')
reset = st.button('Reset')

if 'quiz_ran' not in st.session_state:
    st.write("Welcome to the Quiz! Click the 'Start Quiz' button below to begin.")
    st.session_state.quiz_ran = False

if start:
    run_quiz()
    st.session_state.quiz_ran = True

if reset:
    st.text("The quiz has not been started yet.")
    st.experimental_rerun()


"""
Student Pass Predictor
Run locally: streamlit run app.py
"""

import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression


# -------------------- PAGE SETUP --------------------

st.set_page_config(
    page_title="Student Pass Predictor",
    page_icon="🎓"
)

st.title("🎓 Will this student pass?")

st.write(
    "This is the logistic regression model. I have built "
    "now running as a website anyone can use."
)


# -------------------- LOAD AND TRAIN MODEL --------------------

@st.cache_resource
def load_model():

    students = pd.read_csv("my_students.csv")

    X = students[["hours_studied", "attendance", "prev_marks"]]
    y = students["passed"]

    model = LogisticRegression(max_iter=1000)

    model.fit(X, y)

    return model, students


model, students = load_model()


# -------------------- USER INPUTS --------------------

st.subheader("Enter the student's details")

hours = st.slider(
    "Hours studied",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.1
)

attendance = st.slider(
    "Attendance %",
    min_value=40,
    max_value=100,
    value=75
)

prev_marks = st.slider(
    "Previous marks",
    min_value=0,
    max_value=100,
    value=60
)


# -------------------- PREDICTION --------------------

if st.button("Predict", type="primary"):

    one_student = pd.DataFrame(
        [[hours, attendance, prev_marks]],
        columns=["hours_studied", "attendance", "prev_marks"]
    )

    prediction = model.predict(one_student)[0]

    probabilities = model.predict_proba(one_student)[0]

    # Find probability corresponding to class 1 (PASS)
    pass_index = list(model.classes_).index(1)
    chance = probabilities[pass_index]

    st.divider()

    if prediction == 1:
        st.success(f"### PASS — {chance:.1%} probability")
    else:
        st.error(f"### FAIL — {1 - chance:.1%} probability")

    st.progress(float(chance))

    st.caption(f"Chance of passing: {chance:.1%}")
                                          
    if 0.40 < chance < 0.60:
        st.warning(
            "The model is close to 50/50 here. "
            "It is honestly unsure about this prediction."
        )


# -------------------- MODEL INFORMATION --------------------

with st.expander("What did the model actually learn?"):

    weights = pd.DataFrame({
        "column": ["hours_studied", "attendance", "prev_marks"],
        "weight": model.coef_[0].round(3)
    })

    st.table(weights)

    st.caption(
        "These three numbers represent the learned coefficients. "
        "They are on different scales, so compare them carefully."
    )


# -------------------- TRAINING DATA --------------------

with st.expander("See the training data"):

    st.write(f"{len(students)} students")

    st.dataframe(students, height=260)


# -------------------- FOOTER --------------------

st.divider()

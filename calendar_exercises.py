import streamlit as st

st.set_page_config(page_title="Calendar Exercises", layout="wide")

st.title("📅 Calendar Date Exercises")
st.write("Practice reading and working with calendar dates.")

st.divider()

exercises = [
    {
        "q": "Read 11.22.2009 in words",
        "options": ["November 22, 2009", "November 2, 2099", "February 11, 2009", "November 20, 2029"],
        "answer": "November 22, 2009",
        "hint": "The first part is the month, second is the day, third is the year."
    },
    {
        "q": "Which month is 09 in 09.16.2026?",
        "options": ["June", "September", "November", "October"],
        "answer": "September",
        "hint": "09 is the 9th month."
    },
    {
        "q": "Which part is the day in 07.04.2025?",
        "options": ["07", "04", "2025", "25"],
        "answer": "04",
        "hint": "The middle part is the day."
    },
    {
        "q": "What is 3 days after September 16?",
        "options": ["September 13", "September 16", "September 19", "October 16"],
        "answer": "September 19",
        "hint": "Moving forward means adding days."
    },
    {
        "q": "What is 2 days before October 10?",
        "options": ["October 2", "October 8", "October 12", "November 10"],
        "answer": "October 8",
        "hint": "Moving backward means subtracting days."
    },
    {
        "q": "Which date is written as November 22, 2009?",
        "options": ["11.02.2009", "02.11.2009", "11.22.2009", "22.11.2009"],
        "answer": "11.22.2009",
        "hint": "The numeric order is month, day, year."
    },
    {
        "q": "A party is 4 days away. 1 day passes. How many days remain?",
        "options": ["3", "4", "5", "1"],
        "answer": "3",
        "hint": "The remaining days get smaller, so subtract."
    },
    {
        "q": "Which operation finds days added to a calendar?",
        "options": ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"],
        "answer": "Add (+)",
        "hint": "Adding moves forward on the calendar."
    },
    {
        "q": "What year is in 02.14.2027?",
        "options": ["02", "14", "2027", "27"],
        "answer": "2027",
        "hint": "The year is the last part of the date."
    },
    {
        "q": "Which date comes first?",
        "options": ["September 20", "September 16", "September 25", "October 1"],
        "answer": "September 16",
        "hint": "Earlier dates come first when the month is the same."
    },
    {
        "q": "Read 05.31.2023 in words",
        "options": ["May 31, 2023", "March 5, 2023", "May 5, 2031", "March 31, 2025"],
        "answer": "May 31, 2023",
        "hint": "05 = May, 31 = day, 2023 = year."
    },
    {
        "q": "How many days from September 16 to September 23?",
        "options": ["5", "7", "10", "9"],
        "answer": "7",
        "hint": "Count forward one week."
    },
    {
        "q": "Which operation finds days removed from a calendar?",
        "options": ["Add (+)", "Subtract (-)", "Multiply (x)", "Divide (/)"],
        "answer": "Subtract (-)",
        "hint": "Subtracting moves backward on the calendar."
    },
    {
        "q": "Read 12.25.2024 in words",
        "options": ["December 25, 2024", "December 12, 2025", "October 25, 2024", "December 2, 2024"],
        "answer": "December 25, 2024",
        "hint": "12 = December, 25 = day, 2024 = year."
    },
    {
        "q": "What is 5 days after October 28?",
        "options": ["October 30", "October 33", "November 2", "November 5"],
        "answer": "November 2",
        "hint": "Days wrap into the next month."
    },
]

score = 0
for i, ex in enumerate(exercises):
    with st.container():
        st.markdown(f"**Question {i + 1}:** {ex['q']}")
        answer = st.radio("", ex['options'], key=f"q_{i}", label_visibility="collapsed")
        
        if st.button("Check", key=f"check_{i}"):
            if answer == ex['answer']:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error(f"❌ Incorrect. The answer is **{ex['answer']}**")
                st.info(f"💡 {ex['hint']}")
        st.divider()

if st.button("Show Final Score"):
    st.balloons()
    st.metric("Score", f"{score} / {len(exercises)}")

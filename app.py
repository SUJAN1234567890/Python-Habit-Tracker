import streamlit as st
from database import add_habit, get_all_habits, log_habit_completion, get_habit_completion_count, get_today
import datetime

st.title("Habit Tracker")
habit_name = st.text_input("Enter a new habit:")
if st.button("Add Habit"):
    if habit_name:
        add_habit(habit_name)
        st.success(f"Habit '{habit_name}' added!")
    else:
        st.error("Please enter a habit name.")

habits = get_all_habits()
for habit in habits :
    st.write(f"Habit: {habit[1]} (ID: {habit[0]})")
    if st.button(f"Log Completion for Habit ID {habit[0]}"):
        log_habit_completion(habit[0], datetime.date.today())
        st.success(f"Logged completion for habit '{habit[1]}'!")

if st.button("Show Today's Completions") :
    today = datetime.date.today()
    completions = get_today(today)
    if completions:
        st.write(f"Completions for {today}:")
        for completion in completions:
            habit_id = completion[1]
            habit_name = next((habit[1] for habit in habits if habit[0] == habit_id), None)
            st.write(habit_name)
    else:
        st.write(f"No completions logged for {today}.")


habit_id_entered =st.text_input("Enter The Habit ID to check consistency :")
if habit_id_entered :
    st.write("Habit Completion Counts:")
    st.write(f"The number of time the habit is repeated :{get_habit_completion_count(habit_id_entered)}")

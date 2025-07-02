import streamlit as st 
import pandas as pd

st.set_page_config(page_title="School Paper Usage Calculator", layout="centered") 
st.title("📄 School Paper Usage & Cost Estimator")

st.markdown(""" This calculator estimates how much paper a school uses in a year, and how much it could cost — based on your input values. """)

#Inputfields

students = st.number_input("Number of students", value=1000, step=50) 
teachers = st.number_input("Number of teachers", value=40, step=5) 
weeks_per_year = st.number_input("Active school weeks per year", value=40) 
months_per_year = st.number_input("Academic months per year", value=10)

exams_per_year = st.slider("Exams per year per student", 1, 10, value=6) 
worksheets_per_week = st.slider("Worksheets per student per week", 0, 5, value=2) 
homework_per_week = st.slider("Homework per student per week", 0, 5, value=2) 
circulars_per_week = st.slider("Printed circulars per student per week", 0, 5, value=1) 
admin_docs_per_teacher_weekly = st.slider("Admin sheets per teacher per week", 0, 10, value=5) 
records_per_student = st.slider("Student records stored on paper", 0, 10, value=5) 
certificates_per_event = st.slider("Certificates per school event", 0, 500, value=200) 
posters_forms_per_event = st.slider("Posters/forms per event", 0, 100, value=50) 
events_per_year = st.slider("School events per year", 0, 30, value=10) 
teacher_pages_per_week = st.slider("Teacher lesson printouts/week", 0, 20, value=10) 
art_projects_per_month = st.slider("Arts/crafts projects per student per month", 0, 5, value=1) 
tags_per_student = st.slider("Labels per student (name, files etc.)", 0, 5, value=2) 
tags_per_event = st.slider("Labels per event (ID cards etc.)", 0, 200, value=100) 
gift_kits = st.slider("Gift/stationery kits per year", 0, 500, value=100) 
forms_per_student = st.slider("Finance/permission forms per student", 0, 10, value=3) 
cost_per_sheet = st.number_input("Cost per sheet (INR, incl. ink)", value=1.5, step=0.1)

#Calculation

def compute_usage(): 
 data = { "Assessments": students * exams_per_year * 2, "Worksheets": students * worksheets_per_week * weeks_per_year, "Homework": students * homework_per_week * weeks_per_year, "Circulars & Communication": students * circulars_per_week * weeks_per_year, "Admin (Teacher use)": teachers * admin_docs_per_teacher_weekly * weeks_per_year, "Student Records": students * records_per_student, "Events & Certificates": events_per_year * (certificates_per_event + posters_forms_per_event), "Teacher Notes": teachers * teacher_pages_per_week * weeks_per_year, "Arts & Crafts": students * art_projects_per_month * months_per_year, "Labels & Stickers": students * tags_per_student + events_per_year * tags_per_event, "Packaging & Gifting": gift_kits, "Finance & Docs": students * forms_per_student, } 
 df = pd.DataFrame(list(data.items()), columns=["Category", "Sheets Used"]) 
 df["Cost (INR)"] = df["Sheets Used"] * cost_per_sheet 
 total = pd.DataFrame([{"Category": "TOTAL", "Sheets Used": df["Sheets Used"].sum(), "Cost (INR)": df["Cost (INR)"].sum()}]) 
 df = pd.concat([df, total], ignore_index=True) 
 return df

#Run

#if st.button("Calculate"): result_df = compute_usage() 
#st.dataframe(result_df.style.format({"Cost (INR)": "₹{:.2f}"})) 
#st.success("Done! Scroll below to see your breakdown.")

st.markdown("""
---
💡 **Know a school that should see this?**
[Click to copy this link](https://school-paper-system-reform.streamlit.app) and send it their way.
""")

if st.button("Calculate"):
    try:
        result_df = compute_usage()
        st.dataframe(result_df.style.format({"Cost (INR)": "₹{:.2f}"}))
        st.success("Done! Scroll below to see your breakdown.")
        # Suggestions based on key categories
        st.markdown("### 🌱 Suggested Reforms")
        if result_df.loc[result_df['Category'] == "Worksheets", "Sheets Used"].values[0] > 50000:
            st.write("📚 Too many worksheets? Consider switching to double-sided or recycled paper. Or go compostable weekly packets.")
        if result_df.loc[result_df['Category'] == "Homework", "Sheets Used"].values[0] > 50000:
            st.write("🏠 High homework paper usage? Encourage digital upload or rotating group books.")
        if result_df.loc[result_df['Category'] == "Events & Certificates", "Sheets Used"].values[0] > 2000:
            st.write("🎉 Large event waste? Use eco-certificates and projector-based recognition.")
        if result_df.loc[result_df['Category'] == "Circulars & Communication", "Sheets Used"].values[0] > 20000:
            st.write("📣 Switch to digital/WhatsApp circulars for day-to-day communication.")
        if result_df.loc[result_df['Category'] == "Teacher Notes", "Sheets Used"].values[0] > 10000:
            st.write("🧑‍🏫 Too many lesson prints? Try reusable planning boards or shared digital notebooks.")

         
    except Exception as e:
        st.error(f"Something went wrong: {e}")

import random

eco_hacks = [
    "Wrap gifts in old calendars and tag them: ‘This was going to the bin.’",
    "Your rejected resume = journaling gold.",
    "Every eco-thing you don’t buy is greener than the one you do.",
    "This jar held trauma. Now it holds sugar.",
    "Label your plants after your exes. Let them grow this time.",
    "Compost my feelings log: What are you ready to rot today?",
    "Stitch the thing you couldn’t say. Tears optional.",
    "‘Didn’t buy it.’ Still hot.",
    "Made from trash. What’s your excuse?",
           ]

##st.info(random.choice(eco_hacks))

#st.markdown("### 💬 Community Reform Wall")
##st.write("Real ideas. Gremlin genius. Submit your own below!")
##if st.button("Shuffle Wall Quote"):
 ##   st.rerun()

#user_idea = st.text_input("🧠 Got an idea for eco reform? Drop it here:")
#if user_idea:
       #  st.write("✅ Thank you for your idea! It’ll be compiled in our reform list.")
         #(Later you can add a Google Sheet or save to GitHub)

# Initialize an empty list in session state if not already present
if "user_ideas_list" not in st.session_state:
    st.session_state.user_ideas_list = []

user_idea = st.text_input("💬 Got an idea for eco reform? Drop it here:")

if user_idea:
    st.session_state.user_ideas_list.append(user_idea)
    st.success("✅ Thank you for your idea! It’s been added to the reform wall.")

# Display all submitted ideas
if st.session_state.user_ideas_list:
    st.markdown("### 🌿 Community Reform Wall")
    for idx, idea in enumerate(st.session_state.user_ideas_list, 1):
        st.write(f"{idx}. {idea}")


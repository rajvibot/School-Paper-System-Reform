import streamlit as st 
import pandas as pd

st.set_page_config(page_title="School Paper Usage Calculator", layout="centered") 
st.title("📄 School Paper Usage & Cost Estimator")

st.markdown(""" This calculator estimates how much paper a school uses in a year, and how much it could cost — based on your input values. """)

with st.sidebar:
    st.header("🌿 Phoenix Rising")

    st.markdown("""
    ### 💬 A Note from Me

    If this project speaks to your heart, I’d love to hear from you. Your comments, reflections, and shares help this work ripple further — thank you for being here, for caring, and for imagining new ways to grow.


    ### 🪴🔗 Connect & Explore my other work

    🌐 [Amarnath Yatra Safety Guide Toolkit Website](https://rajvi11.my.canva.site/amarnath-yatra-guide-safety-toolkit)  
    ✍️ [LinkedIn](https://www.linkedin.com/in/rajvi-mittal/)  
    🎨 [Behance](https://www.behance.net/rajvimittal1)
    🧩 [Topmate](https://topmate.io/rajvi_mittal11)
    
    Let’s rise, together.   

    *Rajvi Mittal (Phoenix Rising)*

    ---

    ### 🌍 Inspired by #GenerationRestoration

    This work is a quiet tribute to the Earth — reminding us that healing happens in soft, patient cycles. As we restore ourselves, we restore the world.

    ---

    ### ✨ What is a Seed Paper Journal?

    A **seed paper journal** is made from eco-friendly paper embedded with real seeds (marigold, basil, tulsi, etc.).

    When you're done using it, you can **plant the pages** and grow 🌼🌿 — a gentle act of regeneration and hope.

    ---

    ### 🌟 Why Seed Paper Journals Matter

    ✅ Fully biodegradable & zero waste  
    ✅ Your words become growth 🌱  
    ✅ Meaningful, mindful participation  
    ✅ Perfect for eco-gifting, journaling, art

    ---

    ### 🖊️ About Sustainable Inks

    Many **eco pens and seed pens** now use:

    ✅ Soy/vegetable-based inks  
    ✅ Non-toxic, biodegradable pigments  
    ✅ Water-based, compost-safe formulations  
    ✅ Paper barrels instead of plastic

    ---

    ### ☕ Support This Work

    If you want to contribut helping keep these systems, tools, and art alive:

    [💚 Buy Me a Plant](https://buymeacoffee.com/rajvimittal)

    Every small support fuels big soft revolutions. 🌱
   
    ✨ Thank you for exploring, dreaming, and restoring.

    """)


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


st.markdown("""
---
💡 **Know a school that should see this?**
[Click to copy this link](https://school-paper-system-reform.streamlit.app) and send it their way.
""")

import random

# All your micro eco rituals combined:
eco_challenges = [
    # Week 1
    "🖤 Blackout a bad day — Turn a printed bill into poetry.",
    "👑 Crown Yourself with Cardboard — Toilet roll = king energy.",
    "🫙 Jar of Unsaid Things — Write what you wanted to say this week. Put it in your old coffee jar.",
    "✉️ Envelope Your Regret — Print a template on scrap paper. Mail it to yourself.",
    "👗 Wear Something That Still Works — Bonus if it’s from 2014.",
    "🔖 Reframe That Item — Label a jar 'hope.' See what you put inside.",
    "☕ Use the Ugly Mug — Romanticize the chipped one. It's you-coded.",
    # Week 2
    "📚 Leave a Note in a Bookstore Book — Write 'You’ll be okay' in the margins of capitalism.",
    "🧵 Fix Something with Thread, Not Shame — Button, sock, bag strap. No one has to know.",
    "🌱 Turn a Packet into a Planter — Maggi packet + mint sprout = kitchen redemption.",
    "📝 Print on the Back of That Failed Resume — Give your failure a second job.",
    "🌙 Draw a Moon on a Used Tissue — Tell her what you’re done with.",
    "💌 Give a Compliment Instead of a Lecture — The earth wants joy, not guilt.",
    "🔄 Upcycle a Conversation — Bring back an old dialogue. Ask it again, softer.",
    # Week 3
    "💃 Wear Something Just Because It Feels Like You — Not because it matches.",
    "🧣 DIY a Scarf From a Saree Scrap — Or even a curtain. No one's watching.",
    "🛍️ Make a 'Didn’t Buy' List — Feel proud. Not deprived.",
    "🚫 Unfollow 3 Style Influencers Who Make You Want What You Don’t Need.",
    "🏷️ Make a Label for Your Closet — 'This is not Zara. This is survival.'",
    "🪞 Drape Yourself in Leftovers — Literally or metaphorically. Bonus: mirror selfie.",
    "🎁 Gift Someone Something You Already Own — Make it feel sacred.",
    # Week 4
    "🌿 Plant a Spice You Actually Use — Basil, methi, ajwain — no pressure.",
    "🪴 Compost a Memory — Write it, fold it, bury it in soil.",
    "🗞️ Wrap a Gift in Old Newspaper — Add a line: 'This paper’s seen more than both of us.'",
    "🪨 Repurpose a Plastic Container into an Altar — Add stone, flower, coin. Call it a vibe box.",
    "🌳 Thank the Tree You Ignore — Yes, the one near your parking spot.",
    "🚌 Romanticize a Bus Ride — Less emissions, more imagination.",
    "🔄 Invent Your Own Ritual — Something soft, cyclical, yours.",
    # Bonus
    "📝 Buy Nothing Today. Write Instead.",
    "🌍 Tell Someone Your Earth is Cutie Too."
]

st.markdown("### ✨ Need a micro eco-reform challenge?")
if st.button("🌿 Give me a challenge!"):
    st.info(random.choice(eco_challenges))


#user_idea = st.text_input("🧠 Got an idea for eco reform? Drop it here:")
#if user_idea:
       #  st.write("✅ Thank you for your idea! It’ll be compiled in our reform list.")
         #(Later you can add a Google Sheet or save to GitHub)



import pandas as pd

if "user_ideas_list" not in st.session_state:
    st.session_state.user_ideas_list = []

user_idea = st.text_input("💬 Got an idea for eco reform? Drop it here:")

if user_idea:
    st.session_state.user_ideas_list.append(user_idea)
    st.success("✅ Thank you! Added to the Reform Wall.")

if st.session_state.user_ideas_list:
    st.markdown("### 🌿 Community Reform Wall")
    for idx, idea in enumerate(st.session_state.user_ideas_list, 1):
        st.write(f"{idx}. {idea}")

    # Download option
    if st.button("Download ideas as CSV"):
        df = pd.DataFrame(st.session_state.user_ideas_list, columns=["Ideas"])
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download", csv, "eco_reform_ideas.csv", "text/csv")

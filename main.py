import streamlit as st

# Application title
st.title("Understanding Your Screen Use Habits and Health Support")

# Introduction
st.write("""
This tool will help you better understand your daily screen habits and provide supportive ideas for balancing screen time in a health-conscious way.
""")

# Question 1: Estimated hours of daily screen time
screen_time = st.selectbox("How many hours a day do you estimate you spend with screens?", 
                           options=["Less than 2 hours", "2-4 hours", "4-6 hours", "6-8 hours", "More than 8 hours"])

# Question 2: Devices frequently used
devices = st.multiselect("Which of these devices do you interact with daily? Select all that apply.",
                         options=["Smartphone", "Tablet", "Laptop", "Desktop Computer", "Television", "Other"])

# Question 3: Awareness of potential health effects
awareness = st.radio("Are you aware of any potential health impacts from frequent screen use?",
                     options=["Yes, I am aware", "No, I am not aware", "I've heard some information"])

# Question 4: Experiencing any health effects
health_effects = st.multiselect("Do you experience any of these related health effects? Select all that apply.",
                                options=["Difficulty sleeping", "Headaches", "Eye strain", "Neck or shoulder pain", "None of these"])

# Question 5: Have you tried any methods to manage screen use?
manage_screen_time = st.radio("Have you tried anything to manage your screen time or reduce screen-related health impacts?",
                              options=["Yes", "No"])

# Personalized Score Calculation
# Assign values to responses to calculate a score from 0-100%
score = 0

# Adjust score based on screen time response
if screen_time == "Less than 2 hours":
    score += 10
elif screen_time == "2-4 hours":
    score += 25
elif screen_time == "4-6 hours":
    score += 50
elif screen_time == "6-8 hours":
    score += 75
else:
    score += 90

# Add points based on number of devices used
score += len(devices) * 5

# Adjust score based on health awareness and effects experienced
if awareness != "No, I am not aware":
    score += 10
score += len(health_effects) * 5

# Adjust score based on if they tried managing screen time
if manage_screen_time == "Yes":
    score -= 10  # Slight deduction for proactive steps

# Cap the score at 100
score = min(score, 100)

# Display user score with a comparison to an estimated national average (e.g., 50% as a reference point)
st.write("### Your Screen Use Score: ", score, "%")
if score > 50:
    st.write("""
    Based on your responses, your screen use is above average, which may increase the likelihood of experiencing common screen-related health effects.
    Here are some supportive ideas to help balance your screen habits without disrupting your daily routines:
    """)

    # Suggestions to manage screen use
    st.markdown("""
    - **Use Blue Light Filters**: Try setting devices to "Night Mode" or using apps like F.lux to reduce screen brightness at night.
    - **Consider Blue Light Glasses**: Affordable options for glasses that reduce eye strain.
    - **Take Breaks and Eye Exercises**: The 20-20-20 rule: every 20 minutes, look at something 20 feet away for 20 seconds.
    - **Reduce Screen Time in the Morning and Evening**: Limiting screen use 30 minutes before bed can support better sleep.
    - **Physical Movement**: Stand up, stretch, or move around regularly to reduce neck and shoulder strain.
    """)
else:
    st.write("Your screen time is within a typical range. Continue practicing healthy habits to support your screen use!")

# Final note
st.write("""
Thank you for using this tool to gain insights into your screen use habits. Small, consistent practices can support your well-being in a screen-centered world!
""")

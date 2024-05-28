import streamlit as st

def calculate_bmi(height, weight):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        return bmi
    else:
        return None

# Main application
st.title("User Sign In")

# User input form
username = st.text_input("Username")
password = st.text_input("Password", type="password")
age = st.number_input("Age", min_value=1, max_value=120)
gender = st.radio("Gender", ["Male", "Female", "Other"])
height = st.number_input("Height (in meters)", min_value=0.1, max_value=3.0)
weight = st.number_input("Weight (in kg)", min_value=1.0)
health_goals = st.text_area("Health Goals")

if st.button("Sign In"):
    st.success(f"Welcome, {username}!")

    # Display user profile
    st.subheader("User Profile")
    st.markdown(f"**Username:** {username}")
    st.markdown(f"**Age:** {age}")
    st.markdown(f"**Gender:** {gender}")
    st.markdown(f"**Height:** {height} meters")
    st.markdown(f"**Weight:** {weight} kg")
    st.markdown(f"**Health Goals:** {health_goals}")

    # Calculate BMI
    bmi = calculate_bmi(height, weight)
    if bmi is not None:
        st.markdown(f"**BMI:** {bmi:.2f}")

        # Display diet recommendations based on BMI
        st.subheader("Diet Recommendations")
        if bmi < 18.5:
            st.info("Underweight: Consider increasing calorie intake with a balanced diet.")
            st.info("Have the following food :")
            st.info("For breakfast have Oats(100 g) with milk(200ml)")
            st.info("For Lunch have Rice(200g) with chicken(100g)")
            st.info("For snacks have nuts(100g)")
            st.info("For Dinner have Fish with roti(4) or chapathi(4)")

        elif 18.5 <= bmi < 24.9:
            st.success("Normal weight: Maintain a balanced diet with regular exercise.")
        elif 25 <= bmi < 29.9:
            st.warning("Overweight: Focus on portion control and increase physical activity.")
        else:
            st.error("Obese: Consult with a healthcare professional for personalized advice.")

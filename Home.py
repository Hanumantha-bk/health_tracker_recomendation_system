import streamlit as st
st.set_page_config(
    page_title="Health Tracker and Recommendation System",
    page_icon="⚕️",
)
"""
# Welcome to Health Tracker and Recommendation System🧬
"""
st.image("ht.png")
st.markdown(
    """
   
   
    

    ---

    Our platform begins by inviting users into a personalized health ecosystem. 
    Through seamless user registration and profile creation, 
    individuals embark on a journey of self-discovery and well-being enhancement. 
    By integrating with wearable devices or allowing manual entry, 
    the system meticulously tracks a spectrum of health metrics, 
    ranging from physical activity and sleep patterns to nutritional intake and heart rate.

"""

)
user_name = st.text_input("Enter your name:")
if user_name:
    st.write(f"Hello, {user_name}! How can we assist you today?")

st.markdown(
"""

    Creating a Health Tracker and Recommendation System involves combining technology, 
    data analytics, and user interaction to monitor health metrics and provide 
    personalized recommendations.

    Integrate with wearables or allow manual entry of data for tracking health metrics such as:

   

    1. Physical activity (steps, distance, calories burned)
    2. Heart rate 
    3. Sleep patterns
    4. Nutrition intake
    5. Weight
    
 
    
    ---
    
    
    
    """
)

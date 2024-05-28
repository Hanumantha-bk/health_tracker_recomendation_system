import streamlit as st
from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    age = Column(Integer)
    gender = Column(String)
    health_goals = Column(String)
    is_authenticated = Column(Boolean, default=False)

class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    is_authenticated = Column(Boolean, default=False)

class SessionState:
    def __init__(self):
        self.is_user_authenticated = False
        self.is_admin_authenticated = False
        self.username = ""

session_state = SessionState()

# Create an SQLite database
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Check if session_state has been initialized
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False
    st.session_state.is_admin_authenticated = False
    st.session_state.username = None

# Hardcoded admin credentials (for demonstration purposes)
admin_username = "han"
admin_password = "han@123"

# Admin login section
st.title("Admin Login")
entered_admin_username = st.text_input("Admin Username")
entered_admin_password = st.text_input("Admin Password", type="password")

if st.button("Admin Log In"):
    if entered_admin_username == admin_username and entered_admin_password == admin_password:
        st.session_state.is_admin_authenticated = True
        st.success("Admin logged in successfully!")
    else:
        st.error("Invalid admin credentials. Please try again.")

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["User Profiles", "Accept Users", "Accepted Users", "Delete Users", "Logout"])

# Main application
if st.session_state.is_admin_authenticated:
    if page == "User Profiles":
        st.title("User Profiles")

        # Display user profiles
        db = SessionLocal()
        users = db.query(User).all()

        for user in users:
            st.subheader(f"User Profile - {user.username}")
            st.markdown(f"**Username:** {user.username}")
            st.markdown(f"**Age:** {user.age}")
            st.markdown(f"**Gender:** {user.gender}")
            st.markdown(f"**Health Goals:** {user.health_goals}")
            st.markdown("---")

        db.close()

    elif page == "Accept Users":
        st.title("Accept New Users")

        # Display pending user registrations
        db = SessionLocal()
        pending_users = db.query(User).filter(User.is_authenticated == False).all()

        for pending_user in pending_users:
            st.subheader(f"Pending User - {pending_user.username}")
            st.markdown(f"**Username:** {pending_user.username}")
            st.markdown(f"**Age:** {pending_user.age}")
            st.markdown(f"**Gender:** {pending_user.gender}")
            st.markdown(f"**Health Goals:** {pending_user.health_goals}")
            
            # Accept button for each pending user
            accept_button_key = f"accept_button_{pending_user.id}"
            if st.button(f"Accept {pending_user.username}", key=accept_button_key):
                # Provide motivational and engaging content
                motivation_content = st.text_area("Motivational Content", "Enter motivational and engaging content here.")
                st.success(f"User {pending_user.username} accepted successfully.")
                st.success("Motivational Content:")
                st.markdown(motivation_content)

                # Display user details
                st.subheader(f"User Details - {pending_user.username}")
                st.markdown(f"**Username:** {pending_user.username}")
                st.markdown(f"**Age:** {pending_user.age}")
                st.markdown(f"**Gender:** {pending_user.gender}")
                st.markdown(f"**Health Goals:** {pending_user.health_goals}")

                db.query(User).filter(User.id == pending_user.id).update({"is_authenticated": True})
                db.commit()
                
            st.markdown("---")

        db.close()

    elif page == "Accepted Users":
        st.title("Accepted Users")

        # Display accepted users
        db = SessionLocal()
        accepted_users = db.query(User).filter(User.is_authenticated == True).all()

        for accepted_user in accepted_users:
            st.subheader(f"Accepted User - {accepted_user.username}")
            st.markdown(f"**Username:** {accepted_user.username}")
            st.markdown(f"**Age:** {accepted_user.age}")
            st.markdown(f"**Gender:** {accepted_user.gender}")
            st.markdown(f"**Health Goals:** {accepted_user.health_goals}")
            st.markdown("---")

        db.close()

    elif page == "Delete Users":
        st.title("Delete Users")

        # Display existing users for deletion
        db = SessionLocal()
        existing_users = db.query(User).all()

        for existing_user in existing_users:
            st.subheader(f"Existing User - {existing_user.username}")
            st.markdown(f"**Username:** {existing_user.username}")
            st.markdown(f"**Age:** {existing_user.age}")
            st.markdown(f"**Gender:** {existing_user.gender}")
            st.markdown(f"**Health Goals:** {existing_user.health_goals}")
            if st.button(f"Delete {existing_user.username}"):
                db.delete(existing_user)
                db.commit()
                st.success(f"User {existing_user.username} deleted successfully.")
            st.markdown("---")

        db.close()

    elif page == "Logout":
        st.session_state.is_admin_authenticated = False
        st.session_state.username = None
        st.success("Logged out successfully!")

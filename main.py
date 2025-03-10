import streamlit as st
import string 
import random


st.markdown(
    """
    <style>
        /* Full App Background */
        .stApp {
            background-color: #121212;
            color: white;
            font-family: 'Arial', sans-serif;
        }

        /* Title Styling */
        .stTitle {
            color: #ff9800;
            text-align: center;
            font-weight: bold;
            font-size: 36px;
        }

        /* Input Fields */
        div[data-baseweb="input"] input {
            background-color: #1e1e1e !important;
            color: white !important;
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #ff9800;
        }

        /* Placeholder Text */
        div[data-baseweb="input"] input::placeholder {
            color: #bbbbbb !important;
        }

        /* Buttons */
        .stButton>button {
            background-color: #ff9800;
            color: black;
            font-size: 16px;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 20px;
            transition: 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background-color: #ffa726;
            transform: scale(1.05);
        }

        /* Expander */
        .stExpander {
            background-color: #1e1e1e !important;
            border: 1px solid #ff9800;
            border-radius: 10px;
        }

        /* Messages (Success, Warning, Error) */
        .stSuccess {
            background-color: #4caf50;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }

        .stWarning {
            background-color: #ff9800;
            color: black;
            border-radius: 8px;
            padding: 10px;
        }

        .stError {
            background-color: #f44336;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }

        /* Footer */
        .footer {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            color: #bbb;
            font-size: 14px;
        }
    </style>

    <div class="footer">Made with ❤️ by Ahmed</div>
    """,
    unsafe_allow_html=True
)


st.title("Password Strength Checker")

user_input = st.text_input("Enter Your Password",placeholder="Enter Your Password",type="password").strip()

allowed_chars_weak = string.ascii_lowercase + string.digits
allowed_medium_upper = True 
allowed_chars_medium = string.ascii_lowercase + string.digits + string.ascii_uppercase

if st.button("Check Strength", key="btn1"):
    if len(user_input) < 8 and len(user_input) >= 1 and all(c in allowed_chars_weak for c in user_input):
        st.warning("Password is Weak!")

    elif 8 <= len(user_input) <= 12 and any(c.isupper() for c in user_input) and all(c in allowed_chars_medium for c in user_input):
        st.info("Password is Medium!")
    elif 12 < len(user_input) <= 20 and any(c.isupper() for c in user_input) and any(c.islower() for c in user_input) and any(c.isdigit for c in user_input) and any(c in string.punctuation for c in user_input):
        st.success("Password is Strong!")
    elif len(user_input) >= 1:
        st.error("Invalid or Too Long Password, Please Read Instructions!")

    if len(user_input) >= 1:
         with st.expander("🔽Instructions For Improve Your Password"):
            st.subheader("For Strong Password")
            st.write("✔ Use at least **12+ or under or equal to 20 characters**")
            st.write("✔ Include **uppercase, lowercase, numbers, and symbols**")
            st.write("✔ Avoid **common passwords (123456, password, etc.)**")

            st.subheader("For Medium Password")
            st.write("✔ Use at least **8+ or under or equal to 12 characters**")
            st.write("✔ Include **uppercase(mandatory), numbers, and lowercase**")
            st.write("✔ Avoid **common passwords (123456, password, etc.)**")

            st.subheader("For Weak Password")
            st.write("✔ Use under **8 characters**")
            st.write("✔ Include **lowercase, numbers**")
            st.write("✔ Avoid **common passwords (123456, password, etc.)**")


st.title("Strong Password Generator")


length = st.number_input("Enter Password Length (12-20) To Generate Password",placeholder="Enter Password Length (12-20) To Generate Password", min_value=12, max_value=20, step=1)
if st.button("Generate Strong Password"):
    strong_password = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=length))
    st.success(f"Generated Password: {strong_password}")

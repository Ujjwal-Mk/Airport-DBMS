import pickle
from pathlib import Path
import streamlit as st
import time
import streamlit_authenticator as stauth

names = ["Peter Parker","Rebecca Miller"]
usernames = ["pparker","rmiller"]
passwords = ["abc123","def456"]

hashed_passwords = stauth.Hasher(passwords).generate()

# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)

credentials = {"usernames":{}}

for uname,name,pwd in zip(usernames,names,hashed_passwords):
    user_dict = {"name":name,"password":pwd}
    credentials["usernames"].update({uname:user_dict})

authenticator = stauth.Authenticate(credentials, "cookkkie","random_key",cookie_expiry_days=1)

name, authentications_status, username = authenticator.login("Login","main")

# print(authentications_status)

if authentications_status is False:
    error = st.error("Username/password is incorrect")
    time.sleep(2)
    error.empty()

if authentications_status is None:
    st.warning("Please enter Username and password")

if authentications_status:
    st.title(f"Welcome {name}")
    st.write("login successfull!!")
    authenticator.logout("Logout","main")
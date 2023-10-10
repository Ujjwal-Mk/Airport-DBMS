import streamlit as st
import time
import streamlit_authenticator as stauth
import get_keys as gk

def login_user():

    names,usernames,hashed_passwords = gk.get_usr_info()


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
        return (0,authenticator)

    if authentications_status is None:
        warn = st.warning("Please enter Username and password")
        time.sleep(2)
        warn.empty()

    if authentications_status:
        # st.title(f"Welcome {name}")
        # st.write("login successfull!!")
        authenticator.logout("Logout","main")
        return (1,authenticator)
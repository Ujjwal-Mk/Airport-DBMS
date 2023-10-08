import streamlit as st
import time
import streamlit_authenticator as stauth
import get_keys as gk

# def create_user_registration():
#     uname = st.sidebar.text_input("Username")
#     Pass = st.sidebar.text_input("Password", type="password")
#     f_name = st.sidebar.text_input("First Name")
#     minit = st.sidebar.text_input("Middle Initials")
#     l_name = st.sidebar.text_input("Last Name")
#     auth_lvl = st.sidebar.text_input("Authorization Level",value="2") 
#     if st.sidebar.button("Register") and (uname and Pass and f_name and minit and l_name and auth_lvl):
#         gk.add_usr(uname,Pass,f_name,minit,l_name,auth_lvl)
    
def login_user():
    # names = ["Peter Parker","Rebecca Miller"]
    # usernames = ["pparker","rmiller"]
    # passwords = ["abc123","def456"]

    names,usernames,hashed_passwords = gk.get_usr_info()


    # file_path = Path(__file__).parent / "hashed_pw.pkl"
    # with file_path.open("rb") as file:
    #     hashed_passwords = pickle.load(file)
    # print(type(hashed_passwords),type(hashed_passwords[0]))
    credentials = {"usernames":{}}

    for uname,name,pwd in zip(usernames,names,hashed_passwords):
        user_dict = {"name":name,"password":pwd}
        credentials["usernames"].update({uname:user_dict})

    authenticator = stauth.Authenticate(credentials, "cookkkie","random_key",cookie_expiry_days=1)

    name, authentications_status, username = authenticator.login("Login","main")

    # print(authentications_status)

    if authentications_status is False:
        # if st.button("Create account"):
        #     create_user_registration()
        error = st.error("Username/password is incorrect")
        time.sleep(2)
        error.empty()
        return (0,authenticator)

    if authentications_status is None:
        warn = st.warning("Please enter Username and password")
        # if st.button("Create account"):
        #     create_user_registration()

    if authentications_status:
        # st.title(f"Welcome {name}")
        # st.write("login successfull!!")
        authenticator.logout("Logout","option_menu")
        return (1,authenticator)
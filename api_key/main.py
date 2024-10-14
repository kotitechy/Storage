import streamlit as st
from chatbot import chat_bot
from add_history import add_query as aq
from fetch_his import get_history

st.title("Chatbot AI")

# Sidebar for API key and username input
key_input = st.sidebar.text_input("Enter API Key", placeholder="API Key" , type="password",value="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" )
user_input = st.sidebar.text_input("Say what AI should call you", placeholder="User name")

# Initialize session state variables if they don't exist
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user' not in st.session_state:
    st.session_state.user = ""
if 'key' not in st.session_state:
    st.session_state.key = ""

# Handle login process
if st.sidebar.button("login"):
    if not user_input:
        st.sidebar.warning("Please provide both API key and user name." )
    else:
        st.session_state.logged_in = True
        st.session_state.user = user_input
        st.session_state.key = key_input
        st.sidebar.success(f"Welcome {user_input}")

if(st.sidebar.button("Get History")):
    response = get_history(st.session_state.user)
    if(response=='No history Found'):
        st.error("No history Found")
    else:
        st.sidebar.markdown("History")
        for i in response:
            st.sidebar.info(i)


# Main chat interface after login
if st.session_state.logged_in:
    st.success(f"Welcome {st.session_state.user}")
    question = st.text_input("Ask Something from AI", placeholder="Chat Here")
    
    if st.button("Get Response"):
        if not question:
            st.warning("Please enter a question.")
        else:
            try:
                # Use the key and user stored in session state, not the local variables
                response = chat_bot(st.session_state.key,question)
                st.write(f"{st.session_state.user}: {question}")
                st.write(f"AI: {response}")
                aq(question, st.session_state.user)
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.sidebar.warning("Please enter your API key and user name to log in.")

# favicon = ''
# st.beta_set_page_config(page_title='your_title', page_icon = favicon, layout = 'wide', initial_sidebar_state = 'auto')


# def show_his_page():
#     st.tilte()






# if(st.sidebar.button('Register')):
#      with st.form(key='popup_form'):
#         st.write("### Enter your details:")
#         username = st.text_input("Username")
#         email = st.text_input("Email")
#         api_key = st.text_input("API Key", type="password")
        
#         submit_button = st.form_submit_button(label='Submit')

#         if submit_button:
#             with st.modal("open popup"):
#                 print("ok   ")


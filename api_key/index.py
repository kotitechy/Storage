import streamlit as st

host='192.168.56.1'
user='admin'
passwd='11971197'
database='chatbot_ai'

import pymysql as sql

def get_history(username):
    con = None
    try:    
        con = sql.connect(host=host, user=user, passwd=passwd, database=database)
        print('Connection was successful')
        
        cur = con.cursor()
        query = "select query from queries where username=%s;"
        cur.execute(query, username)
        r=cur.fetchall()
        # list of tuples 
        ls=[]
        for i in r:
            for j in i:
                ls.append(j)
        # print(ls)
        return ls
        
    except Exception as e:
        # print("Data insertion failed:", e)
        return "No history Found"
        
    finally:
        if con:
            con.close()
            # print("Connection closed")


def add_query(prompt,username):
    con = None
    try:    
        con = sql.connect(host=host, user=user, passwd=passwd, database=database)
        print('Connection was successful')
        
        cur = con.cursor()
        query = "INSERT INTO queries (query, username) VALUES (%s, %s)"
        cur.execute(query, (prompt, username))
        con.commit()
        # print("Data insertion successful")
        
    except Exception as e:
        print("Data insertion failed:", e)
        
    finally:
        if con:
            con.close()
            print("Connection closed")

def chat_bot(key, question="hi"):

    from huggingface_hub import InferenceClient

    client = InferenceClient(api_key=key)
    response_parts=[]
    for message in client.chat_completion(
    	model="mistralai/Mistral-7B-Instruct-v0.3",
    	messages=[{"role": "user", "content": f"{question}?"}],
    	max_tokens=500,
    	stream=True,
    ):
        # print(message.choices[0].delta.content, end="")
        response_parts.append(message.choices[0].delta.content)
    # Join all parts into a single string
    full_response = ''.join(response_parts)
    return full_response

# key="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"
# model="google-bert/bert-large-uncased-whole-word-masking-finetuned-squad"
# question="who is priminister of india"


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


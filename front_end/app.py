import streamlit as st
import requests
from time import time



def send(text=""):
    headers = {"Content-Type": "application/json"}
    data = {"content": text}
    res = requests.post("http://localhost:8000/chat", json=data, headers=headers)
    response_data = res.json()

    bot_response = response_data["content"]
    source = f"Nguồn: {response_data['source']} - Trang: {response_data['page']}"
    return bot_response, source


st.title("Chat Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        src = message.get("src", "")
        time_res = message.get("time", "")
        print(f"Source_1: {src}")
        if src:
            print("aaaa")
            st.markdown(f"*{src}*")  # Hiển thị nguồn với định dạng in nghiêng
            st.markdown(f"**Time: {round(time_res, 4)}**")  # Hiển thị nguồn với định dạng in nghiêng

message = st.chat_input("Enter here: ")

if message:
    if message:
        st.chat_message("user").markdown(message)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": message})

    s = time()
    response, src = send(message)
    e = time()
    print("Message: ", message)
    print("=> Response: ", response)
    print("=> Source: ", src)
    print("-" * 50)
    with st.chat_message("assistant"):
        st.write(response)
        st.write(src)
        st.write(f"Time: {round(e - s, 4)}")
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response, "src": src, "time": e - s}
    )
    st.rerun()
#################
# st.title("Chatbot Demo")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for msg, src in st.session_state.messages:
#     st.text(msg)
#     if src:
#         st.markdown(f"*{src}*")  # Hiển thị nguồn với định dạng in nghiêng

# user_input = st.text_input("Bạn: ", "")

# if st.button("Gửi") and user_input:
#     response = requests.post("http://localhost:8000/chat", json={"content": user_input})
#     print(response.text)


#     st.session_state.messages.append((f"Bạn: {user_input}", ""))
#     st.session_state.messages.append((bot_response, source))
#     st.rerun()

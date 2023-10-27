import replicate
import streamlit as st

def response2(string_dialogue, prompt_input):
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature": 0.01, "top_p": 0.1, "max_length": 120,
                                  "repetition_penalty": 1})
    return output


def model_response(prompt_input):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    print(string_dialogue)
    print('--------------')
    return response2(string_dialogue, prompt_input)
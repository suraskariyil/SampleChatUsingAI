import streamlit as ui
#from dotenv import load_dotenv
#from openai import OpenAI

ui.set_page_config(
    page_title="SK",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

#load_dotenv()

#openai_client = OpenAI()

ui.title("✈️ Our first travel AI Agent!!")

greeting_message = {"role": "assistant", "content": "👋 Hello! I'm your AI Travel Agent. How can I assist you today?"}

if "message" not in ui.session_state:
    ui.session_state.message = [
        {"role": "system", "content": """
        Assume you are a travel agent. You used to conduct travel programs across the world!!
        Respond the queries within 2-3 sentences. If the user asks for more details, provide them in max 10 lines.
        """
         },
        greeting_message]

prompt = ui.chat_input(greeting_message["content"])

if prompt:
    ui.session_state.message.append({"role": "user", "content": prompt})

    response = openai_client.chat.completions.create(messages=ui.session_state.message, model="gpt-4-turbo",
                                                     temperature=0.7,
                                                     max_tokens=300, stream=False)

    ai_message = response.choices[0].message.content

    ui.session_state.message.append({"role": "assistant", "content": ai_message})

for message in ui.session_state.message[1:]:
    with ui.chat_message(message["role"]):
        ui.markdown(message["content"])
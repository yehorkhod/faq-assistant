# Imports
import streamlit as st
from streamlit_chat import message
from model import chain
from database_interaction import sql_query
from chat_to_json_parser import chat_to_json_parser
from strings import (
    initial_history_user_input,
    initial_history_ai_response,
    initial_user_input,
    initial_ai_response
)
from database_initialize import DATABASE_URI


def response(query: str) -> str:
    result = chain({
        'question': query,
        'chat_history': st.session_state['history']
    })
    st.session_state['history'].append((query, result['answer']))

    return result['answer']


def rerun() -> None:
    st.session_state['history'] = [(
        initial_history_user_input,
        initial_history_ai_response
    )]
    st.session_state['user'] = [initial_user_input]
    st.session_state['ai'] = [initial_ai_response]
    st.rerun()


st.title('Frequently Asked Questions🦜💡')


# Session state initialization
if 'history' not in st.session_state:
    st.session_state['history'] = [(
        initial_history_user_input,
        initial_history_ai_response
    )]

if 'user' not in st.session_state:
    st.session_state['user'] = [initial_user_input]

if 'ai' not in st.session_state:
    st.session_state['ai'] = [initial_ai_response]

# Container for the chat history
response_container = st.container()
# Container for the user's text input
container = st.container()


# Question asking functionality
with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_input(
            'Question:',
            placeholder='Ask me something!',
            key='input'
        )
        column_1, column_2 = st.columns([11, 1])

        with column_1:
            submit_button = st.form_submit_button(label='Send')

        with column_2:
            rerun_button = st.form_submit_button('🔁')

    if submit_button and user_input:
        output = response(user_input)

        st.session_state['user'].append(user_input)
        st.session_state['ai'].append(output)

    if rerun_button:
        # Saving conversation into the database
        chat_json = chat_to_json_parser(st.session_state['history'])
        sql_query(
            DATABASE_URI,
            (
                'INSERT INTO conversations (conversation) VALUES (%s);',
                (chat_json,)
            )
        )
        rerun()

# Messages pop-up
if st.session_state['ai']:
    with response_container:
        for i in range(len(st.session_state['ai'])):
            message(
                st.session_state['user'][i],
                is_user=True,
                key=str(i) + '_user',
                avatar_style='big-smile'
            )
            message(
                st.session_state['ai'][i],
                key=str(i),
                avatar_style='thumbs'
            )

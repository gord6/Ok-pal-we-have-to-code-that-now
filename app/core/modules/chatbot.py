import os

import flask_login
import openai
import modules._db.prompts as db_prompts
import modules.users as users


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def _load_prompts():
    user_id = flask_login.current_user.id
    task = users.get_current_task()[0]
    return db_prompts.load_prompt_history(user_id, task)


def number_of_tokens(messages):
    return sum([len(prompt["content"]) + 10 for prompt in messages])


def _get_chat_history():
    prompts = _load_prompts()
    prompts.sort(key=lambda p: p[0])

    messages = []

    for prompt in prompts:
        messages.append({"role": "user", "content": prompt[1]})
        messages.append({"role": "assistant", "content": prompt[2]})

    return messages


def call_chatgpt_api(messages):

    return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, stream=True)


def generate_messages(msg):
    messages = _get_chat_history()
    messages.append({"role": "user", "content": msg})

    # shorten history to be less than 4000 tokens
    for i in range(len(messages)):
        if number_of_tokens(messages[i:]) < 4000:
            messages = messages[i:]
            break

    return messages



def get_response(messages):
    return call_chatgpt_api(messages)

# Imports
import json


def chat_to_json_parser(chat: list[tuple[str, str]]) -> str:
    chat_dicts = [{'Користувач': message[0], 'Асистент': message[1]} for message in chat]
    return json.dumps(chat_dicts)

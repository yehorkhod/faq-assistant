# Imports
import json


def chat_to_json_parser(chat: list[tuple[str, str]]) -> str:
    chat_dicts = [{'User': message[0], 'Assistant': message[1]} for message in chat]
    return json.dumps(chat_dicts)

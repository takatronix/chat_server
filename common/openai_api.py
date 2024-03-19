import json
import os

from openai import OpenAI


class OpenAIAPI:
    def __init__(self, config):
        if isinstance(config, str) and os.path.isfile(config):
            with open(config, 'r') as file:
                self.config = json.load(file)
        else:
            self.config = config

        self.client = OpenAI(api_key=self.config['api_key'])

    def ask(self, message, history):

        messages = [{
            "role": "system",
            "content": self.config["system"]
        }]

        if history:
            messages.extend(history)

        messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model=self.config['model'],
            max_tokens=self.config['max_tokens'],
            temperature=self.config['temperature'],
        )
        return chat_completion.choices[0].message.content

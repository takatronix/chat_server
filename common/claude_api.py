import json
import os

import anthropic


class ClaudeAPI:
    def __init__(self, config):
        if isinstance(config, str) and os.path.isfile(config):
            with open(config, 'r') as file:
                self.config = json.load(file)
        else:
            self.config = config
        self.client = anthropic.Anthropic(api_key=self.config['api_key'])

    def ask(self, message, history):
        messages = []
        if history:
            messages = history
        messages.extend(
            [
                {
                    "role": "user",
                    "content": message
                }]
        )
        try:
            response = self.client.messages.create(
                model=self.config['model'],
                max_tokens=self.config['max_tokens'],
                temperature=self.config['temperature'],
                top_p=self.config['top_p'],
                system=self.config['system'],
                messages=messages
            )
        except Exception as e:
            print(e)
            return "エラーが発生しました"

        return response.content[0].text

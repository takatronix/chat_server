import json


class Session:
    messages = []

    def __init__(self, session_name):
        self.load_history(session_name)
        self.name = session_name

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def save_history(self):
        with open(f"history/{self.name}.json", "w", encoding='utf-8') as file:
            json.dump(self.messages, file, ensure_ascii=False, indent=4)

    def clear_history(self):
        self.messages = []

    def load_history(self, session_name):
        try:
            self.messages = []
            with open(f"history/{session_name}.json", "r", encoding='utf-8') as file:
                self.messages = json.load(file)
        except FileNotFoundError:
            self.messages = []
        except json.decoder.JSONDecodeError:
            self.messages = []

import json
import os

from session import Session


class Settings:
    version = "1.0.0beta"
    profiles = {}
    sessions = {}

    # 後ろからcount個のメッセージを取得
    def get_history(self, name, count):
        session = self.get_session(name)
        return session.messages[-count:]

    def get_session(self, name):
        if name not in self.sessions:
            self.sessions[name] = Session(name)
        return self.sessions[name]

    def __init__(self):
        self.profiles = load_profiles()


def load_profiles():
    # profiles.jsonをメモリに入れる
    with open("config/profiles.json", "r", encoding='utf-8') as file:
        _profiles = json.load(file)

    # プロフィールのモデルタイプを取得
    for profile_name in _profiles:
        profile = _profiles[profile_name]
        json_path = "config/models/" + profile['model'] + ".json"
        with open(json_path, "r", encoding='utf-8') as file:
            profile['config'] = json.load(file)

        config = profile['config']
        model_type = config['model_type']

        # APIキーがmodel.jsonにない場合は環境変数から取得
        if 'api_key' not in config:
            if model_type == "openai":
                config['api_key'] = os.environ['OPENAI_API_KEY']
            if model_type == "groq":
                config['api_key'] = os.environ['GROQ_API_KEY']
            if model_type == "claude":
                config['api_key'] = os.environ['CLAUDE_API_KEY']

        # プロフィールの設定をmodel.jsonに反映
        if 'temperature' in profile:
            config['temperature'] = profile['temperature']
        if 'system' in profile:
            config['system'] = profile['system']
        if 'max_tokens' in profile:
            config['max_tokens'] = profile['max_tokens']
        if 'top_p' in profile:
            config['top_p'] = profile['top_p']
    return _profiles

import json
import time

from common.claude_api import ClaudeAPI
from common.groq_api import GroqAPI
from common.openai_api import OpenAIAPI


class LanguageModel:
    def __init__(self, config_file):

        # config_fileが文字列なら、ファイルを読み込む、JSON形式でconfigに格納
        if isinstance(config_file, str):
            with open(config_file, 'r') as file:
                self.config = json.load(file)
        else:
            self.config = config_file

        # model_type に応じて、APIクライアントを生成
        self.model_type = self.config['model_type']
        if self.model_type == 'groq':
            self.api_key = self.config['api_key']
            self.client = GroqAPI(self.config)
        if self.model_type == 'claude':
            self.client = ClaudeAPI(self.config)
        if self.model_type == 'openai':
            self.client = OpenAIAPI(self.config)

    def ask(self, message, history=None):

        # 開始時刻を記録
        start_time = time.time()
        if self.model_type == 'groq':
            result = self.ask_groq(message, history)
        elif self.model_type == 'claude':
            result = self.ask_claude(message, history)
        elif self.model_type == 'openai':
            result = self.ask_openai(message, history)
        else:
            raise Exception(f"Model type {self.model_type} not supported")

        # 経過時間を計算
        lapse_time = time.time() - start_time
        # 経過時間を小数点以下１桁で表示
        lapse_time = round(lapse_time, 1)
        # モデル名:[経過時間]　result を表示
        model = self.config['model']
        temperature = self.config['temperature']
        # 経過時間と結果を表示
        print(f"{self.model_type}:{model}[{temperature}]({lapse_time}) {result}")

        return result, lapse_time

    def ask_groq(self, message, history):
        return self.client.ask(message, history)

    def ask_claude(self, message, history):
        return self.client.ask(message, history)

    def ask_openai(self, message, history):
        return self.client.ask(message, history)

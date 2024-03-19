import json
import os
import shutil

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from settings import Settings
from endpoints.chat import get_chat_router
from endpoints.version import get_version_router


def init_folders():
    # audioフォルダを削除して作成
    os.makedirs("audio", exist_ok=True)
    os.makedirs("history", exist_ok=True)
    shutil.rmtree("audio")


# =============================================================================
# メイン処理
init_folders()
load_dotenv()

settings = Settings()
app = FastAPI()

app.include_router(get_chat_router(settings))
app.include_router(get_version_router(settings))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

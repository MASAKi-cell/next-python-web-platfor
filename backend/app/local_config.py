import os
from dotenv import load_dotenv
from os.path import join, dirname

load_dotenv(verbose=True)  # ファイルが見つからない場合は警告を出力する
dotenv_path = join(dirname(__file__), ".env")  # 絶対パスの取得
load_dotenv(dotenv_path)
local_pass = os.environ.get("ORIGIN")

# syntax=docker/dockerfile:1
FROM python:3.10.12
WORKDIR /app

# コンソール出力
ENV PYTHONUNBUFFERED 1

# 依存関係のインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードのコピー
COPY . .

# アプリケーションの起動
CMD ["python", "main.py"]
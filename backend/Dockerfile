# syntax=docker/dockerfile:1

# --- ビルドステージ ---
FROM python:3.10.13-slim AS builder
WORKDIR /app

# ログを出力
ENV PYTHONUNBUFFERED 1

# 依存関係をインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー
COPY . .

# --- 実行ステージ ---
FROM python:3.10.13-slim AS runtime
WORKDIR /app

# ビルドステージからPython依存関係をコピー
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

# 環境変数を設定
ENV PATH=/root/.local:$PATH

CMD ["python", "app/main.py"]
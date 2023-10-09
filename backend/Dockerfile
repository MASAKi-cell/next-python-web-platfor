# syntax=docker/dockerfile:1
FROM Python:3.10.12
WORKDIR /app

# 依存関係のインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードのコピー
COPY . .

# アプリケーションの起動
CMD ["python", "main.py"]
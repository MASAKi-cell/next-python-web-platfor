# syntax=docker/dockerfile:1
FROM node:16.14.2
WORKDIR /app

# 依存関係のインストール
COPY package*.json ./
RUN npm install

# ソースコードのコピー
COPY . .

# アプリケーションのビルド
RUN npm run build

# コンテナ起動時の実行コマンド
CMD ["npm", "dev"]
# syntax=docker/dockerfile:1

# # base image
FROM node:20.9.0-bookworm-slim as base
WORKDIR /src

# development for local
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
CMD ["npm", "run", "dev"]

# build
FROM base AS builder
COPY --chown=node:node . .
USER node
RUN npm install --loglevel warn
RUN npm run build
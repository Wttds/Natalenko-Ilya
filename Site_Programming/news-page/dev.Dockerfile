FROM node:16 AS builder

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install
RUN apk update && apk update openssl

COPY . .

RUN npm run build

FROM node:16 AS runner

WORKDIR /app

RUN npm install --production

ENV NODE_ENV=production

CMD ["npm", "start"]
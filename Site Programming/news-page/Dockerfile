FROM node:16 AS builder

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

RUN npm run build

FROM node:16 AS runner

WORKDIR /app

RUN npm install --production

ENV NODE_ENV=production

CMD ["npm", "start"]
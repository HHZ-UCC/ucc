FROM node:12.16.0-stretch-slim

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
COPY . .

ENV PORT=8080

EXPOSE 8080

CMD [ "node", "index.js" ]
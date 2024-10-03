FROM node:18-alpine

WORKDIR /react-docker-app/

COPY ./react-docker-app/public/ /react-docker-app/public
COPY ./react-docker-app/src/ /react-docker-app/src
COPY ./react-docker-app/package.json /react-docker-app/

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]
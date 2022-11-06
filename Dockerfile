FROM node:latest
# Create the bot's directory
RUN mkdir -p /user/src/bot
WORKDIR /user/src/bot

COPY package.json /user/src/bot

RUN npm install

COPY . /user/src/bot

# Start the bot.
CMD [ "node", "index.js" ]

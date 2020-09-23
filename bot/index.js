// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

const dotenv = require('dotenv');
const path = require('path');
const restify = require('restify');

// Import required bot services.
// See https://aka.ms/bot-services to learn more about the different parts of a bot.
const { BotFrameworkAdapter } = require('botbuilder');

// This bot's main dialog.
const { AdaptiveCardsBot } = require('./src/adaptiveCardBots');
// Import required bot configuration.
const ENV_FILE = path.join(__dirname, '.env');
dotenv.config({ path: ENV_FILE });

// Create HTTP server
const server = restify.createServer();
server.use(restify.plugins.bodyParser({ mapParams: true }));

server.listen(process.env.port || process.env.PORT || 3978, () => {
    console.log(`\n${ server.name } listening to ${ server.url }`);
    console.log('\nGet Bot Framework Emulator: https://aka.ms/botframework-emulator');
    console.log('\nTo talk to your bot, open the emulator select "Open Bot"');
});

// Create adapter.
// See https://aka.ms/about-bot-adapter to learn more about how bots work.
const adapter = new BotFrameworkAdapter({
    appId: '612bcf63-a526-417b-96b0-aafdddd37286',
    appPassword: 'Ign9Qk4e.0s6E_zo-DL7~Q7_HsiP6fJk7U',
    channelService: process.env.ChannelService,
    openIdMetadata: process.env.BotOpenIdMetadata
});

// Catch-all for errors.
adapter.onTurnError = async (context, error) => {
    // This check writes out errors to console log .vs. app insights.
    // NOTE: In production environment, you should consider logging this to Azure
    //       application insights.
    console.error(`\n [onTurnError] unhandled error: ${ error }`);

    // Send a trace activity, which will be displayed in Bot Framework Emulator
    await context.sendTraceActivity(
        'OnTurnError Trace',
        `${ error }`,
        'https://www.botframework.com/schemas/error',
        'TurnError'
    );

    // Send a message to the user
    await context.sendActivity('The bot encounted an error or bug.');
    await context.sendActivity('To continue to run this bot, please fix the bot source code.');
};

const conversationReferences = {};
// Create the main dialog.
const myBot = new AdaptiveCardsBot(conversationReferences);

// Listen for incoming requests.
server.opts('/api/messages', (req, res) => {
});

server.post('/api/messages', (req, res) => {
    adapter.processActivity(req, res, async (context) => {
        // Route to main dialog.
        await myBot.run(context);
    });
});

server.post('/api/notify', async (req, res) => {
    console.log('request received');
    const body = req.body;
    console.log(body);

    for (const conversationReference of Object.values(conversationReferences)) {
        adapter.continueConversation(conversationReference, async turnContext => {
            await turnContext.sendActivity(myBot.getCard(body));
            // await myBot.run(turnContext);
        });
    }
    res.setHeader('Content-Type', 'text/html');
    res.writeHead(200);
    res.write('<html><body><h1>Message received.</h1></body></html>');
    res.end();
});

server.get('/public/*', restify.plugins.serveStatic({
    directory: __dirname
}));

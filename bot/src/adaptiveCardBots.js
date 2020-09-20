// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

const { ActivityHandler, CardFactory, TurnContext } = require('botbuilder');
const axios = require('axios');

// Import AdaptiveCard content.

const host = process.env.HOST;
const services_url = `https://${host}/services/registry/bot/action`
const WELCOME_TEXT = 'This bot will introduce you to Adaptive Cards. Type anything to see an Adaptive Card.';

const callBotAction = async (url, body) => {
    try {
        const headers = {
            'Content-Type': 'application/json'
        };
        const response = await axios.post(url, JSON.stringify(body), {
            headers: headers
        });
        const data = response.data;
        console.log(data);
        return data;
    } catch (error) {
        console.log(error);
    }
};

class AdaptiveCardsBot extends ActivityHandler {
    constructor(conversationReferences) {
        super();
        this.conversationReferences = conversationReferences;

        this.onConversationUpdate(async (context, next) => {
            this.addConversationReference(context.activity);
            await next();
        });
        this.onMembersAdded(async (context, next) => {
            const membersAdded = context.activity.membersAdded;
            for (let cnt = 0; cnt < membersAdded.length; cnt++) {
                if (membersAdded[cnt].id !== context.activity.recipient.id) {
                    await context.sendActivity(`Welcome to Adaptive Cards Bot  ${ membersAdded[cnt].name }. ${ WELCOME_TEXT }`);
                }
            }
            await next();
        });
        this.onMessage(async (context, next) => {
            this.addConversationReference(context.activity);
            const handleMessageResult = await this.handleMessage(context.activity);
            const { card } = handleMessageResult;
            await context.sendActivity(this.getCard(card));
            await next();
        });
    }

    async handleMessage(activity) {
        const userId = activity.from.id;
        // activity.value:
        // {
        //     target : 'http://',
        //     payload: {
        //         type: 'assign_task'
        //     }
        // }
        const userName = activity.from.userName;
        console.log(`Receivied message from user ${ userId } : ${ userName }`);
        if (this.isUndefined(activity.text)) {
            const target = activity.value.target;
            const payload = activity.value.payload;
            const user = {
                id: activity.from.id,
                name: activity.from.name
            };
            const requestBody = {
                payload: payload,
                user: user
            };
            console.log(`Going to call target endpoint ${ target } with body ${ JSON.stringify(requestBody) }`);
            const cardResponse = await callBotAction(target, requestBody);

            if (cardResponse) {
                return {
                    data: {},
                    card: cardResponse
                };
            }
        } else {
            const cardResponse = await callBotAction(services_url, {});
            return {
                data: {},
                card: cardResponse
            };
        }
    }

    isUndefined(prop) {
        return typeof prop === 'undefined';
    }

    getCard(data) {
        return {
            attachments: [CardFactory.adaptiveCard(data)]
        };
    }

    addConversationReference(activity) {
        const conversationReference = TurnContext.getConversationReference(activity);
        this.conversationReferences[conversationReference.conversation.id] = conversationReference;
    }
}

module.exports.AdaptiveCardsBot = AdaptiveCardsBot;

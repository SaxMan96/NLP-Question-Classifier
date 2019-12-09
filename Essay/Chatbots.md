<img src="https://cambiodigital-ol.com/wp-content/uploads/2019/07/chatbot.jpg" alt="chatbot" style="zoom:150%;" />

## What is a chatbot?

A chatbot is a computer program with which it is possible to have a conversation, whether we want to ask for some type of information or to carry out an action. These conversational agents are mimicking a human speech simulating a conversation or interacting with the user. Nowadays chatbots are the new standard in UI (User Interface) that allows interacting with the system like with another human, which brings a new quality to many services. 

## Why are they getting so popular?

One of the biggest advantages of chatbots is that they can be integrated parts of the website interface (Facebook Messenger, Slack) or some device (Google Assistant, Alexa), where you don't need to download and update them like standard applications. Another is that it is a very universal interactive tool with as many applications as we can think of. The most popular use case is customer services where they playing the same role as real worker communicating with the customer asking and answering questions and more beyond, keeping the conversation more human-like.

> In this report, **give your opinion**, key takeaways, and **conclusions** on the topics covered during the session. You can focus on a particular topic or a few of them. **Relate them with other fields you find could be applied**, give your own contributions with other techniques you know and you believe chatbots could benefit from, or discuss about **pros&cons of the techniques discussed during the session.**  Regardless the topic you choose, I will highly value your own contributions, discussion, and reasoning. 

> ----------------------------------------------------------------------------------------
>
> - [ ] Relate them with other fields you find could be applied
>
> - [ ] give your opinion
>
> - [ ] key takeaways
>
> - [ ] conclusions
>
> - [ ] techniques you know and you believe chatbots could benefit from

##  NLP based chatbots

There are two kinds of chatbots:

- **Rule-based chatbots** - based on keywords they find in input to recognize the question.
- **AI-powered chatbots** - this one uses AI and NLP to plan a conversation to be more natural. More intelligent chatbots are able to plan a series of questions to narrow the subject and deliver a more suitable response. Of course, they are a more interesting topic to talk about.

The core of the AI-powered chatbot system is natural language processing (NLP). Every text entered by the user is parsed to interpret and identifies what the user meant, and determine a set of responses based on this information and previous context. Chatbots are the most complex systems from a linguistic point of view because they contain:

- **Dialog** -  every response of chatbot system is supposed to be in  human-like dialog manner.

- **Refinement** -  leading conversation to point where topic is narrow enough for system to find the right answer.

- **Off-topic conversations** -  being able to interact with questions not related to purpose of the system and ever diverse by itself.

- **Variables detection & memory** - remembering important facts and structuring this information for future use.

- **Speech processing** - chatbots are often connected with speech recognition and generation systems.

  ![comix](https://assets.amuniversal.com/f424e7e00ef301346782005056a9545d)

## Knowledge Base

Knowledge Base is the most essential source of information that chatbot works with, it provides information that is required to accurately respond to the user.

<img src="https://wordstream-files-prod.s3.amazonaws.com/s3fs-public/styles/simple_image/public/images/chatbots-how-chatbots-work.jpg?dkshmERs6WijeCK_6klYsRlV1PbJcym8&amp;itok=_zeJfzK5" style="zoom: 67%;" />

You can imagine it as a list of Favorite Asked Questions (FAQs) that chatbot search to find answers to most common questions. Integrating this with Data Store can give us quite easy to use UI to interact with data-based systems where chatbot serves to present data in a handy way. It might seem simple. There are many other kinds of bases that can extend this system.

- **Learn Knowledge Base** is an extension to Knowledge Base. Maintained by the client, less structured association of keywords with forced by clients matching. This simple module often helps to improve the system without using advanced methods.

- **ML Base** is where the fun begins. It assumes the system holds a history of user entries, consider user rating of system performance using simple like/dislike or 1-10 scale. Used in more extreme cases, where knowledge base didn't bring any answer. 

- **Popularity Base** step forwards from ML Base which tries to simplify the user input by clustering different questions that were meant to receive the same information from the system. Popularity Base tries to track trends of user questions and model this behavior into some more general cases.

In this architecture, any base can be replaced with bases combination, which means that different results from different bases may be combined/merged. This approach allows to create modular system that is more transparent and explainable thus easier to manage.

If you need to create a chatbot that serves the first level of communication with your company, you need to create a proper knowledge base. It won't know what are you opening hours this Christmas or how to make a complaint. It might be overwhelming at first, but start with a few questions and grow from there.

![list](https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1052&q=80)

## Known problems

**Related questions** - we can ask the same question in multiple ways *"How to get to post office", "Where to send a letter"* or *"Post box nearby"*. To deal with it you need training data with bunch of related sentences phrases or even keywords to teach you chatbot to generalize better.

**Unanswered questions** - every system, especially at the beginning of its production phase, has a lot of questions that cannot be found in the main knowledge base and other sources. What you need to do is to gather those questions, find similarities in them and add records to your KB that will contain the proper information.

**Questions that needs to be answered by human** - some questions have to be answered by real responder, and the problem here is not to train chatbot to answer all the questions, but to detect ones that need to be held by a human.

**Efficiency** - chatbots are expected to work in real-time, but Knowledge Bases tend to be a huge document. In order to search such large sets, indexation can be helpful. Indexation creates a data structure that accelerates recovery operations in a database table at the cost of additional records and disk space. I think we should take into account that some words are more common than others. One of the indexation techniques that exploit this property in NLP is TF-IDF, which informs about the frequency of occurrence of terms, taking into account the proper balance of the meaning of the local term and its meaning in the context of the full collection of documents. 

**Typos and text correction** -  Everyone makes mistakes, but humans are able to understand even the most misspelled text, but for a machine its a hard task. Luckily typos can be fixed easily with few tools. Most basic technique relays on finding similar words based a threshold on [Levenshtein distance](http://levenshtein distance/) to accept correction. There are more techniques (Selection Mechanism, Language Model, etc.) Like always a hybrid of these techniques works the best. Here you can find some example of those methods [Spell Correction](http://norvig.com/spell-correct.html).

## Answer generation and understanding

**Natural Language Generation (NLG)** - Based on the query and structured data that the chatbot has, the answer should be prepared in a clear and unambiguous way for the user. The response templates work well, but for more sophisticated responses, it's worth adapting the language to the message. The typical stages of natural-language generation are:

- **Content determination**: Deciding what information to mention in the text.
- **Document structuring**: General organization of information to be provided.
- **Aggregation**: Combining similar sentences to improve readability and naturalness. 
- **Lexical choice**: Putting words to the concepts. 
- **Referring expression generation**: Creating referring expressions that identify objects and regions.
- **Realization**: Creating the actual text, which should be correct according to the rules of syntax, morphology, and orthography.

In order for a bot to perceive a text, it needs a well-structured data representing a sentence. The NLU was created for this purpose.

![NLU&NLG](https://miro.medium.com/max/700/0*CssYMxCpdhLWxISD)

**Natural Language Understanding (NLU)** is one of the biggest AI challenges. Decomposing unstructured input into a structure that the computer can understand. For human it's very natural to understand the intention despite small misspellings, shortcuts, swapped words or colloquialisms, but machines need more structured data. 

- **Distributional** approaches are using machine and deep learning and perform semantic tasks really well. These systems are broad and scalable, but they don't include a true understanding of the real meaning of sentences. These NLP algorithms analyze syntactic based on correlation, contextual dependencies, and part-of-speech tagging n text. 

  I think that these models will be able to deduct a language model based on enough data and proper models. Humans among the world use similar structures to describe the world, each language has nouns, verbs, adjectives and other parts-of-speech that means some kind of general rules were present in the process of creating a language. If only we will be able to model one language we will be able to model them all.

-  **Model Theoretical** approach assumes that language refers to the real world, thus we can model it. Understanding of language is it's strong point, but with a very limited scope. How does it work? For example:

  *What is the longest Asia bridge?* &rarr; `argmax(Bridges in Asia) `&rarr;*Danyang–Kunshan Grand Bridge*

	This approach is requiring a mathematical model created by experts, giving deep understanding in a narrow fields. But I think that if we will use language model in a simple form (binary search tree or sequence) it will be possible to train an encoder to automate the modeling process and use model-theoretical methods in a wider scope.

- **Frame-based** approach, where the sentence is deconstructed into a tabular form. For example sentence "Greg needs access to the database" can be represented as a request transaction.

    | OUTPUT    | INPUT    |
    | --------- | -------- |
    | REQUESTOR | Greg     |
    | REQUEST   | Access   |
    | OBJECT    | Database |

	From one side this method is just representing input text in more selective and labeled structure, but from the other this method requires supervision, rules have to be created by experts, but frame-based approach is much simpler than model-theoretical because here we have tabular data, and with enough representation, we will be able to represent (not model) input data in more structured form. This can be done using a lot of data, but with the use of tools like [Mechanical Turk](https://www.mturk.com/) it doesn't need to take ages.
	
- **Reinforcement learning** - this paradigm assumes that we have an environment in which our system is trained. The process of training consist of iterative simulations in which agents perform their tasks and then are evaluated. There is no training and testing data, only simulation that allows a parameterized model to perform their task. In NLP RL simulator can be an interactive system, where users can play a cooperative game where he can ask and answer questions and model tries to improve its score.

    ![RL](https://miro.medium.com/max/1816/1*c3pEt4pFk0Mx684DDVsW-w.png)

    I think that this kind of approach is really what learning a language is about. When we were kids there were no language lessons, we've started talking by the age of four. We have learned only by listening and mimicking what our parents do. The only evaluation was by giving a good example, no grammar rules. Good environment and enough users to play with are key to success.
    

## What about GDPR?

When we collect personal data using a chatbot, please note that we are responsible for it in accordance with GDPR. If your company wants to support the password change procedure, it cannot do so using a chatbot on Facebook Messenger. It should be implemented on your own website so that you can be sure that the data will remain only in your company. A person consenting to the processing of personal data should be able to withdraw his consent in an easy way as he has given. According to GDPR, it is not possible to collect user data for the future and back it up. This must be taken into account when creating applications.

However, there are many techniques that help to protect personal data. Pseudonymization assumes that personal data can't be linked to a single data object, without the use of additional data. This data should be kept separate to make it hard to link a piece of data to someone's identity. Here are some of the pseudonymization techniques:

- **Scrambling** is about obfuscation the characters, changing the order of letters in a reversible way.
- **Masking** allows you to cover part of the data while still retaining its uniqueness. This is often the case when hiding a piece of a credit card number, which is enough for the system or user to identify it.
- **Tokenization** is about replacing private data with token with no extrinsic or exploitable meaning or value. The resulting token is always the same for the same input, so analytical correlations are still possible.
- **Hashing** function assigns any large number a short number, always having a fixed size, non-specific, quasi-random value, the so-called irreversible shortcut. The resulting hash is always the same for the same input so that analytical correlations are still possible.
- **Encryption** consists in encoding the data using a special decryption key, which should also be stored separately. 

Even though there are plenty of techniques it's always a good idea to consult your data security with an expert in security domain or even a lawyer. AI ethics is a questionable topic, and now even the most advanced algorithms can behave unpredictably. A set of regulations to control chatbot is a must 

## Chatbot frameworks

Starting from scratch will definitely teach you a lesson, but to create something scalable being able to put on a production you need to use a framework. A lot of IT giants have their own systems: Amazon Lex, Microsoft LUIS, and IBM Watson. I will focus on free solutions from Google and Facebook.

**Dialogflow** is a Google-owned company developing human-computer interaction technologies based on natural language conversations. The company is best known for creating Google Assistant, a chatbot for mobile devices that performs tasks and answers users’ questions in a natural language. Dialogflow has API that allows creating lighter chatbots using a simple Intent-Action interface. Below is an example of the use of this API in Node.js 

```javascript
const WELCOME_INTENT = 'Default Welcome Intent';
const NUMBER_INTENT = 'Input Number';
const NUMBER_ARGUMENT = 'num';

// you can add a fallback function instead of a function for individual intents
app.fallback((conv) => {
  // intent contains the name of the intent
  // you defined in the Intents area of Dialogflow
  const intent = conv.intent;
  switch (intent) {
    case WELCOME_INTENT:
      conv.ask('Welcome! Say a number.');
      break;

    case NUMBER_INTENT:
      const num = conv.arguments.get(NUMBER_ARGUMENT);
      conv.close(`You said ${num}`);
      break;
  }
});
```

Dialogflow supports learning new commands similar to those already implemented in the system. It also provides a user interface that helps developers create intentions, entities, and agents. Diagflow has a user-friendly development interface and documentation with a lot of pre-built agents, which combines with one-click integration makes it really easy to use.

**Facebook Wit** is are meant to create a voice interface for hands-free apps for cocking, working out and home automation. Wit allows transferring voice commands to the JSON structure format (example below).

```python
import wit
wit.init()
resp = wit.text_query('Turn on the light', 'MY_WIT_TOKEN')
print('Response: {}'.format(resp))
wit.close()
```

```json
{ 
   "confidence":0.979   "intent":"lights"   "_text":"Turn on the light"   "entities":{ 
      "on_off":[ 
         { 
            "value":"on"
         }
      ]
   }
}
```

Wit allows you to see and edit the conversation tree, and distinguish different roles for members of the conversation. It has a visual chat UI for testing conversations. Wit supports more than 50 languages, so it's a great thing to introduce chatbots to your project.

## How to introduce chatbot to business

Let's assume that your business needs a chatbot to send boarding passes, shipping updates, after purchase opinion gathering or simple promotional messages. There are many tools to deal with it on a business level. Using SMS or an email is prehistoric today. Marketing requires a new channel of communication - like mobile chats - to be involved. 

<img src="https://www.revenueriver.co/hs-fs/hubfs/Business%20functions%20that%20will%20most%20benefit%20from%20chagots-Source%20ReviewKiss-chatbot-booming.png?width=900&amp;name=Business%20functions%20that%20will%20most%20benefit%20from%20chagots-Source%20ReviewKiss-chatbot-booming.png" style="zoom:80%;" />

Most of the big chatbot systems require a person called **botmaster**, who knows both how a company works, and how to introduce that information to a chatbot. Updating a Knowledge Base is one of his tasks. You can train one of your employees to become a botmaster or you can outsource such a person from your chatbot supplier. The second option is more popular and companies are ready to provide such person, to know your business and operate a chatbot system for you. 

There are plenty of ready solutions, that help to create a chatbot system even without programming. Chatfuel, Manychat, FlowXO, Octane, and Recime are just a few of them. Let's look at other examples.

**MobileMonkey** - Chatbots became so popular that you can create conversational chats without even writing a single line of code. Solutions like MobileMonkey allows creating Mobile Marketing chat on Facebook Messenger that more or less automates the direct marketing process with a really high-level designing tool that shows how popular it is. 

<img src="https://www.androidsis.com/wp-content/uploads/2016/07/yahoo-bots.jpg" style="zoom: 67%;" />

**Smooch** is another tool that makes Business To Client (B2C) approach to be easier. WhatsApp distributes a Docker container that contains an API client. Smooch takes care of maintaining, databases and changing WhatsApp AIP and gives its own API. This allows connecting your business with a client with such an elegant way as WhatsApp chat.

![](https://docs.smooch.io/images/whatsapp-architecture2.png)

## What is the future of chatbots

I think that the general concept of chatbots will diversify and there will appear a lot of specialized tools that will be merged with our everyday utilities. What will you find more attractive a fridge or a talking fridge, that will buy your groceries online? The question answers itself.

The main problem when using computer by the ordinary user is that he doesn't understand it and doesn't know how to tell the computer what to do. The development in UI is unstoppable, and it's only a matter of time when we will be able to communicate with a computer just like with other humans. 

The way we are communicating with others seems the easiest and the most natural, but there is other way of information transfer, that's more faster and almost independent of language we are using. Method that's even hard to understand by us. Our thoughts. Even today science is not sure how our brain is working, how information is stored and passed. Doesn't it sounds like a challenge for AI?
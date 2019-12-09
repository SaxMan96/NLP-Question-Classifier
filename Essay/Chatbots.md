![chatbot](https://www.prospectfactory.com.mx/wp-content/uploads/2018/08/chatbot-interaccion-1024x500.png)



## What is chatbot?

A chatbot is a computer program with which it is possible to have a conversation, whether we want to ask for some type of information or to carry out an action. These conversational agents are mimicking a human speech simulating a conversation or interacting with user. Nowadays chatbots are new standard in UI (User Interface) that allows to interact with with the system like with other human, which brings a new quality to many services. 

## Why are they getting so popular?

One of the biggest advantages of chatbots is that they can be integrated parts of website interface, where you don't need to download and update them like standard applications. Other is that it is very universal interactive tool with as many applications as we can think of. The most popular use case is customer services where they playing the same role as real worker communicating with customer asking and answering questions and more beyond, keeping the conversation more human-like

## Two kinds of chatbots

- **Rule-based chatbots** - they are based on keywords they find in question to recognize question.
- **AI-powered chatbots** - this one use AI and NLP to plan a conversation to be more natural. More intelligent chatbots are able to plan a series of question to narrow the subject and deliver more suitable response. Of course they are more interesting topic to talk about.

> Siri, Cortana, Facebook Messenger Telegram Slack 

> In this report, **give your opinion**, key takeaways, and **conclusions** on the topics covered during the session. You can focus on a particular topic or a few of them. **Relate them with other fields you find could be applied**, give your own contributions with other techniques you know and you believe chatbots could benefit from, or discuss about **pros&cons of the techniques discussed during the session.**  Regardless the topic you choose, I will highly value your own contributions, discussion, and reasoning. 
>
> - [x] answer generation, - NGU NLU  Hardcoded i lingwistki
> - [x] the role of the bot master,  - wynajmują ludzi i ogólny osftware
> - [ ] typos and corrections, - levergian distance 
> - [x] the NLU module - corpus, i ma strukture i intencji, 
> - [ ] distributional semantics and disambiguation, -  
> - [ ] indexation - TF-IDF w którym pytaniu jes jakie słowo i sprawdzją w jaich pytaniech i indeksują
> - [x] FAQs
> - [x] knowledge bases
> - [ ] GDPR - RODO -  obfuscation
> - [ ] Relate them with other fields you find could be applied
> - [ ] give your opinion
> - [ ] key takeaways
> - [ ] conclusions
> - [ ] techniques you know and you believe chatbots could benefit from

##  How do they work?

The core of every chatbot system is natural language processing (NLP). Every text entered by user is parsed in order to to interpret and identifies what the user meant, and determine a set of responds based this information and previous context. Chatbots are the most complex systems from a linguistic point of view, because they contain:

- **Dialog** -  every response of chatbot system is supposed to be in  human-like dialog manner.
- **Refinement** -  leading conversation to point where topic is narrow enough for system to find the right answer.
- **Off-topic conversations** -  being able to interact with questions not related to purpose of the system and ever diverse by itself.
- **Variables detection & memory** - remembering important facts and structuring this information for future use.
- **Speech processing** - chatbots are often connected with speech recognition and generation systems.

![comix](https://assets.amuniversal.com/f424e7e00ef301346782005056a9545d)

## Knowledge Base

Knowledge Base is the most essential source of information that chatbot works with, it provides information that are required to accurately respond to the user.

<img src="https://wordstream-files-prod.s3.amazonaws.com/s3fs-public/styles/simple_image/public/images/chatbots-how-chatbots-work.jpg?dkshmERs6WijeCK_6klYsRlV1PbJcym8&amp;itok=_zeJfzK5" style="zoom: 67%;" />

You can imagine it as a list of Favorite Asked Questions (FAQs) that chatbot search in order to find answers to most common questions. Integrating this with Data Store can give us quite easy to use UI to interact with data based systems where chatbot serves for presenting data in handy way. It might seems simply, but there are a lot of other kinds of Bases.

- **Learn Knowledge Base** is an extension to Knowledge Base, which is maintained by client less structured association of key words with forced by clients matching. This simple module often helps to improve system without using sophisticated methods.

- **ML Base** is where fun begins. It that assumes that system holds history of user entries, consider user rating of system performance using simple like/dislike or 1-10 scale. It is used in more extreme cases, where knowledge base didn't bring any answer. 

- **Popularity Base** step forwards from ML Base which tries to simplify the user input by clustering different questions that were meant to receive same information from system. Popularity Base tries to track trends of user questions and model this behavior into some more general case.

In this architecture any base can be replaced with a combination of bases, which means that different results from different bases may be combined/merged. This approach allows to create modular system that is more transparent and explainable thus easier to manage.

If you need to create a chatbot that serves the first level of communication with your company, you need to create proper knowledge base. It won't know what are you opening hours this Christmas or how to make a complaint. It might be overwhelming at first, but start with a few questions and grow from there.

![list](https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1052&q=80)

## Known problems

**Related questions** - we can ask the same question in multiple ways *"How to get to post office", "Where to send a letter"* or *"Post box nearby"*. To deal with it you need training data with bunch of related sentences phrases or even keywords to teach you chatbot to generalize better.

**Unanswered questions** - every system, especially at the beginning of its production phase, has a lot of questions that cannot be found in main knowledge base and other sources. What you need to do is to gather that questions, find similarities in them and add records to your KB that will contain proper information.

**Questions that needs to be answered by human** - some questions has to be answered by real responder, and the problem here is not to train chatbot to answer all the questions, but to detect ones that needs to be held by human.

## Answer generation and understanding

Natural Language Understanding (NLU) is one of biggest AI challenge. Decomposing unstructured input into a structure that computer can understand. For human it's very natural to understand the intention despite of small misspellings, shortcuts, swapped words or colloquialisms, but machines requires more structured data. 

- **Distributional** approaches are using machine and deep learning and perform semantic tasks really well. This systems are broad and scalable, but they don't include true understanding of real meaning of sentences. These NLP algorithms analyze syntactics based on correlation, contextual dependencies and part-of-speech tagging n text. 

  I think that these models will be able to deduct language model based on enough data and proper model. Humans among the world use similar structures to describe world, each language has nouns, verbs, adjectives and other parts-of-speech that means some king of general rules were present in process of creating a language. If only we will be able to model one language we will be able to model them all.

-  **Model Theoretical** approach assumes that language refer to the real world, thus we can model it. Understanding of language is it's strong point, but with a very limited scope. How it works? For example:

  *What is the longest Asia bridge?* &rarr; `argmax(Bridges in Asia) `&rarr;*Danyang–Kunshan Grand Bridge*

	This approach is requiring mathematical model created by experts, giving deep understanding in narrow field. But I think that if we will use language model in a simple form (binary search tree or sequence) it will be possible to train an encoder to automate modeling process and use model-theoretical methods in wider scope.

- **Frame-based** approach, where sentence is deconstructed into a tabular form. For example sentence "Greg needs access to database" can be represented as a request transaction.

    | OUTPUT    | INPUT    |
    | --------- | -------- |
    | REQUESTOR | Greg     |
    | REQUEST   | Access   |
    | OBJECT    | Database |

	From one side this method is just representing input text in more selective and labeled structure, but from the other this method requires supervision, rules have to be created by experts, but frame-based approach is much simpler than model-theoretical because here we have tabular data, and with enough representation we will be able to represent (not model) input data in more structured form. This can be done using a lot of data, but with use of tools like [Mechanical Turk](https://www.mturk.com/) it doesn't need to take ages.
	
- **Reinforcement learning** - this paradigm assumes that we have an environment in which out system is trained. Process of training consist of iterative simulations in which agents performs their tasks and then are evaluated. There is no training and testing data, only simulation that allows a parametrized model to perform their task. In NLP RL simulator can be a interactive system, where user can play an cooperative game where user can ask and answer questions and model tries to improve its score.

    ![RL](https://miro.medium.com/max/1816/1*c3pEt4pFk0Mx684DDVsW-w.png)

    I think that this kind of approach is really what learning a language is about. When we were kids there was no language lessons, we've started talking by the age of four. We have learnt only by listening and mimicking what our parents does. The only evaluation was by giving a good example, no grammar rules. Good environment and enough users to play with are key to success.
    
    ![baby](https://images.unsplash.com/photo-1557939574-a2cb399f443f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)

## Pomysły

Where are they - messenger - if you ask on fb

## Chatbot frameworks

[Chatfue](https://chatfuel.com/)l, [Manychat](https://manychat.com/), [FlowXO](https://flowxo.com/), [Octane](https://octaneai.com/), [Recime](https://recime.io/) - bez kodzenia

Google Dialogflow, Amazon Lex , Microsoft LUIS, Facebook Wit and IBM watson - z kodzeniem



## Articles

https://chatbotslife.com/how-to-create-an-intelligent-chatbot-in-python-c655eb39d6b1

https://chatbotslife.com/chatbots-the-importance-of-chatbots-in-every-business-bf178bc9cfef

## Wit - easy to use development tool 

Tools like [Wit](wit.ai) are meant to create voice interface for hands-free apps for cocking, working out and home automation. Wit allows to transfer voice commands to json structure format.

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



## How to introduce chatbot to business

Lets assume that you business needs a chatbot to send boarding passes, shipping updates, after purchase opinion gathering or simple promotional messages. There are many tools to deal with it on business level. Using SMS or an email is prehistoric nowadays. Marketing requires new channel of communication - like mobile chats - to be involved. 

<img src="https://www.revenueriver.co/hs-fs/hubfs/Business%20functions%20that%20will%20most%20benefit%20from%20chagots-Source%20ReviewKiss-chatbot-booming.png?width=900&amp;name=Business%20functions%20that%20will%20most%20benefit%20from%20chagots-Source%20ReviewKiss-chatbot-booming.png" style="zoom:80%;" />

​																		Source - [Review Kiss](https://reviewkiss.com/2017-year-chatbot-booming/)

Most of big chatbot systems requires a person called bot master, who knows both how company works, and how to introduce that information to chatbot. Updating a Knowledge Base is one of his tasks. You can train one of your employees to become bot master or you can outsource such a person from your chatbot supplier. Second option is more popular and companies are ready to provide such person, to know your business and operate chatbot system for you.

Chatbots became so popular that you can create conversational chats without even writing a single line of code. Solutions like [MobileMonkey](https://www.youtube.com/watch?time_continue=30&v=oC1LaUfNV18&feature=emb_logo) allows to create Mobile Marketing chat on Facebook Messenger that more or less automates the direct marketing process with really high level designing tool shows how popular it is. 

<img src="https://www.androidsis.com/wp-content/uploads/2016/07/yahoo-bots.jpg" style="zoom: 67%;" />

[Smooch](www.smooch.io) is another tool that makes Business To Client (B2C) approach to be easier. WhatsApp distributes a Docker container that contains an API client. Smooch takes care of militainment, databases and changing WhatsApp AIP and gives its own API. This allows to connect you business with client with such elegant way as WhatsApp chat.

![](https://docs.smooch.io/images/whatsapp-architecture2.png)

## What is the future of chatbots

I think that really general concept of chatbots will diversify and there will appear a lot of specialized tools that will be merged with our everyday utilities. What will you find more attractive a fridge or a talking fridge,that will buy your groceries online? The question answers itself.

Main problem when using computer by ordinary user is that he doesn't understand it and doesn't know how  to tell computer what to do. The development in UI is unstoppable, and it's only a matter of time when we will be able to communicate with computer just like with other human. 

The way we are communicating with others seems the easiest and the most natural, but there is other way of information transfer, that's more faster and almost independent of language we are using. Method that's even hard to understand by us. Our thoughts. Even nowadays science are not sure how our brain is working, how information is stored and passed. Doesn't it sounds like a challenge for AI?
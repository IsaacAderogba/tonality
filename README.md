# Using text classification to predict the formality of a sentence

Being able to classify a text as formal or not has positive applications for text retrieval, document editing, and chatbot interactions. To that effect, this experiment prototyped a formality classifier capable of categorizing sentences as either formal or not formal.

[Using text classification to predict the formality of a sentence](https://www.craft.do/s/WsWRw1rIeSCR0B)

[Tonality](https://github.com/IsaacAderogba/tonality)

----

#### Background

[Dementieva et al.(2022)](craftdocs://open?blockId=AFB0DFB6-168A-4755-9192-5FCBD09F99E7&spaceId=64060bdd-99e7-b943-6365-b986ef291ff8) outline that formality classifiers can be used for a variety of tasks: For text retrieval, such a classifier could be used for filtering search results based on the level of desired formality; For document editing, the classifier could be used for flagging either highly formal or informal language. For conversational agents, the classifier could be used for filtering candidate responses to select the one that matches the level of formality in the conversation.

To further solidify the importance of formality, [Pavlick and Tetreault (2016)](craftdocs://open?blockId=1CB8317A-B475-4577-8C48-680BF8EE79E2&spaceId=64060bdd-99e7-b943-6365-b986ef291ff8) cite that formality is capable of subsuming other stylistic dimensions, such as politeness, impartiality, and intimacy.

To build a foundation for these use cases, this experiment prototypes a formality classifier that can identify whether a given sentence is of a casual or formal nature.

#### Approach

In order to classify sentences as either casual or formal, I finetuned a distilled version of the BERT model. [Dementieva et al. (2022)](craftdocs://open?blockId=AFB0DFB6-168A-4755-9192-5FCBD09F99E7&spaceId=64060bdd-99e7-b943-6365-b986ef291ff8) note that case sensititivty preserves important formality information which led me to adopt the *cased* version of the BERT model.

The data used was gathered by [Pavlick and Tetreault (2016)](craftdocs://open?blockId=1CB8317A-B475-4577-8C48-680BF8EE79E2&spaceId=64060bdd-99e7-b943-6365-b986ef291ff8). In their study, they measured formality across genres of news, blogs, emails, and answers with a scale that ranged from -3.00 to 3.00. For the purposes of text classification, scores greater than 0 were ranked as formal while those less than 0 were ranked as casual.

#### Outcome

By the end of training, the formality classifier had an F1 score of 0.82. When visualizing the result in a confusion matrix, we can see that the model performs better at classifying formal sentences.

![matrix.png](https://res.craft.do/user/full/64060bdd-99e7-b943-6365-b986ef291ff8/doc/C69C4E72-CF72-4657-88F3-43B6159CEEE0/6304613A-D6CD-4D56-9186-0123C6866594_2/McHPGaQiEI88emF1QZ0GLLuSpbNjvuncp1CqtCybAdYz/matrix.png)

The high accuracy could also be due to the model developing a tendency for classifying sentences as formal. Drawing from the dataset gathered from [Pavlick and Tetreault (2016)](craftdocs://open?blockId=1CB8317A-B475-4577-8C48-680BF8EE79E2&spaceId=64060bdd-99e7-b943-6365-b986ef291ff8), we can see that formal sentences were longer than casual sentences, on average.

![dataset.png](https://res.craft.do/user/full/64060bdd-99e7-b943-6365-b986ef291ff8/doc/C69C4E72-CF72-4657-88F3-43B6159CEEE0/DDBFBA82-FC76-49E3-9AB8-DF3349D5B44E_2/0KX7rWAJRsDLZxyRg1QWE302DN0NEO5xWVL6tkg2NHgz/dataset.png)

Nonetheless, these results serve as a useful foundation for future work I’ll be doing on Natural Language Processing. The end goal would be to build an agent that complements the AI assistant Grammarly.


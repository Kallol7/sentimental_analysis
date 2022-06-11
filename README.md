# Sentimental analysis from reviews of USA beaches 
Cohere,an nlp tool/platform is used to determine how good its generic/baseline model works on reviews of USA beaches.
## Inspiration
The inspiration was I wanted to stay relavant to theme. I am familier with computer vision. But I have always avoided it before.So,I wanted to try out NLP this time.
## What it does
It takes a sentence which is a review of an USA beach and determines whether it is positve,negative or neutral review.
## How I built it and the challenges
Cohere platform has already some generic/baseline model for nlp. We just "finetune" it to perform it better on specific task. In our case it is a classification task. To make it work we need to provide it reviews about beach and their corresponding sentiment. But I had to work with the baseline model due to unforseen circumstances. Firstly,I collected the reviews and saved them in excel file.Then I converted it to a csv file with all my input. The texts in the csv file was too long for the algorithm to I truncated some of the long texts using excel. The data was collected from reviews available in public.

To be sure that the input represents the overall data I had to make sure I provide the model with enough data from broad range, from very negative reviews to positive reviews. Some of the reviews were even hard to categorize between negative vs. neutral. 272 reviews were used to measure the performace.

At first I decided to try the finetuning model. After exhausting myself collecting all the data I realizes the previous 2 finetunes I ran (following the tutorial on doc) wasn't ready. They were stuck on queue. So I had no way proceed further. After some time it came to my mind why don't I test out the performace of the generic(/basline) model available on cohere. I tweaked my code again, then 2 more problems occured. One,there is a limit for text size for new users in cohere & the other one is that maximum number of input can't be more than 32. I adjusted my code to solve these two problems simultaneously. My code was working, I ran it and then the next problem: even using more then  input at a time caused internal server error. After some trial & error I found 10 input at a time works good. 

Finally,overcoming all these restrictions I was able to hack my way into achieve my goal.
** :) **

## Accomplishments that we're proud of
I used a library to achieve my task which I am not used to doing overnight. The more time passed the complex the code became. Managing it along with the challanges was not easy task. I'm proud of overcoming it.
## What I learned
I learned how to hide API keys. Although I was familier with git, this one was new to me.
 Also, I learned not to be overwhelmed by a task before even diving into it. Actully doing it might make it a lot more simpler. 
## What's next for Sentimental analysis from reviews on USA beaches
What I have done is implemented a tool. But I am fascineted by it. My next step would be to learn about the theoritical aspects of natural language processing. The algorithm can be better by adding more data and refining the model considering the confidence value of the the prediction.

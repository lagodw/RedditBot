# RedditBot

This repo contains code used to create https://single-actor-322702.uk.r.appspot.com/. 

# Methodology

The model is a combination of fine tuned [GPT2](https://huggingface.co/transformers/model_doc/gpt2.html) and [BERT](https://huggingface.co/transformers/model_doc/bert.html) models. The models are trained on data scraped from reddit, code used to scrape the data can be found in the reddit_scrape notebook.

## Data Format

The data is created as pairs of comments based on the reddit thread. For any deep comment, it is paired with the parent comment that it is replying to. For any top level comment (i.e. a comment replying directly to the initial post), the initial post is used as the parent comment. In the case where a post does not contain any text (i.e. a post with only a picture), the title is instead used as the parent comment. Additionally, the subreddit is included at the start of the parent text in order to provide additional context to the model.

## Model Structure

The model is a two stage model. The first stage is to generate predictions from a fine tuned GPT2 model. The model is trained on the combination of subreddit, parent comment, and child comment, with the goal to predict each subsequent word in the sequence. 

The second stage is a fine tuned BERT model for next sentence classification, with the goal to predict whether the child comment is associated with the parent comment. The same data as the GPT2 model is used, however, the data is supplemented by random pairings of parent and child comments in order to provide the negative cases.

For predictions, a subreddit, parent comment, and optional beginning prompt for the child comment is supplied to the GPT2 model and the top 5 generated responses are recorded. Those responses are then fed into the BERT model, which evaluates the probability of each response being paired with the supplied parent comment. The results are sorted by the predicted probability and the response with the highest probability is chosen.

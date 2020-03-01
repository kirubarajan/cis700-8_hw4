# Fine-Tuning GPT-2 For Natural Language Generation
> Arun Kirubarajan & Jacob Beckerman

## Part 1
### Compute the perplexity of test and validation sets according to GPT-2 without fine-tuning and according to GPT-2 with finetuning. Does perplexity go down after fine-tuning?

Perplexity without fine-tuning to presidential speeches: 
```
27.0704402923584 is the perplexity of /content/presidential_speeches_valid.txt according to gpt2-medium

23.510801315307617 is the perplexity of /content/presidential_speeches_test.txt according to gpt2-medium
```

Perplexity with fine-tuning to presidential speeches: 
```
19.99014663696289 is the perplexity of /content/presidential_speeches_valid.txt according to /content/drive/My Drive/finetuned_models/presidential_speeches/checkpoint-3000

18.390100479125977 is the perplexity of /content/presidential_speeches_test.txt according to /content/drive/My Drive/finetuned_models/presidential_speeches/checkpoint-3000
```

Thus, it is clear that fine-tuning to the test set does lower the perplexity.

### Generate at least 100 samples from GPT-2 with fine-tuning and 100 without fine-tuning. Compute the word (or token) overlap of the generated text with the text in the test set. Which set of generated sentences has more words in common with the text in the test set? Is this what you expected?

todo

### The provided code uses top-k with k=50 for generation. Experiment with different sampling strategies and observe how this impacts the quality and diversity of the generations. If you’d like, implement a measure of text diversity such as self-BLEU or dist-1 (the number of unique generated words divided by the total number of generated words), and plot how it changes as you vary the value of either temperature, k, or p.

todo

## Part 2
### (same question as Part 1)

Perplexity without fine-tuning to tweets: 
```
111.16755676269531 is the perplexity of /content/tweets_valid.txt according to gpt2-medium

111.76993560791016 is the perplexity of /content/tweets_test.txt according to gpt2-medium
```

Perplexity with fine-tuning to tweets: 
```
26.263174057006836 is the perplexity of /content/tweets_valid.txt according to /content/drive/My Drive/finetuned_models/vc_tweets/checkpoint-200

26.507057189941406 is the perplexity of /content/tweets_test.txt according to /content/drive/My Drive/finetuned_models/vc_tweets/checkpoint-200
```

Thus, it is clear that fine-tuning to the test set does lower the perplexity.

### Generate at least 100 samples from GPT-2 with fine-tuning and 100 without fine-tuning. Compute the word (or token) overlap of the generated text with the text in the test set. Which set of generated sentences has more words in common with the text in the test set? Is this what you expected?

todo

### The provided code uses top-k with k=50 for generation. Experiment with different sampling strategies and observe how this impacts the quality and diversity of the generations. If you’d like, implement a measure of text diversity such as self-BLEU or dist-1 (the number of unique generated words divided by the total number of generated words), and plot how it changes as you vary the value of either temperature, k, or p.

I increased the temperature to 1.5 and got samples that look like this:

```
\paulg- Do things with data have to be more like life than software? Check out our free eBook today for 20 questions questions &g… 

\paulg- No such things as moral judgment to deal in a way that matters; I wish this could just happen for the good of the community rather than being a thing that's only achieved in theory. The world of the future...we could do better: 

\paulg- A long overdue but good idea by @GavinAtielsen to add my name to "Goddamn to have on your team." #scalability👋 
```

The generated outputs are noticably less sensible and very diverse in their vocabulary, as well as tweet structure (e.g. including hashtags and emojis).

Decreasing the temperature to 0.5 has the opposite effect, where each tweet was a little mundane (and shorter):

```
\paulg- I love the idea of this... and I think it will be a great idea for a startup. 

\paulg- I'm surprised we haven't done this before. 

\paulg- I'm an engineer. I'm also a social media evangelist. 
```

The sentence structure is also noticably less varied (e.g. "I ___ ." )  

Resetting the temperature to 1 and setting `k=25` yielded the following results:

```
\paulg- You can see a bit of a pattern here; the more you work on a project the more things you learn about it. The same is true in life as in business, and the less we do, and the faster we work with… 

\paulg- The biggest problem about technology is when it's all the same. That's an old joke. But the technology in the first 20 years of the internet has been very different. 

\paulg- I'd like to see a lot more people from the tech community take this as an opportunity to learn how to become an entrepreneur, as opposed to as just a VC, and try to… 
```

With a value of `k=75`:

```
\paulg- "A great start in an exciting field? Make sure it's a good one. If not, you could be running a startup in the dark." - @joshk- 

\paulg- One hour and 35 minutes into your flight, you still don’t have enough time in your day for a great meal. You’re being driven crazy. 

\paulg- It takes a village to raise an army. 

```

Seems like a lower value of k causes the model to generate text that is more on topic than a higher value of k.

### Describe your new dataset and how you collected it. Why do you think it is an interesting dataset? What are the sizes (in megabytes) of your train, validation, and test files? Copy some text from the dataset into your report to give us a sense of what it looks like.

Our dataset consists of tweets from venture capitalists and other tech "thinkers". We thought it would be funny since such Twitter users typically . Our training file is roughly 1 megabyte and the our test and validation files are roughly 0.5 megabytes. This is rather small of a dataset since tweets are generally very short in length (~140 characters) and most users tweet only around a few thousand times.

I also pre-pend (as per Daphne's reccomendation) each tweet with the author's username so I can do some pseudo-conditioning during generation to tweet like a specific user.

### Copy some of the text generated by the finetuned model into your report. Is it as good as you hoped? What are some problems you notice with it?

Some examples from avid tweeter Paul Graham:

```
\paulg- For this reason, you should be very careful when you take a company public, and never bet against the idea that you need to raise the price to make money. 

\paulg- You're a fucking liar if you're not a feminist 

\paulg- One of the most important things that I've learned from my mentor Richard Mair is that you don't have to make a company special to make money. 

\paulg- The worst way to learn new skills is to work at someone who is not ready for the job. 
```

These tweets sound good, and they tend to stay on the topic of entrepreneurship, but as see in the second tweet, it often generates tweets that sound nothing like Paul. This could be because of the slight transfer learning effect (the username pre-fix), or because the dataset is too small, so the generated text resembles the original training text better than the fine-tuning set.

### Did you have to tweak any of the flags passed to run_language_modeling.py to get finetuning working on your datasret? If so, which ones did you have to change?

Since the dataset was small, sometimes checkpoints weren't saved so I changed the `save_every` flag. I also messed around with the gradient accumulation parameter, but it was unclear to me how it was affecting performance so I reverted to the notebook's default value. I also doubled the number of epochs, but I noticed this caused the generated text to model the fine-tuning dataset a bit too closely, so I reverted back to a single epoch.

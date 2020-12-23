# stream-sources

This is a project to collect real-time news updates from a variety of sources and stream them out as a JSON firehose. The receiving end of the pipe can render the articles out as a news aggregate to replace native news apps or collect them in a database for future analysis.

## This fork has two significant changes:

1) Multithreaded streams.  Reduces latency so you wait less for your updates.

2) Color coding according to a sentiment score.  There are two keyword files - for "positive" and "negative" strings, with a numeric score.  In the default setup, positive scores are green and negative scores are red.  You can customize the sentiments and colors anyway you want.  Really, anything.  You can set up your RSS for NSFW feeds and make your schwing pink and non-schwing yellow if that's how you want your software to work...

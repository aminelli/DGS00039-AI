import feedparser

NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")

print ('Number of RSS posts :', len(NewsFeed.entries))

entry = NewsFeed.entries[1]
print ('Post Title :',entry.title)

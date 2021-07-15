import nltk
nltk.download('punkt')
from textblob import TextBlob
from newspaper import Article

url = ''

article = Article(url)
article.download()
article.parse()
article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

analysis = TextBlob(article.text) #sentiment analysis
print(analysis.polarity)
print(f'Sentiment: {'positive if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}')
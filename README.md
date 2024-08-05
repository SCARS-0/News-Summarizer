# News-Summarizer
A Python-based application that fetches news articles, generates concise summaries, and performs sentiment analysis. Utilizing Natural Language Processing (NLP) techniques, this tool provides quick insights into the main points and emotional tone of the news, supporting better information consumption and decision-making.

# Working-of-the-project:
tkinter for gui

nltk (natural language tool kit) (just using to download a model)

from textblob import textblob (processing textual data) (helps to carry out sentiment anly)

from newspaper import article (to gather information from the web and scrape multiple URLs) Article extracts useful information from article of newspaper

for these libraries to work we need to install libraies by pip install nltk pip install newspaper3k pip install textblob

article = Article(url) # we create article object of newspaper library focused on url article.download() # download the article article.parse() # dissecting the article into the part that it needs article.nlp() # apply natural language processing

these three libraries do all the work for us Now in the newspaper library, we use its modules like Authors, Publication date, Summary to just display the following contents

nltk.download('punkt') # its a token that divides text into list of sentences by an unsupervised algorithm to build a model for words that start sentence, abbreviation words,etc

SENTIMENT ANALYSIS: analysis = Textblob(article.text) print(analysis.polarity)
f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

we used analysis as an object to store all the text in it and to further appply sentiment analysis, we printed the polarity of the the whole text (which is based on the words used in the article, depending on' that we set a condition if the polarity is above 0 its postivie if below 0 its negative and otherwise its neutral

GUI PART

root = tk.Tk() # constructor root.title("News summarizer") # this is the title of the gui window root.geometry('1200x600') # geometry of window

tlabel = tk.label(root, text="title") tlabel.pack() # just creates a label on gui window

title = tk.text(root, height = 1, width = 100) title.config(state=disabled, bg = '#dddddd') title.pack() # just creates a box like a text box but its disabled

Similarly we create labels and boxes for all the required descriptions in the gui like authors, publication date, sentiment analysis and we just keep the configuration of the url as defualt because that needs to be interactive and user must be able to paste the url in the box. Configurations are set to default by not mentioning the .congif part and deleting the whole line of code for that

btn = tk.Button(root, text = "Summarize", command = summarize) # this command links the button directly with function btn.pack() # for creating button

root.mainloop() # method on main window which we execute when we ant to run applications

Now to add functionality to button we create a function and put all the parsing and downloading code over there.

LINKING PART: (its done in the function)

url = utext.get('1.0','end').strip() #we specify start and endpt of a text of a textbox to get the url pasted by user strip get rid of inline characters title.delete('1.0', 'end') title.insert('1.0', article.title)

author.delete('1.0', 'end') # we delete everything in text box and paste the processed data in the boxes author.insert('1.0', article.authors)

pdate.delete('1.0', 'end') pdate.insert('1.0', article.publish_date)

summary.delete('1.0', 'end') summary.insert('1.0', article.summary)

analysis = TextBlob(article.text) sent.delete('1.0', 'end') sent.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

this code performs sentiment analysis by displying polarity and concluding if text is positive, negative or neutral

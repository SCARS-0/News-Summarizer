import nltk
import tkinter as tk
from newspaper import Article
from textblob import TextBlob

def summarize():

    url = utext.get('1.0', "end").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    pdate.config(state='normal')
    summary.config(state='normal')
    sent.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    pdate.delete('1.0', 'end')
    pdate.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sent.delete('1.0', 'end')
    sent.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    pdate.config(state='disabled')
    summary.config(state='disabled')
    sent.config(state='disabled')


# USER INTERFACE
root = tk.Tk()
root.title("News summarizer")
root.geometry('1200x600')

# Title section
tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

# Author section
alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

# Publication date section
plabel = tk.Label(root, text="Publication date")
plabel.pack()

pdate = tk.Text(root, height=1, width=140)
pdate.config(state='disabled', bg='#dddddd')
pdate.pack()

# Summary section
slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# Sentiment section
selabel = tk.Label(root, text="Sentiment analysis")
selabel.pack()

sent = tk.Text(root, height=1, width=140)
sent.config(state='disabled', bg='#dddddd')
sent.pack()

# URL section
ulabel = tk.Label(root, text="Enter URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

# Button
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()


root.mainloop()
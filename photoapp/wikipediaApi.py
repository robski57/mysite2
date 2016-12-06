import wikipedia
def summary(article):
    summary_list = []
    if article is None:
        article = wikipedia.random()
    if article is not None:
        summary = wikipedia.summary(article)
        summary_list.append(summary)
    return summary_list
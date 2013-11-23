import models

def convert_keyword(keyword):
    return models.Keyword(keyword = keyword)

def convert_author(author):
    return models.Author(author = author)

def convert_article(article_page):
    authors = map(convert_author, article_page.authors or [])
    keywords = map(convert_keyword, article_page.keywords or [])
    return models.Article(title = article_page.title,
                          journal = article_page.journal,
                          abstract = article_page.abstract,
                          publisher = article_page.publisher,
                          issn = article_page.issn,
                          year = article_page.year,
                          url = article_page.url,
                          authors = authors,
                          keywords = keywords)


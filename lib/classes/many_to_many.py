class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable and cannot be changed.")

    @staticmethod
    def get_all_articles():
        return Article.all


class Author:
    def __init__(self, name):
        self._name = name
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name is immutable and cannot be changed.")

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles.append(article)
        return article

    def get_topic_areas(self):
        return list(set(article.magazine.category for article in self.articles))


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name is immutable and cannot be changed.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise AssertionError(f"Expected str for category, got {type(value).__name__}.")
        if len(value) == 0:
            raise AssertionError("Category cannot be an empty string.")
        self._category = value

    def add_article(self, article):
        self.articles.append(article)

    def get_contributors(self):
        return list(set(article.author for article in self.articles))

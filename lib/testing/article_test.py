import pytest
from classes.many_to_many import Article, Author, Magazine

class TestArticle:
    def test_title_is_immutable_str(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        
        with pytest.raises(AttributeError):
            article.title = 500

    def test_get_all_articles(self):
        Article.all = []
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")
        assert len(Article.get_all_articles()) == 2

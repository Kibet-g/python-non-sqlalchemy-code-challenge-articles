import pytest
from classes.many_to_many import Author, Magazine

class TestAuthor:
    def test_name_is_immutable_string(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)

        with pytest.raises(AttributeError):
            author_1.name = "ActuallyTopher"

    def test_add_article(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = author.add_article(magazine, "How to wear a tutu with style")
        assert article.title == "How to wear a tutu with style"
        assert article.magazine == magazine
        assert article.author == author

    def test_topic_areas(self):
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_2, "NYC Architecture")
        topics = author.get_topic_areas()
        assert len(topics) == 2

    def test_topic_areas_are_unique(self):
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_1, "Fashion in NYC")
        topics = author.get_topic_areas()
        assert len(topics) == 1

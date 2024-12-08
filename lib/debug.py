#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Creating sample objects for debugging
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    magazine1 = Magazine("Science Daily", "Science")
    magazine2 = Magazine("Tech Monthly", "Technology")

    article1 = Article(author1, magazine1, "Breaking News in Science")
    article2 = Article(author1, magazine2, "Tech Innovations")
    article3 = Article(author1, magazine1, "New Discoveries in Science")
    article4 = Article(author2, magazine1, "Latest Science Trends")
    article5 = Article(author2, magazine2, "AI in Daily Life")
    article6 = Article(author1, magazine2, "More Tech Innovations")

    # Debugging output
    print(author1.articles())  # Test articles
    print(author1.magazines())  # Test magazines
    print(magazine1.contributors())  # Test contributors
    print(magazine1.article_titles())  # Test article titles
    print(author1.topic_areas())  # Test topic areas
    print(magazine2.contributing_authors())  # Test contributing authors

    # Don't remove this line, it's for debugging!
    ipdb.set_trace()

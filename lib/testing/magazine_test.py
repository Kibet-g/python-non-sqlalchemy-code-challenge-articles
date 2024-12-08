import pytest
from classes.many_to_many import Magazine, Author

class TestMagazine:
    def test_name_is_mutable_string(self):
        magazine = Magazine("Vogue", "Fashion")
        assert isinstance(magazine.name, str)
        with pytest.raises(AttributeError):
            magazine.name = "New Yorker"

    def test_name_len(self):
        magazine = Magazine("Vogue", "Fashion")
        assert 2 <= len(magazine.name) <= 16
        with pytest.raises(AttributeError):
            magazine.name = "New Yorker Plus X"

    def test_category_is_mutable_string(self):
        magazine = Magazine("Vogue", "Fashion")
        assert isinstance(magazine.category, str)
        magazine.category = "Lifestyle"
        assert magazine.category == "Lifestyle"

        with pytest.raises(AssertionError):
            magazine.category = 2

    def test_category_len(self):
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.category != ""
        with pytest.raises(AssertionError):
            magazine.category = ""

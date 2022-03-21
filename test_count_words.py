"""
We write all tests for count_words.py here
"""
# pylint: disable=C0303
# pylint: disable=R0903
# pylint: disable=R0201

import pytest
from count_words import WordCounter

class TestWordCounter:
    
    """
    This is the test class to implement all tests 
    from the class WordCounter
    """

    def test_empty_string(self):
    
        """
        Testing an empty string
        """
        words = ""
        assert WordCounter(words).count_words() == 0
    
    def test_single_word(self):
        """
        Test if we can count a single word
        """
        words = "mitun"
        assert WordCounter(words).count_words() == 1
    
    def test_multiple_words(self):
        """
        Test if we can count multiple words
        """
        words = "Test if we can count multiple words"
        assert WordCounter(words).count_words() == 7

    def test_string_with_empty_space(self):
        """
        Testing if we can count zero words in a string
        with empty space
        """
        words = " "
        assert WordCounter(words).count_words() == 0
    
    def test_symbols(self):
        """
        Test symbols in a string
        """
        words = "$$^&@) I an in this bootcamp %*@$"
        assert WordCounter(words).count_words() == 5
    
    def test_linebreaks(self):
        """
        Test for linebreaks
        """
        words = "Test\nfor\nlinebreaks"
        assert WordCounter(words).count_words() == 3
    
    def test_html_text(self):
        """
        Test if we can read html
        """
        words = "<h1> Testing for html text </h1>"
        assert WordCounter(words).count_words() == 4
    
    def test_html_text_without_attributes(self):
        """
        Test if we can count words in a html text 
        that contains some attributes
        """
        words = '<h1 class="Mitun"> Testing for html text </h1>'
        assert WordCounter(words).count_words() == 4
    
    def test_text_with_hyphens(self):
        """
        Test hyphens in between words
        """
        words = "test-hyphens-in-between-words"
        assert WordCounter(words).count_words() == 5
    
    def test_wrong_data_type(self):
        """
        We want to test wrong data type
        """
        words = {"words": "My name is Joseph"}
        with pytest.raises(Exception) as error:
            WordCounter(words).count_words()
        assert "word string must be of type string" in str(error.value)

# Test Parameterization: We want to run multiple tests at once:



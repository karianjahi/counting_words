"""
We write all tests for count_words.py here
"""
# pylint: disable=C0303
# pylint: disable=R0903
# pylint: disable=R0201

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
    
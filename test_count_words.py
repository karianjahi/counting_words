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

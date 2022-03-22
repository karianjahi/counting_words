"""
This is the module that counts words
We want to write in a OOP style.
"""
# pylint: disable=C0303
# pylint: disable=R0903
# pylint: disable=E0401

import re
from bs4 import BeautifulSoup
class WordCounter:

    """
    This is a class that has all methods to count
    words
    """

    def __init__(self, word_string):
        """
        Constructor method: we give a string
        for the class to process
        """
        assert isinstance(word_string, str), "word string must be of type string"
        self.word_string = word_string
    
    def count_words_now(self):
        """
        This is the method that actually counts the words
        """
        self.run_string_through_html_filter()
        self.word_string = re.sub('[^A-Za-z0-9]+', ' ', self.word_string)
        word_splits = self.word_string.split()
        return len(word_splits)

    def run_string_through_html_filter(self):
        """
        Running the string through bs4 so that we can
        extract the text in case the text is entrapped
        within html
        """
        soup = BeautifulSoup(self.word_string, features="html.parser")
        if len(soup.find_all()) > 0:
            self.word_string = soup.get_text()

if __name__ == "__main__":
    SENTENCE = "Daniel wolf"
    print(WordCounter(SENTENCE).count_words())

    MYSTRING = "$$^&@) I an in this bootcamp %*@$"
    CLEANED = re.sub('[^A-Za-z0-9]+', ' ', MYSTRING)
    print(CLEANED)

    #words = "<h1> Testing for html text </h1>"
    WORDS = "Testing something"
    SOUP = BeautifulSoup(WORDS, features='html.parser')
    print(SOUP.get_text())

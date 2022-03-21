"""
This is the module that counts words
We want to write in a OOP style.
"""
# pylint: disable=C0303
# pylint: disable=R0903
class WordCounter:

    """
    This is a class that has all methods to count
    words
    """

    def __init__(self, word_string):
        """
        Constructor class: we give a string
        for the class to process
        """
        assert isinstance(word_string, str), "word string must be of type string"
        self.word_string = word_string
    
    def count_words(self):
        """
        This is the method that actually counts the words
        """
        word_splits = self.word_string.split()
        return len(word_splits)

if __name__ == "__main__":
    SENTENCE = "Daniel wolf"
    print(WordCounter(SENTENCE).count_words())

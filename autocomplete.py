"""Defines the class AutoComplete
"""
from trie import TrieNode, list_completions


__all__ = ['AutoComplete']



class AutoComplete(object):
    """
    Sets up the the corpus Trie at initialization,
    retrieves list of completions.
    """
    def __init__(self, filepath, nmin=1, case_sensitive=False):
        """Sets up the corpus Trie from a file.

        args:
            filepath:           path of the corpus file (.csv)
            nmin:               minimum length of input string
            case_sensitive:     defines if the search is case sensitive 
        """
        self.root = load_corpus_file(filepath, case_sensitive=case_sensitive)
        self.nmin = nmin
        self.case_sensitive = case_sensitive

    def completions(self, key):
        """returns list of possible completions for key in the corpus."""
        words = []
        
        if len(key) >= self.nmin:
    
            if not self.case_sensitive:
                key = key.lower()

            words = list_completions(self.root, key)

        return words


# helpers
def load_corpus(corpus, case_sensitive=False):
    """Builds a Trie from a list of strings."""
    root = TrieNode()

    for word in corpus:
        if case_sensitive:
            root.insert(word, word)
        else:
            root.insert(word.lower(), word)

    return root


def load_corpus_file(filepath, case_sensitive=False):
    """Builds a Trie from a file containing a list of strings."""
    with open(filepath,'r') as f:
        corpus = [word.strip() for word in f.readlines()]

    return load_corpus(corpus, case_sensitive=case_sensitive)

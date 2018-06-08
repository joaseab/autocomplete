"""Contains the TrieNode class, that represents a node of the Prefix Trie.
Use list_completions to retrieve the list of completions of a given word.
"""

__all__ = ['TrieNode', 'list_completions']



class TrieNode(object):
    """Node of the Trie. Contains value and children nodes"""
    def __init__(self):
        self.children = dict()
        self.value = None

    def insert(self, string, value):
        """Inserts string into Trie. Value is attached to the terminal node."""
        node = self
        index_last_char = None
        for index_char,char in enumerate(string):
            if char in node.children:
                node = node.children[char]
            else:
                index_last_char = index_char
                break

        if index_last_char is not None:
            for char in string[index_last_char:]:
                node.children[char] = TrieNode()
                node = node.children[char]

        node.value = value


def find_completions_node(node, key):
    """Returns node corresponding to matched prefix."""
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None

    return node


def list_completions(node, key):
    """Returns list of strings of the matched prefix completions."""
    completions = []

    def get_terminal(node):
        if node.value is not None:
            completions.append(node.value)
        for key in node.children:
            get_terminal(node.children[key])

    last_node = find_completions_node(node, key)
    if last_node is not None:
        get_terminal(last_node)

    return completions

"""Tests AutoComplete class and TrieNode class"""
import unittest

from autocomplete import AutoComplete
from trie import TrieNode, find_completions_node



class TestAutoComplete(unittest.TestCase):
 
    def setUp(self):
        self.ac = AutoComplete('data/testcorpus.csv', 
                               case_sensitive=False)

        self.ac_cs = AutoComplete('data/testcorpus.csv', 
                               case_sensitive=True)

        self.ac_n3 = AutoComplete('data/testcorpus.csv', 
                                  case_sensitive=False, nmin=4)

    def test_no_completion(self):
        self.assertEqual(len(self.ac.completions('zzz')), 0)

    def test_completion_len(self):
        self.assertEqual(len(self.ac.completions('a')), 6)
        self.assertEqual(len(self.ac.completions('b')), 3)
        self.assertEqual(len(self.ac.completions('z')), 0)
        self.assertEqual(len(self.ac.completions('d')), 1)
        self.assertEqual(len(self.ac.completions('abcdefg')), 1)
        self.assertEqual(len(self.ac.completions('Abcdefg')), 1)

        self.assertEqual(len(self.ac_cs.completions('a')), 5)
        self.assertEqual(len(self.ac_cs.completions('b')), 3)
        self.assertEqual(len(self.ac_cs.completions('z')), 0)
        self.assertEqual(len(self.ac_cs.completions('d')), 0)
        self.assertEqual(len(self.ac_cs.completions('abcdefg')), 0)
        self.assertEqual(len(self.ac_cs.completions('Abcdefg')), 1)

    def test_nmin(self):
        self.assertEqual(len(self.ac_n3.completions('q')), 0)
        self.assertEqual(len(self.ac_n3.completions('qw')), 0)
        self.assertEqual(len(self.ac_n3.completions('qwe')), 0)
        self.assertEqual(len(self.ac_n3.completions('qwer')), 1)

    def test_completions(self):
        completions = self.ac.completions('ab')
        words = ('abc','abcde','Abcdefg')
        cond = all([word in completions for word in words])
        self.assertTrue(cond)


class TestTrieNode(unittest.TestCase):
 
    def setUp(self):
        self.root = TrieNode()
        self.root.insert('ab', 'ab')
        self.root.insert('bc', 'bc')
        self.root.insert('cd', 'cd')
        self.root.insert('bcde', 'bcde')
        self.root.insert('bcdf', 'teste')

    def test_insert_root(self):
        self.assertEqual(len(self.root.children), 3)

    def test_children(self):
        node = self.root.children['a']
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.value, None)

        node = self.root.children['b']
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.value, None)

        node = node.children['c']
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.value, 'bc')

        node = node.children['d']
        self.assertEqual(len(node.children), 2)
        self.assertEqual(node.value, None)

        node_e = node.children['e']
        self.assertEqual(len(node_e.children), 0)
        self.assertEqual(node_e.value, 'bcde')

        node_f = node.children['f']
        self.assertEqual(len(node_f.children), 0)
        self.assertEqual(node_f.value, 'teste')

    def test_find_completions_node(self):
        node = find_completions_node(self.root, 'a')
        self.assertEqual(node, self.root.children['a'])

        node = find_completions_node(self.root, 'b')
        self.assertEqual(node, self.root.children['b'])

        node = find_completions_node(self.root, 'c')
        self.assertEqual(node, self.root.children['c'])

        node = find_completions_node(self.root, 'c')
        self.assertEqual(node, self.root.children['c'])

        node = find_completions_node(self.root, 'ab')
        self.assertEqual(node, self.root.children['a'].children['b'])

        node = find_completions_node(self.root, 'bc')
        self.assertEqual(node, self.root.children['b'].children['c'])

        node = find_completions_node(self.root, 'cd')
        self.assertEqual(node, self.root.children['c'].children['d'])

        node = find_completions_node(self.root, 'bcd')
        self.assertEqual(node, 
            self.root.children['b'].children['c'].children['d'])

        node = find_completions_node(self.root, 'bcde')
        self.assertEqual(node, 
            self.root.children['b'].children['c'].children['d'].children['e'])

        node = find_completions_node(self.root, 'bcdf')
        self.assertEqual(node, 
            self.root.children['b'].children['c'].children['d'].children['f'])


if __name__ == '__main__':
    unittest.main()

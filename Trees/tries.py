"""
link - https://www.youtube.com/watch?v=hjUJFjcrbR4

class Trie:
  def __init__(self):
    self.root = {"*":"*"}

  def add_word(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node:
        curr_node[letter] = {}
      curr_node = curr_node[letter]
    curr_node["*"] = "*"
  
  def does_word_exist(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node:
        return False
      curr_node = curr_node[letter]
    return "*" in curr_node
"""


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_full_word = False


class Trie:
  def __init__(self):
      self.root = TrieNode("*")

  def add_word(self, word) -> None:
      node = self.root

      for char in word:
          if char not in node.children:
              node.children[char] = TrieNode(char)
          node = node.children[char]

      node.is_full_word = True

  def does_word_exist(self, word) -> bool:
      if word == "":
          return True

      node = self.root

      for char in word:
          if char not in node.children:
              return False
          node = node.children[char]

      return node.is_full_word


trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]
for word in words:
    trie.add_word(word)

print(trie.does_word_exist("wait"))  # True
print(trie.does_word_exist(""))  # True
print(trie.does_word_exist("waite"))  # False
print(trie.does_word_exist("shop"))  # True
print(trie.does_word_exist("shoppp"))  # False

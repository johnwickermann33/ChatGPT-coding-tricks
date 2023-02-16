package tests;

class TrieTree {
    class TrieNode {
        TrieNode[] children;
        boolean isEndOfWord;

        TrieNode() {
            children = new TrieNode[26];
            isEndOfWord = false;
        }
    }

    private TrieNode root;

    public TrieTree() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode current = root;
        for (int i = 0; i < word.length(); ++i) {
            int index = word.charAt(i) - 'a';
            if (current.children[index] == null)
                current.children[index] = new TrieNode();

            current = current.children[index];
        }

        current.isEndOfWord = true;
    }

    public boolean search(String word) {
        TrieNode current = root;
        for (int i = 0; i < word.length(); ++i) {
            int index = word.charAt(i) - 'a';
            if (current.children[index] == null)
                return false;

            current = current.children[index];
        }

        return current.isEndOfWord;
    }

    public void printWordsWithPrefix(String prefix) {
        TrieNode current = root;
        for (int i = 0; i < prefix.length(); ++i) {
            int index = prefix.charAt(i) - 'a';
            if (current.children[index] == null)
                return;

            current = current.children[index];
        }

        printWords(current, prefix);
    }

    private void printWords(TrieNode node, String prefix) {
        if (node.isEndOfWord)
            System.out.println(prefix);

        for (int i = 0; i < 26; ++i) {
            if (node.children[i] != null) {
                char c = (char) (i + 'a');
                printWords(node.children[i], prefix + c);
            }
        }
    }
}

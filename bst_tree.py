class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
            
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        else:
            print("Value already exists in tree.")
            
    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False
        
    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left is not None:
            return self._search(value, current_node.left)
        elif value > current_node.value and current_node.right is not None:
            return self._search(value, current_node.right)
        else:
            return False
        
    def delete(self, value):
        if self.root is not None:
            self.root = self._delete(value, self.root)
            
    def _delete(self, value, current_node):
        if value == current_node.value:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                temp_node = current_node.right
                while temp_node.left is not None:
                    temp_node = temp_node.left
                current_node.value = temp_node.value
                current_node.right = self._delete(temp_node.value, current_node.right)
        elif value < current_node.value and current_node.left is not None:
            current_node.left = self._delete(value, current_node.left)
        elif value > current_node.value and current_node.right is not None:
            current_node.right = self._delete(value, current_node.right)
        return current_node

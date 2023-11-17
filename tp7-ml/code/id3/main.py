from decision_tree import *

data = [
    ["sunny", "hot", "high", False, "no"],
    ["sunny", "hot", "high", True, "no"],
    ["overcast", "hot", "high", False, "yes"],
    ["rainy", "mild", "high", False, "yes"],
    ["rainy", "cool", "normal", False, "yes"],
    ["rainy", "cool", "normal", True, "no"],
    ["overcast", "cool", "normal", True, "yes"],
    ["sunny", "mild", "high", False, "no"],
    ["sunny", "cool", "normal", False, "yes"],
    ["rainy", "mild", "normal", False, "yes"],
    ["sunny", "mild", "normal", True, "yes"],
    ["overcast", "mild", "high", True, "yes"],
    ["overcast", "hot", "normal", False, "yes"],
    ["rainy", "mild", "high", True, "no"]
]

attributes = ['outlook', 'temp', 'humidity', 'windy']
tree = DECISION_TREE_LEARNING(data, attributes, None)
print_tree(tree)

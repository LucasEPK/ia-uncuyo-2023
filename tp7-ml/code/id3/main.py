from decision_tree import *

# Example usage with your provided dataset
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

data1 = [
    ["rainy", "cool", "normal", False, "yes"],
    ["rainy", "cool", "normal", True, "no"],
    ["overcast", "cool", "normal", True, "no"],
    ["sunny", "mild", "high", False, "yes"],
    ["sunny", "cool", "normal", False, "no"],
    ["rainy", "mild", "normal", False, "no"],
    ["sunny", "mild", "normal", True, "no"],
    ["overcast", "mild", "high", True, "yes"],
    ["overcast", "hot", "normal", False, "no"],
    ["rainy", "mild", "high", True, "no"]
]

attributes = ['outlook', 'temp', 'humidity', 'windy']
tree = DECISION_TREE_LEARNING(data, attributes, None)
print_tree(tree)

bruh = unique_values('windy', data1)
print(bruh)
bruhp = calculate_positives(data1)
bruhn = calculate_negatives(data1)
print(bruhp," ", bruhn)

bruhAttribute = 'humidity'
attributeValues = unique_values(bruhAttribute, data1)
goal = B(bruhp / (bruhp + bruhn))
print("goal", goal)
remainder = H(bruhAttribute, attributeValues, data1, bruhp, bruhn)
print("remainder", remainder)
gain = information_gain(bruhAttribute, attributeValues, data1, bruhp, bruhn)
print("gainz", gain)

bruhA = argmax_importance(attributes, data1)
print(bruhA)
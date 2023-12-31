import math
# This module implements a decision tree for the tennis.csv dataset

class Node:
    # Nodes for the decision tree
    def __init__(self, label=None, children=None, classification=None):
        self.label = label # Attribute being tested
        self.children = children or {} # Dictionary of (value, subtree) pairs

def DECISION_TREE_LEARNING(examples, attributes, parent_examples):
    # This is an implementation of the pseudocode provided by AIMA on chapter 18

    if not examples:
        return PLURALITY_VALUE(parent_examples)
    elif all_same_classification(examples):
        return examples[0][-1]
    elif not attributes:
        return PLURALITY_VALUE(examples)
    else:
        A = argmax_importance(attributes, examples)
        tree = Node(label=A)

        # Hardcoded for now
        match A:
            case 'outlook':
                attributeSlot = 0
            case 'temp':
                attributeSlot = 1
            case 'humidity':
                attributeSlot = 2
            case 'windy':
                attributeSlot = 3


        for vk in unique_values(A, examples):
            exs = [e for e in examples if e[attributeSlot] == vk]
            subtree = DECISION_TREE_LEARNING(exs, [attr for attr in attributes if attr != A], examples)
            tree.children[(A, vk)] = subtree

        return tree

def PLURALITY_VALUE(examples):
    # Count occurrences of each class label and return the one with the highest count

    class_counts = {}
    for example in examples:
        label = example[-1]
        class_counts[label] = class_counts.get(label, 0) + 1
    
    return max(class_counts, key=class_counts.get)

def argmax_importance(attributes, examples):
    # This chooses the attribute with the highest information gain

    maxGainAttribute = None
    maxGain = -1

    p = calculate_positives(examples)
    n = calculate_negatives(examples)
    for attribute in attributes:
        attributeValues = unique_values(attribute, examples)
        gain = information_gain(attribute, attributeValues, examples, p, n)

        if gain > maxGain:
            maxGain = gain
            maxGainAttribute = attribute

    return maxGainAttribute

def all_same_classification(examples):
    # Check if all examples have the same class label
    return all(example[-1] == examples[0][-1] for example in examples)

def unique_values(attribute, examples):
    # Get unique values of the specified attribute from examples

    # Hardcoded for now
    match attribute:
        case 'outlook':
            attributeSlot = 0
        case 'temp':
            attributeSlot = 1
        case 'humidity':
            attributeSlot = 2
        case 'windy':
            attributeSlot = 3

    return set(example[attributeSlot] for example in examples)

# ================================== Aux functions =================================

def calculate_positives(examples):
    count = 0
    for example in examples:
        if example[-1] == "yes":
            count += 1
    return count

def calculate_negatives(examples):
    count = 0
    for example in examples:
        if example[-1] == "no":
            count += 1
    return count

def entropy(q):
    if q == 0 or q == 1:
        return 0
    return -(q * math.log2(q) + (1 - q) * math.log2(1 - q))

def B(q):
    return entropy(q)

def H(attribute, attribute_values, examples, p, n): 
    # Remainder function

    # Hardcoded for now
    match attribute:
        case 'outlook':
            attributeSlot = 0
        case 'temp':
            attributeSlot = 1
        case 'humidity':
            attributeSlot = 2
        case 'windy':
            attributeSlot = 3

    total_entropy = 0
    for value in attribute_values:
        exs = [e for e in examples if e[attributeSlot] == value]
        pk = sum(1 for ex in exs if ex[-1] == 'yes')  # Positive examples
        nk = sum(1 for ex in exs if ex[-1] == 'no')   # Negative examples
        total_entropy += (pk + nk) / (p + n) * B(pk / (pk + nk))

    return total_entropy

def information_gain(attribute, attribute_values, examples, p, n):
    goal_entropy = B(p / (p + n))
    remainder = H(attribute, attribute_values, examples, p, n)
    return goal_entropy - remainder

def print_tree(node, depth=0):
    if node is not None:
        if isinstance(node, str):
            print("  " * depth + f"Class: {node}")
        else:
            print("  " * depth + f"Attribute: {node.label}")
            for (value, subtree) in node.children.items():
                print("  " * (depth + 1) + f"Value: {value}")
                print_tree(subtree, depth + 2)

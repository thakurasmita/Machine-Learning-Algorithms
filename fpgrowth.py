# Sample code to do FP-Growth in Python
import pyfpgrowth
# Creating Sample Transactions
transactions = [
     ['d','b','c','a'],
     ['e','d','c'],
     ['a','b'],
     ['a','c','d'],
     ['f','g','d','b']
 ]
 
#Finding the frequent patterns with min support threshold=2
FrequentPatterns=pyfpgrowth.find_frequent_patterns(transactions=transactions,support_threshold=2)
print(FrequentPatterns)
 
# Generating rules with min confidence threshold=2
Rules=pyfpgrowth.generate_association_rules(patterns=FrequentPatterns,confidence_threshold=2)
Rules
# Bonus questions:
# 1. Write a generic function that will accept an array of type string or integer and count
# the length of each element.
# Example,
# Input: [“abc”, “apple”, “orange”]
# Output: [3,5,6]
# Input: [12, 456, 9000]
# Output: [2,3,4]
# No points: But I am going to put your name in my SIUE website under something cool. And
# if you keep on doing bonus problems for a certain number of times, I will give you an award
# towards the end of the semester in front of the whole class. It can be for more than one
# student. Still contemplating the idea but I will do something. Please participate. If you have
# attempted the bonus question the subject of the email should be “cs325 quiz-4_bonus”. Put
# everything in the same repo.

def elementLengths(arr):
    return [len(str(element)) for element in arr]

strings = input("Enter elements separated by commas: ")

array = [int(x) if x.isdigit() else x for x in strings.split(',')]

out = elementLengths(array)

print("Input:", array)
print("Output:", out)

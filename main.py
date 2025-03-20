with open("story.txt", "r") as f:
    story = f.read()

#print(story)
words = set()
target_start = "<"
target_end = ">"
start_of_word = 0

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != 0:
        word = story[start_of_word: i+1]
        words.add(word)
        

#print(words)

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

#print(answers)

for word in words:
    story = story.replace(word, answers[word])

print(story)





        

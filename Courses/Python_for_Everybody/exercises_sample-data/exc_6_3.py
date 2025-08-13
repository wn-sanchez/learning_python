def count(word, character):
    count = 0
    for letter in word:
        if letter == character:
            count = count + 1
    print(count)

word = input('Enter word:')
character = input('Enter character:')
count(word, character)

#using string method
print(word.count(character))

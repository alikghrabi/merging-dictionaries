def count_word(sentence):
    words = sentence.split()
    word_count={}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

sentence = input("Enter a sentence")
result = count_word(sentence)
print("Counted Words: ", result)
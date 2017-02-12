def count_word(word, ch):
    count = 0
    for letter in word:
        if letter == ch:
            count = count + 1
    return count


word_in = raw_input("Enter the word: ")
ch_in = raw_input("Enter the character you want to count: ")
count_ch = count_word(word_in, ch_in)
print count_ch

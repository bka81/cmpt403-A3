import string
from collections import Counter
import math

if __name__ == "__main__":
    # Read plaintext from file
    try:
        with open("vigenere.txt", "r", encoding="utf-8") as f:
            vigeneretext = f.read()
    except FileNotFoundError:
        print("Error: vigenere.txt not found.")
        exit(1)

    # get the words with their positions in the text
    words = vigeneretext.split()
    
    position_words = []
    p = 0
    for w in words: 
        position_words.append((w, p))
        p = p + len(w)

    # for analyzing word frequency
    count_per_word = Counter(words)
    repeated_words = count_per_word.most_common(30)
    print(f"Most repeated cipher words: {repeated_words}")
    
    # all the unique words in the text
    total_words = list(set(words))
    
    # get the positions of the words in the text with their repaated positions
    positions_unique = [[] for i in range(len(total_words))]

    for i in range(len(total_words)):
        for j in range(len(position_words)):
            if position_words[j][0] == total_words[i]:
                positions_unique[i].append(position_words[j][1])


    # Save the words and positions with more than 1 position
    unique_words_positions = []
    for i in range((len(positions_unique))):
        if(len(positions_unique[i]) > 1):
            unique_words_positions.append((total_words[i], positions_unique[i]))

    #calculate the distances between positions for repeated words 
    distances_between_positions = [[] for i in range(len(unique_words_positions))]
    for i in range((len(unique_words_positions))):
        for j in (range(1, len(unique_words_positions[i][1]))):
                distances_between_positions[i].append(unique_words_positions[i][1][j] - unique_words_positions[i][1][j-1])
        print(f"word: {unique_words_positions[i][0]}, positions: {unique_words_positions[i][1]}, distances: {distances_between_positions[i]}")

    print()

    # find the divisors for each distance between the words. 
    divisors = [[[] for j in range(len(distances_between_positions[i]))] for i in range(len(distances_between_positions))]
    for i in range(len(distances_between_positions)):
        for j in range(len(distances_between_positions[i])):
            for d in range(1, distances_between_positions[i][j] + 1):
                if distances_between_positions[i][j] % d == 0:
                    divisors[i][j].append(d)
        print(f"Divisors for {unique_words_positions[i][0]} : {divisors[i]}")            

    # note that the most repeated divisor accross different words and distances was 7. 
    ciphertext_no_spaces = []
    for char in vigeneretext:
        if char.isalpha():
            ciphertext_no_spaces.append(char)
    
    grid = []
    index = 0
    while(index < len(ciphertext_no_spaces)) :
        array = []
        for char in range(7):
            if index < len(ciphertext_no_spaces):
                array.append(ciphertext_no_spaces[index])
                index = index + 1
        grid.append(array)

    print()
    for row in grid: 
        print(row)

    #find the most common letters:
    letter_count = Counter(ciphertext_no_spaces)
    print(letter_count.most_common(5))


    
    columns_grid = list(zip(*(grid[0:(len(grid) - 1)])))
    col_letter_count = []
    for i in range(len(columns_grid)):
        col_letter_count.append(Counter(columns_grid[i]))
        print (f"most common letter per column: {col_letter_count[i].most_common(2)}")

    
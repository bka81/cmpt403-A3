

# read the cipher files and save them as raw bytes:
with open("ctext0", "rb") as f:
    ctext0_bytes = f.read()
with open("ctext1", "rb") as f:
    ctext1_bytes = f.read()

with open("words1.txt", "r", encoding="utf-8") as f:
    words_p = f.read()

words_letter_p = words_p

ctext0_list = list(ctext0_bytes)
ctext1_list = list(ctext1_bytes)

guess_list = []

guess_list = [words_letter_p]
#for i in range(len(words_letter_p)): guess_list.append(words_letter_p[i])



result = [[] for i in range(len(guess_list))]
result_words = []

for i in range(len(guess_list)):
    for j in range(len(guess_list[i])):
        result[i].append(ctext0_list[j] ^ ctext1_list[j] ^ ord(guess_list[i][j]))
    result_words.append("".join([chr(x) for x in result[i]]))

#print(result)
for i in range(len(guess_list)):
    print(f"{guess_list[i]} : {result_words[i]}")

#check the size of the text:
text = """The very first well-documented description of a polyalphabetic cipher was by Leon Battista Alberti around 1467 and used a metal cipher disk to switch between cipher alphabets. Alberti's system only switched alphabets after several words, and switches were indicated by writing the letter of the corresponding alphabet in the ciphertext. Later, Johannes Trithemius, in his work Polygraphia (which was completed in manuscript form in 1508 but first published in 1518),[6] invented the tabula recta, a critical component of the Vigenere cipher.[7]

Padding Padding Padding Padding Padding Padding Padding Padding Padding Padding Padding Padding Padding
"""
print(len(text.encode()))

text_prog = """In programming and information security, a buffer overflow or buffer overrun is an anomaly whereby a program writes data to a buffer beyond the buffer's allocated memory, overwriting adjacent memory locations.

Buffers are areas of memory set aside to hold data, often while moving it from one section of a program to another, or between programs. Buffer overflows can often be triggered by malformed inputs; if one assumes all inputs will be smaller than a certain size and the buffer is created to be that size, then an anomalous transaction that produces more data could cause it to write past the end of the buffer.

Padding Padding Padding Paddi"""
print(len(text_prog.encode()))
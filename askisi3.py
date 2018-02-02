def rot13(s):
    result = ""
    for letter in s:
        letter_num = ord(letter)
        if letter_num >= ord('A') and letter_num <= ord('Z'):
            if letter_num > ord('M'):
                letter_num -= 13
            else:
                letter_num += 13
        elif letter_num >= ord('a') and letter_num <= ord('z'):
            if letter_num > ord('m'):
                letter_num -= 13
            else:
                letter_num += 13
        result += chr(letter_num)
    return result

word = raw_input("dose leksi")
print "rot13 einai: "
print rot13(word)

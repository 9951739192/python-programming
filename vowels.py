#Write a program to fetch all words which starts and ends with vowel in the string?
def word_with_vowel():
    st = 'Python is number one language'
    vowel='aeiou'
    words=[word for word in st.split() if word[0].lower() in vowel and word[-1].lower() in vowel]
    print(words)
word_with_vowel()    

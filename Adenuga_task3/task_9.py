# # task_9
# # #9 Ask the user to enter a sentence and print the number of vowels in it.
sentence = input("Enter your sentence here: ")
# #coversion 
con_sentence = sentence.lower()
print(con_sentence.count("a") + con_sentence.count("e") + con_sentence.count("i") + con_sentence.count("o") + con_sentence.count("u i"))
# second approach
vowel_a = sentence.count('a')
vowel_e = sentence.count("e")
vowel_i = sentence.count("i")
vowel_o = sentence.count("o")
vowel_u = sentence.count("u")
# display
volwel_alpha = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
print(f"the vowels pesent in your sentence {volwel_alpha}")

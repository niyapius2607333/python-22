str=input("Enter a string ")
vowels="aeiouAEIOU"
vowels_count=0
consonants_count=0
for char in str:
    if char in vowels:
        vowels_count+=1
    else:
        consonants_count+=1
print("No.of vowels in the given statement",vowels_count)
print("No. of consonants in the given statement",consonants_count)





from operator import sub


def anagrams_of(string_to_get):
    #Base Case: string = 1 char
    if len(string_to_get) == 1:
        return string_to_get
    
    #Create an array to hold all anagrams:
    collection = []

    #Find all anagrams of substring
    substring_anagrams = anagrams_of(string_to_get[1:])

    #Iterate over all substrings
    for substring_anagram in substring_anagrams:
        for i in range(0,len(substring_anagram)+1):
            #Create a copy of the substring anagram
            copy = substring_anagram

            # Insert first char of string into substring based on index
            collection.append((copy[:i] + string_to_get[0] + copy[i:]))
    
    return collection



print(anagrams_of("abc"))
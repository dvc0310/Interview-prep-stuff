def mergeAlternately(word1, word2):
    longer = word1
    shorter = word2
    
    if len(word2) > len(word1):
        longer, shorter = word2, word1
    
    word = ""
    i = 0
    while i < len(shorter):
        word += word1[i]
        word += word2[i]
        i += 1

    while i < len(longer):
        word += longer[i]
        i += 1

    return word
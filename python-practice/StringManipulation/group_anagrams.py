def group_anagrams(strs):

    group = []
    processed = set()

    for char in strs:
        if char not in processed:
            anagram_group = [char]
            processed.add(char)
        
            for ch in strs:
                if ch != char and ch not in processed:
                    if sorted(ch) == sorted(char):
                        anagram_group.append(ch)
                        processed.add(ch)
        
            group.append(anagram_group)

    return group

print(group_anagrams(input("Enter words separated by space: ").split()))    
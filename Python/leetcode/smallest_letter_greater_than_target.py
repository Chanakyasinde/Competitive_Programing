def nextGreatestLetter(letters, y):
    for let in letters:
        if let > y:
            return let
    return letters[0]

#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    result = []
    if pattern == "":
        return True
    
    for i in range(0, len(text)):    # loop every char in text at index i
        if text[i] == pattern[0]:   # if curr text char is equal to first char in pattern
            j = i
            for p in range(len(pattern)):
                if j > len(text)-1 or pattern[p] != text[j]:
                    break
                if p == len(pattern)-1:
                    result.append(i)
                j += 1
    return len(result) != 0


# bananas
#     nas
# 0123456

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    result = []
    if pattern == "":
        return 0
    
    for i in range(0, len(text)):    # loop every char in text at index i
        if text[i] == pattern[0]:   # if curr text char is equal to first char in pattern
            j = i
            for p in range(len(pattern)):
                if j > len(text)-1 or pattern[p] != text[j]:
                    break
                if p == len(pattern)-1:
                    return i
                    

                j += 1

    return None










                
                



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)p
    result = []
    len_text = len(text)
    
    for i in range(0, len_text):    # loop every char in text at index i
        if len(pattern) == 0:
            for t in range(0, len_text):
                result.append(t)
            break    

        if text[i] == pattern[0]:   # if curr text char is equal to first char in pattern
            j = i
            for p in range(len(pattern)):
                if j > len(text)-1 or pattern[p] != text[j]:
                    break
                if p == len(pattern)-1:
                    result.append(i)
                j += 1
    return result


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
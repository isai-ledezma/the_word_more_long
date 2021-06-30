def strmorelong(text1):
    print(text1)
    long = 'a'
    for word in text1:
        if len(word) > len(long):
            long = word
    print(f'the str more long is    {long}      with {len(long)} labels')


def main():
 
    text = input("give me the word's or text:") #example 'the wolf are big' where wolf is the str more long
    textsplited = text.split(" ")
    strmorelong(textsplited)
    pass


if __name__ == '__main__':
    main()

def encode(plaintext,key):
    plaintext = plaintext.lower()
    ciphertext = []
    for letter in plaintext:
        ciphertext.append(chr(((ord(letter) - 96 + key)%26) + 96 ))
    return(''.join(ciphertext))

def decode(ciphertext,key):
    ciphertext = ciphertext.lower()
    plaintext = []
    for letter in ciphertext:
        plaintext.append(chr(((ord(letter) - 96 - key)%26) + 96 ))
    return(''.join(plaintext))

def decode_close_matches(ciphertext,key):
    plaintext = decode(ciphertext,key)
    if plaintext in data.keys():
        return(plaintext)
    return(get_close_matches(plaintext,data.keys())[0])


enorde=input('Decode or Encode?(d or e)\n')
sentence=input("enter the Phrase to encode or decode:\n")
b=[]
sentence_ex = sentence.split()
print(sentence_ex)
if enorde=='e':
    key=eval(input("what is the Key?\n"))
    for word in sentence.split():
        b.append(encode(word,key))
    print(' '.join(b))

elif enorde=='d':
    scores=[0]*26
    gcm=input('Get Close Matches?(y or n(no is recommended))')
    if gcm=='y':
        from difflib import get_close_matches
        import json
        data=json.load(open('data.json'))
        for key in range(1,26):
            for word in sentence.split():
                word = decode(word,key)
                if word in data.keys():
                    scores[key - 1] += 2
                else:
                    word_close_match = get_close_matches(word,data.keys())    
                    if len(word_close_match) != 0:
                        scores[key - 1] += 1
        bestkey = scores.index(max(scores)) + 1         
        for word in sentence_ex:
            b.append(decode_close_matches(word,bestkey))
        print(' '.join(b))   
    else:
        import json
        data=json.load(open('data.json'))
        for key in range(1,26):
            for word in sentence.split():
                word=decode(word,key)
                if word in data.keys():
                    scores[key-1]+=1
        bestkey = scores.index(max(scores)) + 1
        for word in sentence.split():
            b.append(' ')
            b.append(decode(word,bestkey))   
        print('The key semms to be %d'% bestkey)
        print(''.join(b)[1:])


    
else:
    print('WRONG')


    

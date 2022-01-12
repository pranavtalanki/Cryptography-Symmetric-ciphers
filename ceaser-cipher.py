def getNum(text):
    k=0
    for i in range(len(text)):
        numbers[i]=ord(text[k])%65
        k+=1
    print(numbers)


def CeaserCipher(text,key):
    getNum(text)
    for i in range(len(text)):
        cipherNum[i]=(numbers[i]+key)
    print("before modding : ",cipherNum)
    for i in range(len(text)):
        cipherNum[i]=(cipherNum[i])%26
    print("after modding : ",cipherNum)


plaintext=input("Enter plain text : ")
key=int(input("Enter key : "))
l=len(plaintext)
numbers=[0 for i in range(l)]
cipherNum=[0 for i in range(l)]
CeaserCipher(plaintext,key)
ciphertext=[]
for i in range(len(plaintext)):
    ciphertext.append(chr(cipherNum[i] + 65))
print("ciphertext : ","".join(ciphertext))



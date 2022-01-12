def getNum(text):
    k=0
    for i in range(len(text)):
        numbers[i]=ord(text[k])%65
        k+=1
    print(numbers)
def AffineCipher(text,a,b):
    getNum(text)
    for i in range(len(text)):
        cipherNum[i]=(a*numbers[i]+b)
    print("before modding : ",cipherNum)
    for i in range(len(text)):
        cipherNum[i]=cipherNum[i]%26
    print("after modding : ",cipherNum)


plaintext=input("Enter plain text : ")
alpha=int(input("Enter ALPHA : "))
beta=int(input("Enter BETA : "))
l=len(plaintext)
numbers=[0 for i in range(l)]
cipherNum=[0 for i in range(l)]
AffineCipher(plaintext,alpha,beta)
ciphertext=[]
for i in range(len(plaintext)):
    ciphertext.append(chr(cipherNum[i] + 65))
print("ciphertext : ","".join(ciphertext))



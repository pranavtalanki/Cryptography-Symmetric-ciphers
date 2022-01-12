import math

def getkeyMatrix(key):
	k = 0
	print("key Matrix : ")
	for i in range(3):
	    for j in range(3):
	        keyMatrix[i][j] = ord(key[k]) % 65
			k=k+1
        print(keyMatrix[i])
	
def getmsgMatrix(key,l):
	k = 0
	for i in range(l):
		for j in range(3):
			messageVector[j][i] = ord(key[k]) % 65
			k += 1
	print("messagematrix : ",messageVector)


def encrypt(messageVector,l):
	for i in range(3):
		for j in range(l):
			for x in range(3):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26
	print("cipherMatrix : ",cipherMatrix)

def HillCipher(message, key,l):

	getkeyMatrix(key)
	getmsgMatrix(message,l)
	encrypt(messageVector,l)
	CipherText=[]
	for i in range(l):
		for j in range(3):
			CipherText.append(	)
	print("Ciphertext: ", "".join(CipherText))




message = input("Enter message string(make sure all are capitals): ")
key = input("Enter key string(make sure all are capitals): ")

print(len(message))
l=len(message)/3
l=math.ceil(l)
print(l)
keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0]*l for i in range(3)]
cipherMatrix = [[0]*l for i in range(3)]
HillCipher(message, key,l)

#DKUUJRJER
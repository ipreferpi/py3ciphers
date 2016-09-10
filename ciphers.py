#Cipher Tools
import string
import re

low = string.ascii_lowercase
up = string.ascii_uppercase
def shift(char, shiftVal):
	if char in low:
		return low[(low.index(char) + shiftVal) % 26]
	elif char in up:
		return up[(up.index(char) + shiftVal) % 26]
	else:
		return char

def caesarE(plaintext, sh): return "".join(shift(char,sh) for char in cleantext(plaintext))

def caesarD(plaintext, sh): return caesarE(plaintext, 26 - (sh % 26))

def rot13(plaintext): return(caesarE(plaintext, 13))


def substitute(ch, key):
	if ch in low:
		return key[low.index(ch)]
	elif ch in up:
		return key[up.index(ch)].upper()
	else:
		return ch

def atbash(plaintext):
	key = low[::-1]
	return "".join(substitute(char, key) for char in cleantext(plaintext))

def vigenereE(plaintext, key):
	ciphertext = ''
	ptindex = 0
	keyindex = 0
	while ptindex < len(plaintext):
		ciphertext += shift(plaintext[ptindex], letterindex(key[keyindex]))
		keyindex += 1
		ptindex += 1
		if keyindex > len(key):
			keyindex = 0
	return ciphertext

def vigenereD(plaintext, key):
	ct = ''
	ptindex = 0
	keyindex = 0
	while ptindex < len(plaintext):
		ct += shift(plaintext[ptindex], 26 - letterindex(key[keyindex]))
		keyindex += 1
		ptindex += 1
		if keyindex > len(key):
			keyindex = 0
	return ct

def letterindex(ch):
	if ch.lower() in low:
		return low.index(ch.lower())
	else:
		return -1

def letterfreq(text):
	freq = {}

	for char in text:
			print(char)
			if char in freq:
				freq[char] += 1
			else:
				freq[char] = 1
	
	print(freq)
	return freq


def groupfreq(textin, minSize, maxSize):
	freqarray = []
	minS = minSize
	maxS = maxSize+1
	text = cleantext(textin)
	for i in range(minS,maxS):
		currentIndex = 0
		freq = {}
		while(currentIndex < len(text)-1):
			sliced = text[currentIndex:currentIndex+i]
		
			if (sliced in freq):
				freq[sliced] += 1
			else:
				freq[sliced] = 1
			currentIndex += 1
		freqarray.append(freq)

	return freqarray

def cleantext(textin): #removes all nonletters and capitalizes
	new = ""
	text = textin.upper()
	for char in text:
		if (char in up):
			new += char
	return new;

def groupDistance(textIn):
	frequency = groupfreq(textIn, 3, 5)
	for dictpair in frequency:
		for group in dictpair:
			if dictpair[group] > 1:
				print(group, dictpair[group], '\n')
				kek = [m.start() for m in re.finditer(group, textIn)]
				print(kek)


#Testing
print("Testing Caesar")
print(caesarE("Beware the ides of March", 1))
print(caesarD(caesarE("Beware the ides of March", 1), 1))
print("Testing Rot13")
print(rot13("So secure OMG"))
print("Testing Atbash")
print(atbash("Super Secure!"))

print(letterindex('z'))
print(vigenereE("testing", "yourmom"))
print(vigenereD("RSMKUBS", "yourmom"))

print(vigenereE("whoops", "yourmom"))

testdata1 = "RIKVBIYBITHUSEVAZMMLTKASRNHPNPZICSWDSVMBIYFQEZUBZPBRGYNTBURMBECZQKBMBPAWIXSOFNUZECNRAZFPHIYBQEOCTTIOXKUNOHMRGCNDDXZWIRDVDRZYAYYICPUYDHCKXQIECIEWUICJNNACSAZZZGACZHMRGXFTILFNNTSDAFGYWLNICFISEAMRMORPGMJLUSTAAKBFLTIBYXGAVDVXPCTSVVRLJENOWWFINZOWEHOSRMQDGYSDOPVXXGPJNRVILZNAREDUYBTVLIDLMSXKYEYVAKAYBPVTDHMTMGITDZRTIOVWQIECEYBNEDPZWKUNDOZRBAHEGQBXURFGMUECNPAIIYURLRIPTFOYBISEOEDZINAISPBTZMNECRIJUFUCMMUUSANMMVICNRHQJMNHPNCEPUSQDMIVYTSZTRGXSPZUVWNORGQJMYNLILUKCPHDBYLNELPHVKYAYYBYXLERMMPBMHHCQKBMHDKMTDMSSJEVWOPNGCJMYRPYQELCDPOPVPBIEZALKZWTOPRYFARATPBHGLWWMXNHPHXVKBAANAVMNLPHMEMMSZHMTXHTFMQVLILOVVULNIWGVFUCGRZZKAUNADVYXUDDJVKAYUYOWLVBEOZFGTHHSPJNKAYICWITDARZPVU"
# testingfreq = groupfreq(testdata1,3,5)



# for mm in testingfreq:
# 	for cc in mm:
# 		if mm[cc] > 1:
# 			print(cc, mm[cc], '\n')

groupDistance(testdata1)
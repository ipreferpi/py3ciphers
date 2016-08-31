#Cipher Tools
import string
low = string.ascii_lowercase
up = string.ascii_uppercase
def shift(ch, sh):
	if ch in low:
		return low[(low.index(ch) + sh) % 26]
	elif ch in up:
		return up[(up.index(ch) + sh) % 26]
	else:
		return ch

def caesarE(plaintext, sh): return "".join(shift(ch,sh) for ch in plaintext)

def caesarD(plaintext, sh): return encrypt(plaintext, 26 - (sh % 26))

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
	return "".join(substitute(ch, key) for ch in plaintext)

def vigenereE(plaintext, key):
	ct = ''
	ptindex = 0
	keyindex = 0
	while ptindex < len(plaintext):
		ct += shift(plaintext[ptindex], letterindex(key[keyindex]))
		keyindex += 1
		ptindex += 1
		if keyindex > len(key):
			keyindex = 0
	return ct

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




print("Testing Caesar")
print(caesarE("Beware the ides of March", 1))
print("Testing Rot13")
print(rot13("So secure OMG"))
print("Testing Atbash")
print(atbash("Super Secure!"))

print(letterindex('v'))
print(vigenereE("testing", "yourmom"))
print(vigenereD("RSMKUBS", "yourmom"))


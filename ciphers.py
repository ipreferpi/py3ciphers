#Cipher Tools

#TO DO
#	Make each cipher it's own object, with it's own functions of .encrypt and .decrypt ie caesar.decrypt()
#	Finish the frequency analysis functions for breaking Vigenere ciphers, and put them inside an object
import string
import re

low = string.ascii_lowercase
up = string.ascii_uppercase

def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)


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
	plaintext = cleantext(plaintext)
	ptindex = 0
	keyindex = 0
	while ptindex < len(plaintext):
		ciphertext += shift(plaintext[ptindex], letterindex(key[keyindex]))
		keyindex += 1
		ptindex += 1
		if keyindex > len(key) -1:
			keyindex = 0
	return ciphertext

def vigenereD(plaintext, key):
	ct = ''
	ptindex = 0
	keyindex = 0
	plaintext = cleantext(plaintext)
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
	#Finds the frequency of each letter in the text
	#Input: text string
	#Output: Dictionary of letters and the number of occurences
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
	#Finds all occurences of text groups in size range
	#Input: text, minimum size, and maximum size
	#Output:
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
	return new

def groupDistance(textIn):
	#Finds the distance between occurences between each text group in the provided text
	#Returns dictionary of 
	print("running groupdistance")
	frequency = groupfreq(textIn, 3, 7)
	distdict = {}
	for dictpair in frequency:
		for group in dictpair:
			if dictpair[group] > 1:
				#print(group, dictpair[group])
				#print("finding instances of", group)
				kek = [m.start() for m in re.finditer(group, cleantext(textIn))]
				#print(kek)
				#check the distance between instances of group in kek
				distances = set()
				denominators = set()

				for loc in kek:
					for x in range(0,len(kek)-1):
						thisdistance = loc - kek[x]
						#print(loc, "minus", kek[x])
						if thisdistance > 0:
							distances.add(thisdistance)
				#print("All distances are",distances)
				

				for item in distances:
					f = factors(item)
					f.discard(1)
					denominators.update(f)
				#print(denominators, "\n")
				distdict[group] = denominators
	return distdict



def breakVigenere(ct):
	freqAnalysis = groupDistance(ct)
	print("Running breaker")
	factorOccurences = {}
	for group in freqAnalysis:
		#Uncomment next line to print all groups and their factors
		#print(group, "\t", freqAnalysis[group])
		for factor in freqAnalysis[group]:
			if factor in factorOccurences:
				factorOccurences[factor] += 1
			else:
				factorOccurences[factor] = 1
	
	for counter in range(1,50):
		if counter in factorOccurences:
			print(counter, '\t', factorOccurences[counter])

#Testing
def testCipherFunctions():
	#Test Caesar
	print("Testing Caesar")
	print(caesarE("Beware the ides of March", 1))
	print(caesarD(caesarE("Beware the ides of March", 1), 1))
	print()
	#Test Rot13
	print("Testing Rot13")
	print(rot13("So secure OMG"))
	print()

	#Test AtBash
	print("Testing Atbash")
	print(atbash("Super Secure!"))
	print()
	
	#Test Vigenere
	print(vigenereE("testing", "yourmom"))
	print(vigenereD("RSMKUBS", "yourmom"))
	print()
	
	#Output should be this:
	#> Testing Caesar
	#> CFXBSFUIFJEFTPGNBSDI
	#> BEWARETHEIDESOFMARCH

	#> Testing Rot13
	#> FBFRPHERBZT

	#> Testing Atbash
	#> HFKVIHVXFIV

	#> RSMKUBS
	#> TESTING

def testBreakerFunctions():
	testkey = "virtual"
	testpt = "WATCHINGACOASTASITSLIPSBYTHESHIPISLIKETHINKINGABOUTANENIGMATHEREITISBEFOREYOUSMILINGFROWNINGINVITINGGRANDMEANINSIPIDORSAVAGEANDALWAYSMUTEWITHANDAIROFWHISPERINGCOMEANDFINDOUTTHISONEWASALMOSTFEATURELESSASIFSTILLINTHEMAKINGWITHANASPECTOFMONOTONOUSGRIMNESSTHEEDGEOFACOLOSSALJUNGLESODARKGREENASTHEBEALMOSTBLACKFRINGEDWITHWHITESURFRANSTRAIGHTLIKEARULEDLINEFARFARAWAYALONGABLUESEAWHOSEGLITTERWASBLURREDBYACREEPINGMISTTHESUNWASFIERCETHELANDSEEMEDTOGLISTENANDDRIPWITHSTEAUZEREANDTHEREGREYISHWHITISHSPECKSSHOWEDUPCLUSTEREDINSIDETHEWHITESURFWITHAFLAGFLYINGABOVETHEMPERHAPSSETTLEMENTSSOMECENTURIESOLDANDSTILLNOBIGGERTHANPINHEADSONTHEUNTOUCHED"


	breakerTest = vigenereE(testpt, testkey)
	print(breakerTest)

	breakVigenere(breakerTest)
	print(len(testkey))

testCipherFunctions()
testBreakerFunctions()
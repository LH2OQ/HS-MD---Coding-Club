"""
HELFERFUNKTIONEN
"""

"""
STRINGS
"""
def isUpper(c: str):
	return c.isalpha() and c == c.upper()

def isLower(c: str):
	return c.isalpha() and c == c.lower()
	
def splitCCI(text: str, after: list = [")"], before: list = [] ):
	out = ""
	i = 0
	for char in text:
		inA = char in after
		nInB = not char in before
		inB = char in before
		nInA = not char in after 
		oInA = inA and nInB
		oInB = inB and nInA
		inAB = inA and inB
		nInAB = nInA and nInB
		hasBef = i > 0
		hasNxt = i < len(text) - 1
		isL = isLower(char)
		isD = char.isdigit()
		isA = char.isalpha()
		befIsU = hasBef and isUpper(text[i-1])
		befIsL = hasBef and isLower(text[i-1])
		befIsD = hasBef and text[i-1].isdigit()
		befIsA = hasBef and text[i-1].isalpha()
		nxtIsU = hasNxt and isUpper(text[i+1])
		nxtIsL = hasNxt and isLower(text[i+1])
		nxtIsD = hasNxt and text[i+1].isdigit()
		nxtIsA = hasNxt and text[i+1].isalpha()
		cci = "#C&C&I#"
		if oInA:
			out += char
		if ((isL or oInA) and nxtIsU) or (isD and nxtIsA) or (isA and nxtIsD):
			out += cci
		if inB :
			out += char
			if inA:
				out += cci
			i += 1
	return out.split(cci)

def deleteDbl(arr: list):
	for x in arr:
		for y in arr:
			if x is not y and x == y:
				del arr[arr.index(x)]

def replaceList(string: str, arr: list, repl: str or list):
	newstr = repl
	for i in range(len(arr)):
		if isinstance(newstr, list):
			newstr = repl[i]
		string = string.replace(arr[i], newstr)
	return string
	
def splitReplaced(string: str, arr: list, repl: str):
	return replaceList(string, arr, repl).split(repl)

"""
DICTIONARIES AND SETS
"""
def nestedSet(dct, keys, value):
    for k in keys[:-1]:
        dct = dct.setdefault(k, {})
    dct[keys[-1]] = value
    return dct

def setHasKey(dct, key: str):
	t = type(dct)
	if t == dict:
		for [k, v] in dct.items():
			if type(v) == dict:
				return setHasKey(v, key)
			if k == key:
				return True
	return False

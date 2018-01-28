#!/usr/bin/python

def Tally(Dictionary):

	String = ''

	for Key in Dictionary:
		String = String + Key.lower()

	Vowels = {
		'a':0,
		'e':0,
		'i':0,
		'o':0,
		'u':0
	}

	for Character in String:
		if Vowels.has_key(Character):
			Vowels[Character] = Vowels[Character] + 1

	print(Vowels)
	print

	return sum(Vowels.values())

Dictionary = {'Cyan':123, 'Magenta':'ABC', 'Yellow':456, 'Black':'DEF', 'Red':789, 'Green':'GHI', 'Blue':0}

print(Dictionary)
print
print(str(Tally(Dictionary)) + ' vowel(s)')

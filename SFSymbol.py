# python3 SFSymbol.py >> SFSymbol.swift

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import os
import plistlib

def capitalize(index, text):
	out = text.capitalize() if index != 0 else text
	if index == 0:
		if text[0].isdigit():
			out = '_' + out
	return out

def generateSymbolName(symbolName):
	name = []
	components = symbolName.split('.')
	for index, component in enumerate(components):
		name.append(capitalize(index, component))
	return "".join(name)			

def generateSwiftEnumeration(propertyList):
	print("enum SFSymbol: String {")
	for property in propertyList['symbols']:
		print('    ' + generateSwiftEnumerationCase(property))
	print("}")	

def generateSwiftEnumerationCase(property):
	return 'case `' + generateSymbolName(property) + '` = ' + '"' + property + '"'

def main():
	fileName = os.path.expanduser('name_availability.plist')
	propertyList = plistlib.readPlist(fileName)
	if 'symbols' in propertyList:
		generateSwiftEnumeration(propertyList)

main()

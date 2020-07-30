import pyfiglet
import sys
import pickle

print("-----------------------------------------------------------------------------------------------------------------------")
print(pyfiglet.figlet_format("Discord ASCII Generator"))
print("-----------------------------------------------------------------------------------------------------------------------")
print('Release: 0.1.3')
print('Developed by: Sumedh')
print()
print("Description: Based on pyfiglet, this app will convert your text to BASIC ASCII and add formatting for Discord. \nThis will enable you to simply enter text, select border & spacing preference and copy paste it into discord. Enjoy!")
print("-----------------------------------------------------------------------------------------------------------------------")
print("New with v0.1.3: ")
print("		- Ability to add spacing between each character to make it look nicer")
print("		- Fixed Discord formatting bug")
print("		- Save default preferences by 'stfu' command when prompted for exit.")
print("		- *Note ^^ : Program needs to be restarted in order for preferences to be loaded in")
print("		- If you would like to reset preferences, just delete the prefs.txt file")

print("-----------------------------------------------------------------------------------------------------------------------")

print()


border = False
die = False
extra_spacing = False
set_default = False

def load_prefs():
	global extra_spacing, border, set_default
	try:
		with open('prefs.txt','rb') as sav:
			border = pickle.load(sav)
			extra_spacing = pickle.load(sav)
			set_default = pickle.load(sav)
	except:
		print("Unable to Load Preferences")
		print()
		set_default = False
		border = False
		die = False
		extra_spacing = False

load_prefs()

def save_prefs():
	global extra_spacing, border, set_default
	try:
		with open('prefs.txt','wb') as sav:
			border = pickle.dump(border,sav,pickle.HIGHEST_PROTOCOL)
			extra_spacing = pickle.dump(extra_spacing,sav,pickle.HIGHEST_PROTOCOL)
			set_default = pickle.dump(set_default,sav,pickle.HIGHEST_PROTOCOL)
	except:
		print("Unable to Save Preferences")

def main():
	global border, die, extra_spacing, set_default
	word = input("Enter text: ")
	if set_default == False:
		try:
			panel = input("Would you like a panel? (Default: no) y/n: ")
			if panel == 'y':
				border = True
			else:
				pass
		except:
			main()

		try:
			spacing = input("Would you like extra spacing between characters? y/n: ")
			if spacing == 'y':
				extra_spacing = True
			else:
				pass
		except:
			main()

	for_d(convert(word))
	print()
	end_s = input(str("Type exit/quit if you want to exit...Type anything else to keep going: "))
	if end_s == ('exit' or 'quit'):
		die = True
	elif end_s == 'stfu':
		set_default = True
		save_prefs()
		print("Ok, Saving preferences...")

def convert(text):
	global extra_spacing
	output = text
	if extra_spacing == True:
		output = " ".join(output)
	else:
		pass
	output = pyfiglet.figlet_format(output)
	output = output.replace("`","'")
	return output 

def for_d(art):
	global border
	line_list = art.split('\n')
	final = []
	if border == True:
		for i in line_list:
			bordered_line = ('`|' + i + '|`')
			print(bordered_line)

	else:
		for i in line_list:
			new_ln = '`' + i + "`"
			#.append(new_ln)
			print(new_ln)


while die == False:
	main()

print('ded')
sys.exit()
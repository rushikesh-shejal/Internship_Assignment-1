def char_count(s):
	str=s.lower()
	vowels="aeoui"
	vow_count=0
	space_count=0
	special_char_count=0
	digit_count=0
	for char in str:
		if char.isalpha():
			if char in vowels:
				vow_count+=1
		elif char.isdigit():
			digit_count+=1
		elif char.isspace():
			space_count+=1
		else:
			special_char_count+=1
			
	print(f"\nAnalysis for: '{s}'")
	print(f"Vowels: {vow_count}")
	print(f"Digits: {digit_count}")
	print(f"Spaces: {space_count}")
	print(f"Special Characters: {special_char_count}")

input_string=input("Enter a String::")
char_count(input_string)
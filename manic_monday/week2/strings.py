def ask() -> str:
	#: ask for a text and return as string
	return input("Make a title from... ")

def titlize(s: str) -> str:
	#  change s into title form and return as string
	s = s.lower()
	s = s.title()
	return s

def main():
	# do not change code below
	s = ask()
	s = titlize(s)
	print(f"The title is: {s}")

if __name__ == "__main__":
	# do not change code below
	main()

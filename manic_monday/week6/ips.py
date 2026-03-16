import re

def read_ips():
	with open("ips.txt") as f:
		content = f.read()
	content =  content.strip().split(" ")
	return list(dict.fromkeys(content))		
	

def get_pattern():
	# see https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
	# uses regex to determine of IP address is a valid IP in the range:
	# 47.82.11.0 - 47.82.11.255
    # return the pattern, so something like r"^47.....$"
	return r"^47\.82\.11\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d?|0)$"

def filter_ips(all_ips):
    pattern = get_pattern()
    format =  re.compile(pattern=pattern)
    correct = [ip for ip in all_ips if format.match(ip)]
    return correct

def main():
	# do not change below code
	all_ips = read_ips()
	correct_ips = filter_ips(all_ips)
	for p in correct_ips:
		print(p)
	print(len(correct_ips))

if __name__ == "__main__":
	main()

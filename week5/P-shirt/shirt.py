import sys
from PIL import Image
from PIL import ImageOps

file_suffix = ["png", "jpg", "jpeg"]

def check_file_arguments():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()
    if len(sys.argv) > 4:
        print("Too much command-line arguments")
        sys.exit()

    # get files suffix
    before_file = sys.argv[1]
    after_file = sys.argv[2]

    if len(before_file.split(".")) != 2 or len(after_file.split(".")) != 2:
        print("Invalid Input")
        sys.exit()
    before_suffix = before_file.split(".")[1]
    after_suffix = after_file.split(".")[1]

    if not before_suffix in file_suffix or not after_suffix in file_suffix:
        print("Invalid input")
        sys.exit()

    # compare the suffix
    if before_suffix != after_suffix:
        print("Input and Output have different extensions")
        sys.exit()

def file_change():
    before_file = sys.argv[1]
    after_file = sys.argv[2]

    people_image = Image.open(before_file)
    shirt_image = Image.open("./shirt.png")
    shirt_image = ImageOps.fit(shirt_image, people_image.size)
    people_image.paste(shirt_image, (150,-150), shirt_image)
    people_image.save(after_file)

def main():
    check_file_arguments()
    file_change()

main()
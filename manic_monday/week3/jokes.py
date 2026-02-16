import sys
from pyjokes import pyjokes
default = "en"
LANGUAGES = ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "ru", "sv"]
def read_arg():
    if len(sys.argv) < 2:
        return default
    arg = sys.argv[1]
    if not arg.startswith("-"):
        return default
    lang = arg[1:].lower()
    if lang not in LANGUAGES:
        return default
    return lang     


def get_single_joke(lang):
    # check current lang wether is in LANGUAGES list
    if lang not in LANGUAGES:
        return "Bad joke"
    try:
        return pyjokes.get_joke(language=lang)
    except Exception:
        return "Bad joke"   
         

def main():
    lang = read_arg()
    joke = get_single_joke(lang)
    print(joke)

if __name__ == "__main__":
	main()

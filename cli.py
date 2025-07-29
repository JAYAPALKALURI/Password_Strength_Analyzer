# cli.py
import argparse
from analyzer import analyze_password
from wordlist_generator import generate_wordlist, save_wordlist

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer & Wordlist Generator")
    parser.add_argument("--password", help="Password to analyze", required=False)
    parser.add_argument("--inputs", nargs='*', help="Custom inputs like name, pet, birthdate", required=False)
    parser.add_argument("--export", help="Export wordlist to file", action="store_true")

    args = parser.parse_args()

    if args.password:
        result = analyze_password(args.password)
        print(f"\nPassword: {result['password']}")
        print(f"Score: {result['score']}/4")
        print(f"Estimated Crack Time: {result['crack_time']}")
        print("Suggestions:", *result['suggestions'], sep="\n - ")

    if args.inputs:
        wordlist = generate_wordlist(args.inputs)
        print(f"\nGenerated {len(wordlist)} wordlist entries.")
        if args.export:
            save_wordlist(wordlist)
            print("Wordlist saved to 'wordlists/custom_wordlist.txt'.")

if __name__ == "__main__":
    main()

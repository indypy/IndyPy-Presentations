import argparse

parser = argparse.ArgumentParser(
    description="A simple script to echo the first argument back to you",
    epilog="Enjoy!"
)
parser.add_argument("echo", help="echo the string you type here")
args = parser.parse_args()
print(args.echo)

import sys

usaage = """usage: oldskool.py echo

positional arguments:
  echo        echo the string you type here

"""

if len(sys.argv) != 2:
    print(usaage)
else:
    print(sys.argv[1])

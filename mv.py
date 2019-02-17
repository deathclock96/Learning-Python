from sys import argv
from os import remove

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
in_data = in_file.read()

print(f"The inpute file is {len{in_data} bytes long")

print("Ready, hit ENTER to continue, CTRL -C to abort:")
input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print("Alright, all done!")

out_file.close()
in_file.close()

os.remove(from_file)

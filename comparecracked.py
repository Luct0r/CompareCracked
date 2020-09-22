#!/usr/bin/env python3

dumpf = ("<FILE PATH>ntds.dit")
crackedf = ("<FILE PATH>crackedHashes.txt")

dump_array = []
cracked_array = []
cracked_count = 0

with open(dumpf) as file:
    for line in file:
        dump_array.append(line)

with open(crackedf) as file:
    for line in file:
        cracked_array.append(line)

for dump in dump_array:
    for cracked in cracked_array:
        cracked_hash = cracked.split(":")[0]
        cracked_pass = cracked.split(":")[1]
        if cracked_hash in dump:
            print(dump.rstrip("\n") + " --> " + cracked_pass)
            cracked_count = cracked_count + 1

possible_hashes = len(dump_array)

print("You've cracked " + str(cracked_count) + " of " + str(possible_hashes) + "!")

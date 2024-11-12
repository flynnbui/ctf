#!/usr/bin/env python3
import hashlib
import random

def sha256Hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def generateVariations(content):
    lines = content.split('\n')
    newLines = [line + ' ' if random.choice([True, False]) else line.rstrip() for line in lines]
    return '\n'.join(newLines)

def birthdayAttackMatch(originalContent, fakeContent, targetSuffixLength=4):
    seenHashes = {}

    while True:
        # generate a original variation 
        originalVariant = generateVariations(originalContent)
        originalHash = sha256Hash(originalVariant)
        originalSuffix = originalHash[-targetSuffixLength:]

        if originalSuffix not in seenHashes:
            seenHashes[originalSuffix] = {'type': 'original', 'content': originalVariant, 'hash': originalHash}
        else:
            # match from a previous fake variant check
            if seenHashes[originalSuffix]['type'] == 'fake':
                print("Match found!")
                print(f"Original Content Hash: {originalHash}")
                print(f"Fake Content Hash: {seenHashes[originalSuffix]['hash']}")

                # Save the matching contents
                with open('realConfessionMatch.txt', 'w', encoding='utf-8') as file:
                    file.write(originalVariant)
                with open('fakeConfessionMatch.txt', 'w', encoding='utf-8') as file:
                    file.write(seenHashes[originalSuffix]['content'])

                print("Matching files saved as 'realConfessionMatch.txt' and 'fakeConfessionMatch.txt'.")
                return

        # generate fake variation
        fakeVariant = generateVariations(fakeContent)
        fakeHash = sha256Hash(fakeVariant)
        fakeSuffix = fakeHash[-targetSuffixLength:]

        # store the fake variant and its hash 
        if fakeSuffix not in seenHashes:
            seenHashes[fakeSuffix] = {'type': 'fake', 'content': fakeVariant, 'hash': fakeHash}
        else:
            # macthing from a previous original variant check
            if seenHashes[fakeSuffix]['type'] == 'original':
                print("Match found!")
                print(f"Fake Content Hash: {fakeHash}")
                print(f"Original Content Hash: {seenHashes[fakeSuffix]['hash']}")

                # Save the matching contents
                with open('realConfessionMatch.txt', 'w', encoding='utf-8') as file:
                    file.write(seenHashes[fakeSuffix]['content'])
                with open('fakeConfessionMatch.txt', 'w', encoding='utf-8') as file:
                    file.write(fakeVariant)

                print("Matching files saved as 'realConfessionMatch.txt' and 'fakeConfessionMatch.txt'.")
                return

def main():
    inputFile = 'input.txt'  
    secondFile = 'fake.txt'

    with open(inputFile, 'rb') as file:
        originalContent = file.read().decode('utf-8')
    with open(secondFile, 'rb') as file:
        fakeContent = file.read().decode('utf-8')

    print("Starting birthday attack to match hash suffixes...")
    birthdayAttackMatch(originalContent, fakeContent)

if __name__ == "__main__":
    main()

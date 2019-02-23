# SmartHashCat

HashCat wrapper, encapsulating the use of CeWL, to efficiently crack passwords.

## Flow

1. Dictionary generation
2. Dictionary attack
3. Brute force 1-6 length passwords
4. Quick mask attack
5. Slow mask attack
6. Slower mask attack
    - Starts with bruteforce of 7 lenght passwords
7. Desesperate mask attack

## Installation
```
git clone URL
cd SmartHashCat
sh setup.sh
```

## Examples
- Complete attack:
```
SmartHashCat.py -n Example -u https://www.example.com -f hashes.txt
```

- Complete attack without CeWL:
```
SmartHashCat.py -n Example -f hashes.txt
```

- Start at Dictionnary attack phase and continue all the way to desperate mask attacks:
```
SmartHashCat.py -p 1 -f hashes.txt
```

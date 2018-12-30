from hashlib import sha256

def hashcreator(pw):
    pw_bytestring = pw.encode()
    return sha256(pw_bytestring).hexdigest()

yorumlar=[]
numara = 1
sifre = "378bc297aed78d68f2aa8dbb2064d8beb85f42fab45e1062e1749659a25b0524"

while True:
    kullanici_sifresi = input("Please enter the password to be allowed to comment: ")
    if str(hashcreator(kullanici_sifresi)) != sifre:
     while True:
        print("Sorry but you entered the wrong password :( Please try again.")
        break
    else:
     print("Correct password, WELCOME :) !")
     break 

while True:
    yorum= [input("Please leave a comment: ")]
    yorumlar = yorumlar + yorum
    print("All previous comments of yours: \n")
    for c in yorumlar:
        print(str(numara) + "- " + str(c) + "\n")
        numara = numara + 1
    numara=1
    l= input("Leave or stay?(Type 'L' or 'l' to leave, type anything else(or just press enter) to stay): ")
    if l=="L" or l=="l":
        break
    
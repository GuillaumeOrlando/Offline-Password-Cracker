import hashlib
import time

time1=time.time()

# Hashing functions
def encode_md5(plain_password):
    md5_password = hashlib.md5(plain_password).hexdigest()
    return md5_password

def encode_sha1(plain_password):
    sha1_password = hashlib.sha1(plain_password).hexdigest()
    return sha1_password

def encode_sha256(plain_password):
    sha256_password = hashlib.sha256(plain_password).hexdigest()
    return sha256_password

def encode_sha512(plain_password):
    sha512_password = hashlib.sha512(plain_password).hexdigest()
    return sha512_password

# Decode Functions
def decode_sha1(hash, e_sha1):
    if (hash == e_sha1):
        file_result.write(hash + ":" + plain_password + "\n")
        print("[Found] : " "sha1 " + hash + ":" + plain_password)
    return ()

def decode_sha256(hash, e_sha256):
    if (hash == e_sha256):
        file_result.write(hash + ":" + plain_password + "\n")
        print("[Found] : " "sha256 " + hash + ":" + plain_password)
    return ()

def decode_sha512(hash, e_sha512):
    if (hash == e_sha512):
        file_result.write(hash + ":" + plain_password + "\n")
        print("[Found] : " "sha512 " + hash + ":" + plain_password)
    return ()

def decode_md5(hash, e_md5):
    if (hash == e_md5):
        file_result.write(hash + ":" + plain_password + "\n")
        print("[Found] : " "md5 " + hash + ":" + plain_password)
    return ()

def close():
    file_result.close()
    fbis.close()
    f.close()
    return()

#Open Plain Text Passwords File
file_result = open("Result.txt", "w")
with open("list.txt", "r") as f :

    full_file = f.read()
    file = full_file.split("\n")

    #Open Hash File
    with open("hash.txt", "r") as fbis :

        full_hash_file = fbis.read()
        hash_file = full_hash_file.split("\n")

    # Encode Passwords
    for plain_password in file :
            e_sha1 = encode_sha1(plain_password)
            e_sha256 = encode_sha256(plain_password)
            e_sha512 = encode_sha512(plain_password)
            e_md5 = encode_md5(plain_password)

            # Decode Hash File
            for hash in hash_file:
                decode_sha1(hash, e_sha1)
                decode_sha256(hash, e_sha256)
                decode_sha512(hash, e_sha512)
                decode_md5(hash, e_md5)

close()
#Guessing Statistics
fd = open('hash.txt', 'r')
hash_nummber = 0
while fd.readline():
    hash_nummber += 1

fd = open('Result.txt', 'r')
hash_sucessfull = 0
while fd.readline():
    hash_sucessfull += 1

# print("[*] Number of hash : " + str(hash_nummber))
# print("[*] Number of hash sucessfully decrypt : " + str(hash_sucessfull))
percent = int(hash_sucessfull) * 100 / int(hash_nummber)
print("[*] Password found : " + str(percent) + "%")

time2=time.time()-time1
print("[*] Task completed in %f" %time2 + "s.")
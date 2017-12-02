import hashlib
import time
import argparse
import sys
import os.path

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
        if (verbose == True):
            print("[Found] : " "sha1 " + hash + ":" + plain_password)
    return ()

def decode_sha256(hash, e_sha256):
    if (hash == e_sha256):
        file_result.write(hash + ":" + plain_password + "\n")
        if (verbose == True):
            print("[Found] : " "sha256 " + hash + ":" + plain_password)
    return ()

def decode_sha512(hash, e_sha512):
    if (hash == e_sha512):
        file_result.write(hash + ":" + plain_password + "\n")
        if (verbose == True):
            print("[Found] : " "sha512 " + hash + ":" + plain_password)
    return ()

def decode_md5(hash, e_md5):
    if (hash == e_md5):
        file_result.write(hash + ":" + plain_password + "\n")
        if (verbose == True):
            print("[Found] : " "md5 " + hash + ":" + plain_password)
    return ()

def path_target(target):
    if (os.path.exists(target)):
        return()
    else:
        print("[Error] The target file does not exist")
    exit()

def path_password(password):
    if (os.path.exists(password)):
        return()
    else:
        print("[Error] The password file does not exist")
    exit()

def path_output(output):
    if (os.path.exists(output)):
        return()
    else:
        print("[Error] The output file does not exist")
    exit()


def close():
    file_result.close()
    fbis.close()
    f.close()
    return()


# Help
parser = argparse.ArgumentParser(description='Offline password cracking tool.')
parser = argparse.ArgumentParser()
parser.add_argument("-t","--target", help='Destination of the hash list.')
parser.add_argument("-p","--password", help='Destination of the plain text password list.')
parser.add_argument("-o", "--output", help='Destination of the output file.')
parser.add_argument("-v", "--verbose", action="store_true", help="Allow verbose mode")
parser.add_argument("-md5", "--MD5", action="store_true", help="Hash are only in md5 format")
parser.add_argument("-sha1", "--SHA1", action="store_true", help="Hash are only in sha1 format")
parser.add_argument("-sha256", "--SHA256", action="store_true", help="Hash are only in sha256 format")
parser.add_argument("-sha512", "--SHA512", action="store_true", help="Hash are only in sha512 format")
parser.add_argument("-u", "--UNKNOWN", action="store_true", help="Hash format is not known (default)")

args = parser.parse_args()

# Get Arguments
target = args.target
password = args.password
output = args.output
verbose = args.verbose
md5 = args.MD5
sha1 = args.SHA1
sha1 = args.SHA256
sha1 = args.SHA512
unknown = args.UNKNOWN

#Test Path
path_target(target)
path_password(password)
path_output(output)

#Open Plain Text Passwords File
file_result = open(output, "w")
with open(password, "r") as f :

    full_file = f.read()
    file = full_file.split("\n")

    #Open Hash File
    with open(target, "r") as fbis :

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
		if (unknown == True):
                	decode_sha1(hash, e_sha1)
                	decode_sha256(hash, e_sha256)
                	decode_sha512(hash, e_sha512)
                	decode_md5(hash, e_md5)
		elif (md5 == True):
			decode_md5(hash, e_md5)
		elif (sha1 == True):
			decode_sha1(hash, e_sha1)
		elif (sha256 == True):
			decode_sha256(hash, e_sha256)
		else:
			decode_sha512(hash, e_sha512)
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

import re
x = True

def main():

    fd = open('leak.txt', 'r')
    line_number = 0
    while (fd.readline()):
        line_number += 1

    print("[+] Start parsing data ...")
    b = 0

    output = open("final.txt", "w")
    with open("leak.txt", "r") as f :

         full_file = f.read()
         hash = full_file.split("\n")

         while (x == True):

            # print(hash[int(b)])
            a = re.split('MD5 |:|MD5PLAIN ', hash[int(b)])
            b += 1
            real_hash = a[1]
            # Visible Output
            output.write(real_hash + "\n")
            percent = b * 100 / line_number
            print("[" + str(percent) + "%" + "] " + real_hash)

if __name__ == '__main__':
    main()

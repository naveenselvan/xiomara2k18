import hashlib
from Crypto.Util.strxor import strxor

def bs(word, sum_chunk):
    bin_string = bin(int(sum_chunk,16))[2:].zfill(len(word)).replace("1", " ").replace("0", "\0")
    return strxor(word, bin_string)

flag = "xiomara{Xiomara_is_fun_indeed!_With_<3_Ronald_Rivest}\n"

print "\nWelcome to Rivomara Encryption System\n"
print "\nPress 1 to explore my system and 2 to submit your flag:\n"

try:
    option = raw_input("-->  ")
except:
    exit("\n")

if option == "1":
    while True:
        try:
            msg = raw_input("\nEnter your message:\n")
        except:
            exit("\n")

        sum = hashlib.md5(msg).hexdigest()

        s1 = ["hello", " hacker", "! ronald", " rivest", " here" ]
        s2 = ["this", " is a new algorithm", ", i've designed", " for the people", " of xiomara"]
        s3 = ["after", " a long", " time", " thinking", " about", " hashing", " , text", " steganography", ", et cetera"]
        s4 = ["hope", " you have", " fun time", " solving", " this", " challenge"]
        s5 = ["enjoy", " learning", " crypto", " and have", " a great", " day ahead"]
        s6 = ["goodbye"]

        c1 = ""
        c2 = ""
        c3 = ""
        c4 = ""
        c5 = ""
        c6 = ""

        for i in range(5):
            c1 = c1 + bs(s1[i], sum[i])
            c2 = c2 + bs(s2[i], sum[i+5])
        for i in range(9):
            c3 = c3 + bs(s3[i], sum[i+10])
        for i in range(6):
            c4 = c4 + bs(s4[i], sum[i + 19])
        for i in range(6):
            c5 = c5 + bs(s5[i], sum[i + 25])
        for i in range(1):
            c6 = c6 + bs(s6[i], sum[i + 31])

        print "\nRivomara encrypted text:\n"
        print c1
        print c2
        print c3
        print c4
        print c5
        print c6

elif option == "2":
    try:
        hashed = raw_input("\nYour flag:\n")
    except:
        exit("\n")
    if hashed == "96b8fe0349d4e7cec7be0148f5abaea0":
        print "\nCongrats!"
        print flag
    else:
        print "\nSorry hacker, wrong flag!\nGive it a shot once more\nI'm sure you can get it\n"

else:
    print "\nExiting due to invalid response!\n"
    exit()

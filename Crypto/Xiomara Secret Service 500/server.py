from Crypto.Random import random
from Crypto.Hash import SHA
from Crypto import Random
from Crypto.Cipher import AES
from time import sleep
from binascii import hexlify

def commentary(n):
    try:
        for i in range(1, 21):
            sleep(random.randint(0, 6))
            print("Traffic reached Server #" + str(i))
        print("Ctrl+C boy! INTERCEPT and INJECT!")
        exit()
    except KeyboardInterrupt:
        if i-1==n:
            print("\n\nGotcha! Intercepted:\n")
            return
        else:
            print("\nOops! Missed! Be alert to intercept at the right time!\n")
            exit()

def rev_commentary(n):
    try:
        for i in range(1, 21)[::-1]:
            sleep(random.randint(0, 6))
            print("Traffic reached Server #" + str(i))
        print("Ctrl+C boy! INTERCEPT and INJECT!")
        exit()
    except KeyboardInterrupt:
        if i+1==n:
            print("\n\nGotcha! Intercepted:\n")
            return
        else:
            print("\nOops! Missed! Be alert to intercept at the right time!\n")
            exit()

if __name__ == '__main__':
    try:
        n = random.randint(1, 19)

        print("\nWelcome to the Xiomara secret service!\n"
              "We have compromised server #"+str(n)+" for you!\n"
              "You are into it now, be ready to listen, and inject!\n")

        p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
        g = 2

        a = random.randint(0, p)
        A = pow(g, a, p)

        sleep(1)
        print("\nFBI sends its DH parameters to NSA!\n")
        commentary(n)

        print("g = "+str(g)+";\np = "+str(p)+";\nA = "+str(A)+";\n")
        M_A = raw_input("\nQuick! Inject your well crafted payload:\n")

        b = random.randint(0, p)
        B = pow(g, b, p)

        sleep(3)
        print("\nYay! Your payload has successfully reached the NSA!\n")

        if('g' not in M_A or 'p' not in M_A or 'A' not in M_A):
            sleep(1)
            print("\nOops! The NSA has detected that you have tampered the data! Run away for your lives!\n")
            exit()

        sleep(1)
        print("\nNSA sends its DH parameters to FBI!\n")

        rev_commentary(n)

        print("\nB = "+str(B)+";\n")
        M_B = raw_input("\nQuick! Inject your well crafted payload:\n")
        sleep(3)
        print("\nYay! Your payload has successfully reached the FBI!\n")

        if ('B' not in M_B):
            sleep(1)
            print("\nOops! The FBI has detected that you have tampered the data! Run away for your lives!\n")
            exit()

        M_B = int(M_B[4:-1])
        key_AM = str(pow(M_B, a, p))
        h = SHA.new()
        h.update(key_AM)
        key = h.digest()[0:16]
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ct = hexlify(iv + cipher.encrypt(b"If you read this message, you've successfully hacked us. Welcome to FBI! Here's your reward xiomara{w3_l057_0ur_1n736r17y_70_dh}"))

        sleep(1)
        print("\nFBI sends the 'secret' to NSA!\n")
        commentary(n)

        print("\nThe Secret: "+ct+"\n")
    except:
        exit()

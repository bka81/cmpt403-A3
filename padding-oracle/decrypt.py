import sys
import subprocess
import os


f = open(sys.argv[1], "rb")
ciphertext_data = f.read()
f.close()


#check the message padding:

msg = bytearray(b"When you see this, it's very likely that your decryption works. Congrats!")
print((len(msg))%16)


    

#PART 1: DECRYPT BYTE:

#extract last 16 bytes and the 16 bytes before that: 32 bytes in total
yN = ciphertext_data[-16:]
yN_prev = ciphertext_data[-32:-16]

# generate a random array of 16 bytes then change the last to try i value
block = bytearray(os.urandom(16))
for i in range(0,256):
    block[15] = i
    r_yN = block + yN
    with open("r_yN_file", "wb") as f:
        f.write(r_yN)
    output = subprocess.check_output(["python3","oracle.py","r_yN_file"])
    if output.strip() == b"1":
        for j in range(0, 16):
            block[j] = os.urandom(1)[0]
            r_yN = block + yN
            
            with open("r_yN_file", "wb") as f:
                f.write(r_yN)
            
            output = subprocess.check_output(["python3","oracle.py","r_yN_file"])
            
            if output.strip() == b"0":
                D_yN_16 = i ^ (17 - (j+1))
                break
            D_yN_16 = i ^ 1
        xN_16 = D_yN_16 ^ yN_prev[15]
        break
print (xN_16)


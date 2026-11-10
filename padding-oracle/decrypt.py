import sys
import subprocess
import os


f = open(sys.argv[1], "rb")
ciphertext_data = f.read()
f.close()


#check the message padding:

msg = bytearray(b"When you see this, it's very likely that your decryption works. Congrats!")



# Number of blocks in the ciphertext:
#PART 3: DECRYPT ALL THE BLOCKS:
open("plaintext.txt", "wb").close()
num_blocks = len(ciphertext_data) // 16
for c in range(0, num_blocks - 1):
    y_prev = ciphertext_data[(c * 16) : ((c + 1) * 16)] 
    y_curr = ciphertext_data[((c + 1) * 16) : ((c + 2) * 16)]
    

    #PART 1: DECRYPT BYTE:

    yN = y_prev
    yN_prev = y_curr

    # generate a random array of 16 bytes then change the last to try i value
    block_r = bytearray(os.urandom(16))
    for i in range(0,256):
        block_r[15] = i
        r_yN = block_r + yN
        with open("r_yN_file", "wb") as f:
            f.write(r_yN)
        output = subprocess.check_output(["python3","oracle.py","r_yN_file"])
        if output.strip() == b"1":
            for j in range(0, 16):
                block_r[j] = os.urandom(1)[0]
                r_yN = block_r + yN
                with open("r_yN_file", "wb") as f:
                    f.write(r_yN)
                
                output = subprocess.check_output(["python3","oracle.py","r_yN_file"])
                #oracle returned no:
                if output.strip() == b"0":
                    D_yN_16 = i ^ (17 - (j+1))
                    break
                #oracle returned yes:
                D_yN_16 = i ^ 1
            xN_16 = D_yN_16 ^ yN_prev[15]
            break
   

    D_yN = [D_yN_16]
    xN = [xN_16]

    #PART2: DECRYPT BLOCK:

    #1. Set r as (r1 |r2 | . . . |rk−1 |i|D(y)k+1 |D(y)k+2 | . . . |D(y)16 ⊕ (17 − k)). Initially i = 0.
    for k in range (14, -1 , -1):
        block_r[15] = D_yN_16 ^ (17 - (k + 1)) 
        for i in range(0,256):
            block_r[k] = i
            r_yN = block_r + yN
            with open("r_yN_file", "wb") as f:
                f.write(r_yN)
            output = subprocess.check_output(["python3","oracle.py","r_yN_file"])
            if output.strip() == b"1":
                D_yN.insert(0, i)
                xN.insert(0, (i ^ yN_prev[k]))
                block_r[k] = i
                break

    print(f"D_yN = {D_yN}")
    print(f"plaintext xN = {xN}")
    
    with open("plaintext.txt", "ab") as f:
        f.write(bytes(xN))







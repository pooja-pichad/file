# Aapke paas ek list hai. 
# Iss list mein har string ko ek file-question3.
# txt naam ki file mein nayi line mein daalo. Aapki list yeh rahi:
 
from os import write


banks_list = ["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda\n"] 
#banks_list=open("file-question3.text","w")
# banks_list.write("kotak\n")
# banks_list.write("HDFC\n")
# banks_list.write("RBL\n")
# banks_list.write("SBI\n")
# banks_list.write("Bank of Baroda")
# banks_list.close()
i=0
for i in banks_list:
    file=open("bank1.txt","a")
    file.write(i)
    file.close()

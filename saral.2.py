# Aapne jo pichle question mein (Question 1) file download kari hai, 
# usko read karke usme number of lines count kar ke print karein. 
# Aapne sirf uss file ki number of lines Count karne ka code likhna hai.
#  Hint: Har \n ke baad nayi line shuru hoti hai. Aap yeh use kar ke nayi 
#  line ka ko pehchan sakte ho.
# Edit on Github
my_file=open("people1.text","r")
c=0
for i in my_file:
    c=c+1
print(c)
my_file.close()
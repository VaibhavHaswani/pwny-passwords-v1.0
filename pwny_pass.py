# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:11:12 2020

@author: Vaibhav Haswani
"""

import hashlib
import requests
import sys

def req(passw):
	url='https://api.pwnedpasswords.com/range/'+passw                          #setting api with hash prefix
	res=requests.get(url)                                                      #getting response
	if res.status_code != 200:                                                 #raise execption if response not 200 
		raise RuntimeError(f"Error code:{res.status_code} \nPlease Check your api!!")
	return res

def api_response(hashes,tailhash):                                             #takes hash response suffix data and your passwd hash suffix
	hashes=[data.split(':') for data in hashes.splitlines()]                   #spliting hash data into list of hash suffix and counts 
	for hashd,count in hashes:                                                 
		if hashd==tailhash:                                                    #check if the suffix matches the record , return count then
			return count
	return 0	

def pwncheck(passw):
	sha_pass=hashlib.sha1(passw.encode('utf-8')).hexdigest().upper()            #converting password to required format as by api i.e SHA1 hash(requires utf-8 string and hexdigit format),uppercase  
	sha_head,sha_tail=sha_pass[:5],sha_pass[5:]                                 #slicing sha hash into suffix having first five digits of sha hash as required by api for k anonymity 
	res_data=req(sha_head).text                                                 #getting response data
	return api_response(res_data,sha_tail)                                      #return count if found


def result(passwd):
	out=pwncheck(passwd)
	if out==0:
		print("\n\nMYou Got lucky Buddy, NO PWNED RECORD FOUND !!")
	else:
		print(f"\n\nWTF! Go and change your password bitch , FOUND IN {out} PWNED RECORDS")

def main():
	print('''              Welcome  to  PwnyPasswords!!
                                   --By Vaibhav Haswani\n\n\n''')
	opt=None
	while opt!='q':
		passwd=input("Enter your password to check if pwned:")
		result(passwd)
		opt=input("\n...To check more passwords press any key...(q to quit)")
	else:
		print("GoodBye!!")
		sys.exit()
		
  

if __name__=='__main__':
	main()						
						
				 
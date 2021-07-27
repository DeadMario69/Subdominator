import requests
import argparse
from os import path

parser=parser.ArgumentParser()
parser.add_argument('-t' ,'--target', help='Add target')
parser.add_argument('-w' ,'--wordlist', help='Provide your wordlist')
parser=parser.parse_args()
	def main():
		if parser.target:
			if path.exists(parser.wordlist):
						wordlist= open(parser.wordlist, 'r')
	            		wordlist=wordlist.read().split('\n')
#HTTPS requests	            		
	            		for subdomain in wordlist:
	            			urls= "http://"+subdomain+"."+parser.target
	            			try:
	            				requests.get(urls)
	            			except requests.ConnectionError:
	            				pass
	            			else:
	            				print("(+) Subdomain exist:" + urls)
	       #HTTP requests
	            				
	            				for subdomain in wordlist:
	            			url= "http://"+subdomain+"."+parser.target
	            			try:
	            				requests.get(url)
	            			except requests.ConnectionError:
	            				pass
	            			else:
	            				print("(+) Subdomain exist:" + url)
	            				
	            		if __name__=='__main__':
	            			try:
	            			  main()
	            			except KeyboardInterrupt:
	            				exit				
	            				
	            			
	            				
						
			
			
			
	

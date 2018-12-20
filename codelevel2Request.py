import requests

# Sloppy script to get, sort, and post the data

def sort(string):
	string = string.split(",")
	for i in range(len(string)):
		if(string[i]==" "):
			string[i]=0
		else:
			string[i]=int(string[i])
	for item in string:
                print(item)
	print '\n' 
#Do something for the space
	#for(i = 0; i<string.length;i++)

#First step - 32
#var str2 = new String()
	for i in range(len(string)):
		string[i]=string[i]-32
	for item in string:
                print(item)
	print '\n' 

#Second step original position
#for (var x=0;x<str1.length;x++)
#str2[x]=94-str2[x]
	for i in range(len(string)):
		string[i]=94-string[i]
	for item in string:
                print(item)
	print '\n' 

#Third step original ascii code
#for (var x=0;x<str1.length;x++)
#str2[x]=str2[x]+32
	for i in range(len(string)):
                string[i]=string[i]+32
	for item in string:
                print(item)
	print '\n' 

#Last step original ascii code to Char
#for (var x=0;x<str1.length;x++)
#str2[x] = String.fromCharCode(str2[x])
	for i in range(len(string)):
                if(string[i]==158):
                        string[i]=chr(32)
                else:
                        string[i]=chr(string[i])
	for item in string:
		print(item)
	string=''.join(string)
	return string

url = "https://www.hackthis.co.uk/levels/coding/2"
login = "https://www.hackthis.co.uk/?login"
payload = {"username": "pedromachuka", "password": "8caractere"}

s = requests.Session() # Start a session
s.post(login, data=payload) # Login
response = s.get(url).text # Get problem data
problem = response[response.find("<textarea>")+10:response.find("</textarea")] # Parse for words
solution = sort(problem) # Solve problem
payload = {"answer": solution}
s.post(url, data=payload) # Post data
response = s.get(url).text
if ("Incomplete" in response):
    print ":("
else:
	print "Sucessfully solved problem"


#algo debut resolv coding2 javascript

#Get the textarea
#var str1 = (document.getElementsByTagName('textarea')[0].value);
#str1 = str1.split(',')

#Make it in numbers
#for (var x=0;x<str1.length;x++)
#str1[x]=parseInt(str1[x])

#Do something for the space 

#First step - 32
#var str2 = new String()
#for (var x=0;x<str1.length;x++)
#str2[x]=str1[x]-32

#Second step original position
#for (var x=0;x<str1.length;x++)
#str2[x]=94-str2[x]

#Third step original ascii code
#for (var x=0;x<str1.length;x++)
#str2[x]=str2[x]+32

#Last step original ascii code to Char
#for (var x=0;x<str1.length;x++)
#str2[x] = String.fromCharCode(str2[x])

import requests

#Script to get an image with login

url = "https://www.hackthis.co.uk/levels/extras/captcha1.php"
login = "https://www.hackthis.co.uk/?login"
payload = {"username": "pedromachuka", "password": "8caractere"}

#Start a session
s = requests.Session()
#Login
s.post(login, data=payload) 
#Get img data
response = s.get(url, allow_redirects=True) 

#write img data
open('captcha1.png', 'wb').write(response.content)

#soumettre la réponse
payload = {"answer": solution}
s.post(url, data=payload) # Post data


#test validation du niveau
response = s.get(url).text
if ("Incomplete" in response):
    print ":("
else:
	print "Sucessfully solved problem"

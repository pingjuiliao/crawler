import requests

###########
### Simple Post
#######

# <h2>Tell me your name!</h2>
# <form method="post" action="processing.php">
                            ##################
# First name: <input type="text" name="firstname"><br>
# Last name: <input type="text" name="lastname"><br>
# <input type="submit" value="Submit" id="submit">
# </form>

params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
pageThatIsGonnaDirectedTo = "http://pythonscraping.com/files/processing.php"
r = requests.post(pageThatIsGonnaDirectedTo, data=params)
print(r.text)

###########
### File Upload
#######
files = {'uploadFile': open('./downloaded/img/lrg%20(1).jpg', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php", files= files)
print(r.text)


###########
### Cookie
#######

params = {'username': 'Ryan', 'password': 'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Coolie is set to:")
print(r.cookies.get_dict())
print("---------")
print("Going to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies= r.cookies)
print(r.text)



###########
### 
########


session = requests.session()
params = {'username': 'username', 'password': 'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Coolie is set to:")
print(s.cookies.get_dict())
print("---------")
print("Going to profile page...")
s = session.get("http://pythonscraping.com/pages/cookies/profiles.php")
print(s.text)

###########
###  Basic Access Authentication
########

from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('Ryan', 'password')
r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth = auth)
print(r.text)
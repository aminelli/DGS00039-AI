import re
text = "The web address is https://www.tutorialspoint.com"

# Taking "://" and "." to separate the groups 
result = re.search('([\w.-]+)://([\w.-]+)\.([\w.-]+)', text)
if result :
    print ("The main web Address: ",result.group())
    print ("The protocol: ",result.group(1))
    print ("The doman name: ",result.group(2) )
    print ("The TLD: ",result.group(3))

import re

if  re.search("tor", "Tutorial"):
        print ("1. search result found anywhere in the string")
        
if re.match("Tut", "Tutorial"):
         print ("2. Match with beginning of string" )
         
if not re.match("tor", "Tutorial"):
        print ("3. No match with match if not beginning" )

# Search as Match
        
if  not re.search("^tor", "Tutorial"):
        print ("4. search as match")
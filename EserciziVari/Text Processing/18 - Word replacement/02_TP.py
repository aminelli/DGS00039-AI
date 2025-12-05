import re
sourceline  = re.compile("Tutor", re.IGNORECASE)
 
Replacedline  = sourceline.sub("Tutor","Tutorialspoint has the best tutorials for learning.")
print (Replacedline)
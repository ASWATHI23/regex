import re
txt="Python is simple"
x=re.search("^Python",txt)
if x:
    print("found")
else:
    print("not found")
print("................")
import re
txt="Python is simple"
x=re.search("[is]",txt)
if x:
    print("found")
else:
    print("not found")
print(".....................")
import re
txt="Python is simple"
x=re.search("simple$",txt)
if x:
    print("found")
else:
    print("not found")
print("...................")
import re
txt="Python is simple"
x=re.search("[^sim]",txt)
if x:
    print("found")
else:
    print("not found")
print(".................")
import re
txt="Python is simple"
x=re.search("Pyth?.n",txt)
if x:
    print("found")
else:
    print("not found")
print("...................")
import re
txt="Python is simple"
x=re.search("Pyt.+n",txt)
if x:
    print("found")
else:
    print("not found")
print("................")
import re
txt="Python is simple"
x=re.search("Pyt.*n",txt)
if x:
    print("found")
else:
    print("not found")


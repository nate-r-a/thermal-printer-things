# curl http://www.google.com/finance/info?q=VSGAX

import requests
r = requests.get('http://www.google.com/finance/info?q=VSGAX')
r = r.text[4:]
print(r)
arr = eval(r)
d = dict(arr[0])
print(d)
print(d["t"])
print(d["l_cur"] + "   " + (d["c"]) + " (" + d["cp"] + ")")
print("Last updated .........")
# print(d[""])
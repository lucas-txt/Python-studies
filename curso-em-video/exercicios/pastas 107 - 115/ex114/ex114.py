import urllib
import urllib.request

try:
    site = urllib.request.urlopen(r'http://www.pudim.com.br')
except:
    print('deu erro')
else:
    print('tudo ok, o site pudim esta no ar')
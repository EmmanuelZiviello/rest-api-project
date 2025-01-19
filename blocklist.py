'''
blocklist.py
This file contains the blocklist of jwt tokens.It will be imported by app and the logout resource so that 
tokens can be added to the blocklist when the user logs out
'''
BLOCKLIST=set()#servirebbe un database  per salvare i jwt bloccati
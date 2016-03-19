Shamir's Secret Sharing

Will take in a Secret and produce X number of secret parts.
The app will be Distributed, using sockets to communicate with all clients.

Server: hawk.cs.umanitoba.ca port 5252
Clients: Anyone else


We should probably do this for the sockets:
http://code.activestate.com/recipes/531824/
     with Select, seems to support multi-connections which is what we'll need anyways...

To run, you just have to run Dealer.py (The Server) and Client.py.
They run just on localhost for the time being

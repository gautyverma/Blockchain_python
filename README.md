Make a virtual enviroment first using python

***ACTIVATE THE ENVIROMENT***

''' after moving to the location proceed these steps

"cd Da-coins"
".\blockchain-env\Scripts\activate"

 '''
***For running python on CMD***
'''
python -m backend.blockchain.block

'''

***Run the tests***
make sure to activate the virtual enviroment
"""
 python -m pytest backend/tests
"""

***Run Application and API***
"""
python -m backend.app
"""
*** Run a peer instance ***
"""
set PEER = True &&pyhton -m backend.app
"""

***RUN the FRONTEND ***
In the frontend directory:
'''
npm run start
'''

*** Seed the backend with data***
Make sure to activate the VE
'''
export SEED_DATA=True && python -m backend.app
'''
![image](https://github.com/gautyverma/Da-Coins/blob/master/Screenshot%20(80).png)
![image](https://github.com/gautyverma/Da-Coins/blob/master/Screenshot%20(81).png)

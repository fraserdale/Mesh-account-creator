# Mesh-account-creator
Account creator for mesh group. Size, JDsport and FootPatrol. Mobile accounts
For multiple accounts created, they are wrote to an external file.

## Single account:
For single account creation, enter email desired into the config.json file. Also fill out the rest of config.json with correct info
Then run JDSingle/SizeSingle/FootpatrolSingle
This will create you one mobile account for the site that you selected when running the selected script.

## Multiple accounts:
You need a catch all email domain. You can buy these very cheap on namecheap.com also easy to setup, just look it up
Fill out config.json with all correct information. 
For the email address in config.json put your catchall domain eg 'fraser.com' when you run the script this will create accounts with email addresses with that domain eg '638293@fraser.com, 847018@fraser.com'
If you want a prefix infront, in config.json put the prefix@domain eg 'clothes@fraser.com' this will create emails like this 'clothes+748204@fraser.com,clothes+735142@fraser.com'

You can now run any of the JDMulti/SizeMulti/FootpatrolMulti
The script will ask how many accounts you want and if you want random passwords or the one you set in config.json
The accounts created will be saved with passwords in corresponding accounts files.




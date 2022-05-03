# BloodhoundQuery
A little program to parse and query Bloodhound data

Inspired by Ippsecs video https://www.youtube.com/watch?v=o3W4H0UfDmQ and the horrible UI of jq I decided to make my own program with even worse UI. Its meant for getting simple data from Bloodhound.zip so you dont have to run Bloodhound just to list some user names.

When run without the `-i` parameter you get premade lists of queries.

This whole thing is very much WIP and might or might not die in side-project hell. If I decide to continue this there will be SQL support at some time as well as better UI code.

```
usage: bloodhound_query.py [-h] [-f F] [-i]

options:
  -h, --help  show this help message and exit
  -f F        Path to BloodHound.zip
  -i          Opens interactive mode which lets you parse the data by hand.


```
```
python bloodhound_query.py
choose item:
0 - IppsecVideoQueries
choose: 0
choose item:
0 - computers_with_os
1 - disabled_users
2 - enabled_users
3 - kerberoastable_users
4 - last_logon
5 - never_logged_on
6 - usernames_descriptions
7 - usernames_only_valid_descriptions
choose:
```

```
python bloodhound_query.py -i
Welcome to Bloodhound Query - type help for help
>help
get_users - Get user data with keys try: get_users name description enabled
keys_users - Show all available keys of the user struct try: keys_users
must - Filter the data by a key with a value try: must enabled True
not - Filter the data by a key with a value try: not enabled False
users - Get all user data try: users
computers - Get all computer data try: computers
print - Print the data previously gotten try: print
pretty - Print the data neatly: pretty
one - Print the first element of the data previously gotten try: one
Accumulator has 0 items
>keys_users
{
    "Aces": {
        "IsInherited": "bool",
        "PrincipalSID": "str",
        "PrincipalType": "str",
        "RightName": "str"
    },
    "AllowedToDelegate": "list",
    "HasSIDHistory": "list",
    "IsACLProtected": "bool",
    "IsDeleted": "bool",
    "ObjectIdentifier": "str",
    "PrimaryGroupSID": "str",
    "Properties": {
        "admincount": "bool",
        "description": "str",
        "displayname": "str",
        "distinguishedname": "str",
        "domain": "str",
        "domainsid": "str",
        "dontreqpreauth": "bool",
        "email": "str",
        "enabled": "bool",
        "hasspn": "bool",
        "highvalue": "bool",
        "homedirectory": "NoneType",
        "lastlogon": "int",
        "lastlogontimestamp": "int",
        "name": "str",
        "passwordnotreqd": "bool",
        "pwdlastset": "int",
        "pwdneverexpires": "bool",
        "sensitive": "bool",
        "serviceprincipalnames": "list",
        "sfupassword": "NoneType",
        "sidhistory": "list",
        "title": "NoneType",
        "trustedtoauth": "bool",
        "unconstraineddelegation": "bool",
        "unicodepassword": "NoneType",
        "unixpassword": "NoneType",
        "userpassword": "NoneType",
        "whencreated": "int"
    },
    "SPNTargets": "list"
}
Accumulator has 0 items
>


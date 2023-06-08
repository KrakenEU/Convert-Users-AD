# Convert-Users-AD
Convert Users format (Name Surname) in valid Active Directory Users

Many times doing an AD pentest we need to create a few combinations of users we found in a web, that´s what this simple script does.

It creates a few combinations of user name+surname that are likley to appear in an AD enviroment

## USAGE:

```python3 convert-users-AD.py -h```

```
[+] USAGE

> python3 convert-users-AD.py Users_file.txt


[+] Users_file.txt format:

Username1 Surname1
Username2 Surname2
Username3 Surname3
...
``` 

## Example with test.txt:

```cat test.txt```

```
Aileen Wallace
Charlotte Hall
Evan Davies
Ieuan Monks
Joshua Morgan
Lois Hopkins
```

## RUN

``` python3 convert-users-AD.py test.txt ```

```
AileenWallace
AWallace
AileenW
A.Wallace
Aileen.W
CharlotteHall
CHall
CharlotteH
C.Hall
Charlotte.H
EvanDavies
EDavies
EvanD
E.Davies
Evan.D
IeuanMonks
IMonks
IeuanM
I.Monks
Ieuan.M
JoshuaMorgan
JMorgan
JoshuaM
J.Morgan
Joshua.M
LoisHopkins
LHopkins
LoisH
L.Hopkins
Lois.H
```

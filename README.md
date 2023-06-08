# Convert-Users-AD
Convert Users format (Name Surname) in valid Active Directory Users

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

Aileen Wallace

Charlotte Hall

Evan Davies

Ieuan Monks

Joshua Morgan

Lois Hopkins

## RUN

``` python3 convert-users-AD.py test.txt ```

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

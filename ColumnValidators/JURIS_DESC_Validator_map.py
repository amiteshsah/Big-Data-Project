#!/usr/bin/env python
import sys
import string
import os
import datetime
import difflib
import csv
import re



juris = ["DEPT OF CORRECTIONS","HEALTH & HOSP CORP","N.Y. HOUSING POLICE", "N.Y. POLICE DEPT","N.Y. TRANSIT POLICE","NYS DEPT TAX AND FINANCE",
"OTHER","TRI-BORO BRDG TUNNL","U.S. PARK POLICE","AMTRACK", "CONRAIL", "FIRE DEPT (FIRE MARSHAL)","METRO NORTH",
"N.Y. STATE PARKS","NEW YORK CITY SHERIFF OFFICE","NYC DEPT ENVIRONMENTAL PROTECTION","SEA GATE POLICE DEPT","STATN IS RAPID TRANS",
"DISTRICT ATTORNEY OFFICE","LONG ISLAND RAILRD","N.Y. STATE POLICE","NYC PARKS", "NYS DEPT ENVIRONMENTAL CONSERVATION","POLICE DEPT NYC",
"PORT AUTHORITY"
]


def juris_desc_Validator(value):
    helper = True
    JURIS_DESC = value
    # key,value = line.split("\t")
    if len(JURIS_DESC) == 0:
        return JURIS_DESC + "\t" + "TEXT JURIS_DESC, NULL"
    else:
        for i in juris:
            seq = difflib.SequenceMatcher(None, i, value,)
            if(seq.ratio() > 0.7):
                return JURIS_DESC + "\t" + "TEXT JURIS_DESC, VALID"
            else:
                pass
        return JURIS_DESC + "\t" + "TEXT JURIS_DESC, INVALID"



for line in sys.stdin:
    data = list(csv.reader([line], delimiter=','))[0]
    JURIS_DESC = data[12]
    print(juris_desc_Validator(JURIS_DESC))

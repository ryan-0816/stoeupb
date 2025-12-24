from more_phrasing import *

phrases={}

for starter in STARTERS:
    starter = starter + '-'
    for middle in MIDDLES:
        for structure in STRUCTURES:
            for ender in ENDERS:
                steno = (starter+middle+structure+ender).replace('**','*')

                if any(char in steno for char in 'AO*EU'):
                    steno = steno.replace('-', '')

                try:
                    phrases[steno] = lookup([steno])
                except KeyError:
                    pass

for starter in SIMPLE_STARTERS:
    starter=starter+'-'
    for negation in ['','*']:
        for middle in SIMPLE_PRONOUNS:
            for structure in SIMPLE_STRUCTURES:
                for ender in ENDERS:

                    steno = (starter+negation+middle+structure+ender).replace('**','*')

                    if any(char in steno for char in 'AO*EU'):
                        steno = steno.replace('-', '')

                    try:
                        phrases[steno] = lookup([steno])
                    except KeyError:
                        pass

import json
with open("my-jeff.json", "w") as outfile:
    json.dump(phrases, outfile, indent=0)
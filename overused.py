import re

tests = {
    #REMOVE
    'Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.' : 'should be removed',
    'buffalo buffalo' : 'should be removed',
    #OK
    'buffalo and a buffalo' : 'should NOT be removed',
    'buffalo buff aloe' : 'should NOT be removed',
    #REMOVE
    'joint support joint support' : 'should be removed',
    'joint support for joint support' : 'should be removed',
    'there is joint support for joint support for joint support': 'should be removed',
    #OK
    'joint support joined sub port' : 'should NOT be removed',
    'joint joint support support' : 'should NOT be removed',
    #REMOVE
    'bipolar bi-polar' : 'should be removed',
    'bi-polar bi polar' : 'should be removed',
    'bipolar bi-polar bi polar bear' : 'should be removed',
    #OK
    'bipolar buy pole air' : 'should NOT be removed',
    #REMOVE
    'Legless Lego Legolas Lego Lass Lego Lasso' : 'should be removed',
    'Legless legolas' : 'should be removed',
    'Legless lego lass' : 'should be removed',
    'Legolas lego lass' : 'should be removed',
    #OK
    'Legolas teen imp act lego lasting impact' : 'should NOT be removed',
    #REMOVE
    'A shipping ship shipping shipping ships' : 'should be removed',
    'shipping shipping' : 'should be removed',
    'Shipping ships shipping ships' : 'should be removed',
    #OK
    'shipping ship ping' : 'should NOT be removed',
    'shipping this and shipping that' : 'should NOT be removed',
    #REMOVE
    'Fish and And and And and Chips' : 'should be removed',
    'and and and' : 'should be removed',
    #OK
    'and and' : 'should NOT be removed',
    #REMOVE
    'Liam Neeson sneezes on his niece''s knees on Es on a Nissan, onii-san~~' : 'should be removed',
    'Knees on neeson' : 'should be removed',
    #REMOVE
    'James, while John had had "had", had had "had had". "Had had" had had a better effect on the teacher.' : 'should be removed',
    'had had had' : 'should be removed',
    #OK
    'had had' : 'should NOT be removed',
    #REMOVE
    'One-one won one race, Two-two won one too.' : 'should be removed',
    'One won one' : 'should be removed',
    'Juan won one race, Tutu won one too' : 'should be removed',
    'Juan won one' : 'should be removed',
    #REMOVE
    'Awful lawful offal falafel waffles' : 'should be removed',
    'Awful lawful waffle' : 'should be removed',
    'Awful lawful falafel' : 'should be removed',
    'Awful lawful' : 'should be removed',
    #OK
    'Awfully lawful Lee' : 'should NOT be removed',
    #REMOVE
    'Rhabarberbarbara' : 'should be removed',
    #REMOVE
    'Low-Cal Calzone Zone' : 'should be removed',
    'calzone zone' : 'should be removed',
    #REMOVE
    'Real eyes realize real lies' : 'should be removed',
    'realize real lies' : 'should be removed',
    #OK
    'Realizing real lies sing' : 'should NOT be removed',
    #REMOVE
    'Condescending con descending' : 'should be removed',
    'con descending, condescending' : 'should be removed',
    #REMOVE
    'Will Reed will read Will''s wills' : 'should be removed',
    'Will reed will read' : 'should be removed',
    'Will will will' : 'should be removed',
    #OK
    'Will will' : 'should NOT be removed',
    #REMOVE
    'will smith and his friend will smith' : 'should be removed',
    'will smith will smith' : 'should be removed',
    'will will smith smith' : 'should be removed',
    'Will Smith will smith will.' : 'should be removed',
    'Will smith Will smith Will Smith "Will''s Myth"?': 'should be removed',
    #OK
    'will smith will''s myth' : 'should NOT be removed',
    #REMOVE
    'My micro Mike Row crow''s mic row rows my micro Mike Rowe crow.' : 'should be removed',
    'Micro mike rowe' : 'should be removed',
    #OK
    'Micro machine my chroma sheen' : 'should NOT be removed',
    #REMOVE
    'Police police police police police' : 'should be removed',
    'Police police police' : 'should be removed',
    'Policemen police men' : 'should be removed',
    #OK
    'Police police' : 'should NOT be removed',
    'swarming policemen police men swore Ming' : 'should NOT be removed',
    #REMOVE
    'Snowden''s snowed in' : 'should be removed',
    'Snowed-in Snowden' : 'should be removed',
    #OK
    'Snowden, he''s no Denny''s.' : 'should NOT be removed',
    #REMOVE
    '"Prince died" - dyed prints' : 'should be removed',
    #OK
    'Prince Opal Lee Prints a pulley' : 'should NOT be removed',
    #REMOVE
    'Cruz''s cruise crews'' cruze' : 'should be removed',
    #REMOVE
    'ajar Jar-Jar jars jars' : 'should be removed',
    #REMOVE
    'Reservation reservation' : 'should be removed',
    #OK
    'Reservation: Hyatt, Wayne?  Reserve a Shania Twain.' : 'should NOT be removed',
    #REMOVE
    'Jack Black''s blackjack' : 'should be removed',
    #REMOVE
    'Retiring retired tires' : 'should be removed',
    'Retiring re-tired tires' : 'should be removed',
    'tire tire tire' : 'should be removed',
    #OK
    'Retirement meant tired mint' : 'should NOT be removed',
    #REMOVE
    'Invest in vests' : 'should be removed',
    #REMOVE
    'Caesar sees her seize her seizure.' : 'should be removed',
    #REMOVE
    'Bear Grylls, bare, grills bare-grills bear' : 'should be removed',
    #REMOVE
    'Link''s lynx links links' : 'should be removed',
    'Linkin'' Park parked their Lincoln in Lincoln Park.' : 'should be removed',
    #OK
    'Linkin Logs\'ll ink in logs' : 'should NOT be removed',
    #REMOVE
    'Xbox One X' : 'should be removed',
    #REMOVE
    'complex complex' : 'should be removed',
    #REMOVE
    'A noisy noise annoys an oyster' : 'should be removed',
    #REMOVE
    'enemy anemone' : 'should be removed',
    #OK
    'enemy enemy an Emmy' : 'should NOT be removed',
    'anemone any money anemone' : 'should NOT be removed',
    #REMOVE
    'Putin, poutine, or a poo-tin.' : 'should be removed',
     'Putin\'s poutine' : 'should be removed',
    'carrion carry-on.' : 'should be removed'
}

patterns = [
    #"Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo."
    '(buffalo\W*){2,}',
    #"joint support for joint support for joint support for the bipolar bi-polar bi polar bear"
    '^(?=(.*joint\W+support){2,})',
    '^(?=(.*bi\W*polar){2,})',
    #"Legless Lego Legolas' Lego Lass' Lego Lasso"
    '((legless|legolas|lego\W+lass)\W*){2,}',
    #"A shipping ship shipping shipping ships"
    '(?=(.*(shipping)){3,})|(shipping\W*){2,}',
    '((shipping\Wships)\W*){2,}',
    #"Fish and And and And and Chips", or any of its variants. We've done it to death.
    '(and\W*){3,}',
    #"Liam Neeson sneezes on his niece's knees on Es on a Nissan, onii-san~~"
    '((neeson|sneezes?\W+on|knees\W+on|nissan)\W*){2,}',
    #"James, while John had had "had", had had "had had". "Had had" had had a better effect on the teacher."
    '(had\W*){3,}',
    #"One-one won one race, Two-two won one too." Also to include variations with "Juan".
    '(one|juan)\W+won\W+one',
    #"Awful lawful offal falafel waffles". We've done this to death too.
    '((awful|lawful|offal|falafel|waffle)\W*){2,}',
    #"Rhabarberbarbara"
    'Rhabarberbarbara',
    #"Low-Cal Calzone Zone". Done to death.
    '((calzone|cal|zone)\s*){2,}',
    #"Real eyes realize real lies"
    '((Real eyes|realize|real lies)\W*){2,}',
    #"Condescending con descending". Done to death.
    '((Condescending|con\W+descending)\W*){2,}',
    #Anything pertaining to Will's last testament (especially if his last name is Reed). We've had way too many variations on the theme!
    '((Will\W*Re[ea]d)\W*){2,}',
    '((Will)\W*){3,}',
    #Anything pertaining to Will Smith. Done to death.
    '^(?=(.*will){2,})(?=(.*smith){2,})',
    #"My micro Mike Row crow's mic row rows my micro Mike Rowe crow."
    '((Micro|mike row|mic crow|mic row|mike crow)\W*){2,}',
    #"Police police police police police". Done to death.
    '(police\W*){3,}',
    '^(\W*police\W*men\W*){2,}',
    #Anything about Edward Snowden's makeshift igloo.
    '^(?=(.*(Snowden|snowed\W*in)){2,})',
    #Anything about the death of Prince.
    '((Prince\W*died|prints\W*dyed|dyed\W*prints)\W*){2,}',
    #Anything about Senator Cruz's cruise ship, his crews, his Cruze, or his friend Tom Cruise.
    '^(?=(.*(Cruise|crew.?s|cruze?)){3,})',
    #Please, no more ajar Jar-Jar jars!
    '((jar\W*jar|a?jar)\W*){3,}',
    #"Reservation reservation reservation". If you're going to use this, you better get far more creative with it.
    '(reservations?\W*){2,}',
    #Anything about Jack Black's blackjack, him being secretly black, or him eating Cracker Jacks.
    '((black\W*jack\W*s?|jack\W*black\W*s?)\W*){2,}',
    #Either of the two E*TRADE commercials we currently know about.
    '(((re-?)?tir(e[ds]?|ing))\W*){3,}',
    '((in\W*vests?)\W*){2,}',
    #"Caesar sees her seize her seizure."
    '((Ceasar|seizure|seize\W*her)\W*){2,}',
    #"Bear Grylls, bare, grills bare-grills bears" or anything else involving him and bears cooking in various states of undress.
    '^(?=.*((bear|bare)\W*gr[yi]lls|gr[iy]lls\W*(bear|bare))\W*){2,}',
    #Anything involving Link, links, and Linkin' Park parking their Lincoln in Lincoln Park.
    '((l(ink|ynx)(in|s)?)\W*){3,}',
    '^(?=.*(linkin\W*park|lincoln)){2,}',
    #Please, no more submissions regarding the XBox One X. Unless they're really really long.
    'xbox\W*one\W*x',
    #"Complex complex complex" or similar.
    '((complex)\W*){2,}',
    #"A noisy noise annoys an oyster" and any of it's many boisterous variants.
    '((nois[ey]|annoys|an\W*oyster)\W*){3,}',
    #Any avalanches using "enemy anemone" as a repeating unit.
    '(enemy.*?anemone)|(anemone.*?enemy)',
    #Any avalanches involving Putin, poutine, or a poo-tin.
    '^(?=(.*p(u|oo|ou)\W*?tin)){2,}',
    #Any avalanches involving a carrion carry-on.
    '^(?=(carr[iy]\W*?on)){2,}'
]

passcount = 0
for test, result in tests.items():
    verdict = "should NOT be removed"
    for pattern in patterns:
        if re.search(pattern, test, re.IGNORECASE):
            verdict = "should be removed"
    if verdict == result:
        passcount += 1
    else:
        print('FAILED TEST   "' + test + '"')
print(str(passcount) + ' of ' + str(len(tests)) + ' tests passed')

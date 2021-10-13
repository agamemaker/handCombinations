#outdated
FOREST = "Forest"
MOUNTAIN = "Mountain"
SWAMP = "Swamp"
RITUAL = "Ritual"
CHANCELOR = "Chancellor of the Tangle"
SIMIAN = "Simian Spirit Guide"
MAP = "Renegade Map"
MANAMORPHOSE = "Manamorphose"
WRAITH = "Street Wraith"
REFORGE = "Reforge the Soul"
PACT = "Pact of Negation"
SIDEBOARD = "sideboard"
BELCHER = "Goblin Charbelcher"
RECROSS = "Recross the Paths"
LAY_OF_THE_LAND = "layOfTheLand"
ATTUNE = "Attune with Aether"
CARAVAN = "Caravan Vigil"
OPEN = "Open the Gates"
TRAVERSE = "Traverse the Ulvenwald"
SPY = "Balustrade Spy"
UNDERCITY = "Undercity Informer"
PENTAD = "Pentad Prism"
TALISMAN = "Talisman of Resilience"
DOMINANCE = "Talisman of Dominance"
SPHERE = "Sphere of the Suns"
POWDER = "Serum Powder"
ORACLE =  "Thassa's Oracle"
JOURNEY = "Memory's Journey"
UNEARTH = "Unearth"

#Flip Lands

#W
EMERIA = "Emeria's Call"

#U
SEAGATE = "Sea Gate Restoration"

#B
AGADEEM = "Agadeem's Awakening"
PELAKKA = "Pelakka Predation"
MAULING = "Hagra Mauling"

#R
SHATTER = "Shatterskull Smashing"
VALAKUT = "Valakut Awakening"
SPIKE = "Spikefield Hazard"
SONG = "Song-Mad Treachery"

#G
TIMBER = "Turntimber Symbiosis"
BALA = "Bala Ged Recovery"
TANGLE = "Tangled Florahedron"

#Rituals
DESPERATE = "Desperate Ritual"
PYRETIC = "Pyretic Ritual"
FEAT = "Irencrag Feat"

#Mana Fixers
STRIKE = "Strike it Rich"
CANTOR = "Wild Cantor"

#Interaction
LEYLINE = "Leyline of Sanctity"
SEIZE = "Thoughtseize"
MOON = "Blood Moon"

#Plunge shenanigans
PLUNGE = "Infernal Plunge"
TITAN = "Pact of the Titan"
THOPTER = "Ornithopter"

########################################

FINISHER =[BELCHER, RECROSS, UNDERCITY, SPY]
LOTL =[TRAVERSE, MAP, CARAVAN, ATTUNE, OPEN, LAY_OF_THE_LAND]
BASICLAND = [FOREST, MOUNTAIN, SWAMP]
ACCELERANT = [SIMIAN, DESPERATE, PYRETIC, PENTAD, TALISMAN, CANTOR]
CANTRIP =[MANAMORPHOSE, WRAITH]
COMBO = []
INTERACTION = [PACT, LEYLINE, SEIZE]

########################################


############################################

WHITEMANA = [EMERIA]
BLUEMANA = [SEAGATE]
BLACKMANA = [AGADEEM, PELAKKA, MAULING]
REDMANA = [SHATTER, VALAKUT, SPIKE, SONG]
GREENMANA = [TIMBER, BALA, TANGLE]
LAND = WHITEMANA + BLUEMANA + BLACKMANA + REDMANA + GREENMANA
UNTAPPEDLAND = [EMERIA, SEAGATE, AGADEEM, SHATTER, TIMBER]

RITUAL2 = [DESPERATE, PYRETIC]
CSHIFTR = [MANAMORPHOSE, STRIKE, CANTOR]

############################################

def handContains(search, hand):
    for card in search:
        if card in hand:
            return True
    return False

def handCount(search, hand):
    count = 0
    for card in search:
        count += hand.count(card)
    return count

### One off conditions

def hasFullPlunge(hand):
    return PLUNGE in hand and (TITAN in hand or THOPTER in hand)

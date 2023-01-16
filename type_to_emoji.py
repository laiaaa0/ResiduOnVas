def emoji_from_type(residu_destination):
    type_to_emoji={
    'Fracció orgànica (marró)' : '\U0001F7EB', 
    'Deixalleria / Punt Verd ': '\U0000267B', 
    'Vidre (verd)':'\U0001F7E9',
    'Medicaments ':'\U0001F48A', 
    'Fracció resta (gris)':'\U0001F5D1', 
    'Contenidor  Roba ':'\U0001F455',
    'Envàs lleuger (groc)':'\U0001F7E8', 
    'Deixalleries especifiques':'', 
    'Contenidors Piles':'\U0001F50B',
    'Paper i cartró (blau)':'\U0001F7E6'}

    if residu_destination in type_to_emoji:
        return type_to_emoji[residu_destination]
    print(f"Could not find {residu_destination}")
    return ""

if __name__=="__main__":
    ll=['', 'Envàs lleuger (groc)', 'Contenidor  Roba ', 'Medicaments ', 'Nom il·lustració', 'Paper i cartró (blau)', 'Contenidors Piles', 'Fracció resta (gris)', 'Fracció orgànica (marró)', 'Deixalleria / Punt Verd ', 'Vidre (verd)', 'Deixalleries especifiques']
    for val in ll:
        print(emoji_from_type(val))

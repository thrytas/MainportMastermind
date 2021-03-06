outcomes = {
    '1-1': 'Storm, sla een beurt over', 
    '1-2': 'Zet twee stappen met een schip naar keuze',
    '1-3': 'Zet drie stappen met een schip naar keuze',
    '1-4': 'Zet vier stappen met een schip naar keuze',
    '1-5': 'Zet vijf stappen met een schip naar keuze',
    '1-6': 'Gooi nog een keer met een dobbelsteen voor de kansuitkomst',
    '2-1': 'Zet twee stappen met een schip naar keuze',
    '2-2': 'Beweeg een schip met vier ogen of beweeg twee schepen met twee ogen',
    '2-3': 'Beweeg een schip met vijf ogen of beweeg een schip met twee ogen en een ander schip met drie ogen ',
    '2-4': 'Beweeg een schip met zes ogen of beweeg een schip met twee ogen en een ander schip met vier ogen',   
    '2-5': 'Beweeg een schip met zeven ogen of beweeg een schip met twee ogen en een ander schip met vijf ogen',
    '2-6': 'Zet twee stappen met een schip naar keuze en gooi nog een keer met een dobbelsteen voor de kansuitkomst',
    '3-1': 'Zet drie stappen met een schip naar keuze',
    '3-2': 'Beweeg een schip met vijf ogen of beweeg een schip met drie ogen en een ander schip met twee ogen',
    '3-3': 'Beweeg een schip met zes ogen of beweeg een schip met drie ogen en een ander schip met drie ogen',
    '3-4': 'Beweeg een schip met zeven ogen of beweeg een schip met drie ogen en een ander schip met vier ogen',
    '3-5': 'Beweeg een schip met acht ogen of beweeg een schip met drie ogen en een ander schip met vijf ogen',
    '3-6': 'Zet drie stappen met een schip naar keuze en gooi nog een keer met een dobbelsteen voor de kansuitkomst',
    '4-1': 'Zet vier stappen met een schip naar keuze',
    '4-2': 'Beweeg een schip met zes ogen of beweeg een schip met vier ogen en een ander schip met twee ogen',
    '4-3': 'Beweeg een schip met zeven ogen of beweeg een schip met vier ogen en een ander schip met drie ogen',
    '4-4': 'Beweeg een schip met acht ogen of beweeg een schip met vier ogen en een ander schip met vier ogen',
    '4-5': 'Beweeg een schip met negen ogen of beweeg een schip met vier ogen en een ander schip met vijf ogen',
    '4-6': 'Zet vier stappen met een schip naar keuze en gooi nog een keer met een dobbelsteen voor de kansuitkomst',
    '5-1': 'Zet vijf stappen met een schip naar keuze',
    '5-2': 'Beweeg een schip met zeven ogen of beweeg een schip met vijf ogen en een ander schip met twee ogen',
    '5-3': 'Beweeg een schip met acht ogen of beweeg een schip met vijf ogen en een ander schip met drie ogen',
    '5-4': 'Beweeg een schip met negen ogen of beweeg een schip met vijf ogen en een ander schip met vier ogen',
    '5-5': 'Beweeg een schip met tien ogen of beweeg een schip met vijf ogen en een ander schip met vijf ogen',
    '5-6': 'Zet vijf stappen met een schip naar keuze en gooi nog een keer met een dobbelsteen voor de kansuitkomst',
    '6-1': 'Gooi nog een keer met een dobbelsteen voor de kansuitkomst',
    '6-2': 'Beweeg een schip met twee ogen en gooi nog een keer voor de kansuitkomst',
    '6-3': 'Beweeg een schip met drie ogen en gooi nog een keer voor de kansuitkomst',
    '6-4': 'Beweeg een schip met vier ogen en gooi nog een keer voor de kansuitkomst',
    '6-5': 'Zet vijf stappen met een schip naar keuze en gooi nog een keer met een dobbelsteen voor de kansuitkomst',
    '6-6': 'Verdeel naar keuze twaalf stappen over beide schepen',
    }

outcomes_kans = {

'1': "Gooi opnieuw tot je 2, 3, 4, of 5 gooit.",
'2': "Speler mag nog een keer gooien en bij het aantal ogen, dat deze heeft gegooid, 1 optellen of aftrekken. Vervolgens zet u het totale aantal stappen met een schip naar keuze.",
'3': "Speler mag een grondstof ruilen met een schip naar keuze, als speler geen grondstoffen wil of kan ruilen mag deze 3 stappen zetten. Grondstoffen ruilen kan alleen van schip tot schip.",
'4': "Wind mee, speler mag nog een keer gooien, het aantal ogen dat speler gooit wordt verdubbeld.",
'5': "Schipbreuk, sla een beurt over.",
'6': "Gooi overnieuw tot u 2, 3, 4, of 5 gooit."
}

outcome = 'Klik op gooi om te beginnen'

havens = [
    'Rotterdam',
    'Qatar',
    'Shanghai',
    'Singapore',
    'Kaapstad',
    'Dakar',
    'Rio de Janeiro',
    'Caracas',
    'Los Angeles',
    'Quebec',
]

def MouseInSpace(x, y, w, h):
    return ((mouseX > x) and (mouseX < x+w) and (mouseY > y) and (mouseY < y+h))

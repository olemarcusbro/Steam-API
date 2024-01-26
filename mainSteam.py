#Her importerer vi requests modulen denne gjør at vi kan hente data og infromasjon fra Steam API.
import requests

#SteamHex = 76561198799125478
#SteamApiKey = 28AA5C9A3E2D93A76EE4200B590C77CF

VarUrlLevel = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=28AA5C9A3E2D93A76EE4200B590C77CF&steamids=76561198799125478' #Dette er URL til Steam API
VarResponseUsername = requests.get(VarUrlLevel) #Dette er koden som henter data fra Steam API
VarDataUsername = VarResponseUsername.json() #Denne koden henter data fra Steam API og gjør det om til JSON format
VarSteamHex = VarDataUsername.get('response', {}).get('players', [{}])[0].get('steamid') #Denne koden henter SteamHex fra JSON formatet
VarAvatarUser = VarDataUsername.get('response', {}).get('players', [{}])[0].get('avatarfull') #Denne koden henter Avatar/profilbilde fra JSON formatet
VarBrukerNavn = VarDataUsername.get('response', {}).get('players', [{}])[0].get('personaname') #Denne koden henter brukernavn fra JSON formatet
VarRealNameUser = VarDataUsername.get('response', {}).get('players', [{}])[0].get('realname') #Denne koden henter virklignavn fra JSON formatet





VarUrlLevel = 'http://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key=28AA5C9A3E2D93A76EE4200B590C77CF&steamid=76561198799125478' #Dette er URL til Steam API
VarResponseLevel = requests.get(VarUrlLevel) #Dette er koden som henter data fra Steam API
DataLevel = VarResponseLevel.json() #Denne koden henter data fra Steam API og gjør det om til JSON format
SteamLevel = DataLevel.get('response', {}).get('player_level', 0) #Denne koden henter Steam Level fra JSON formatet



VarUrlLevel = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=28AA5C9A3E2D93A76EE4200B590C77CF&steamid=76561198799125478&include_appinfo=1&format=json' #Dette er URL til Steam API
VarResponseGames = requests.get(VarUrlLevel) #Dette er koden som henter data fra Steam API
VarDataGames = VarResponseGames.json() #Denne koden henter data fra Steam API og gjør det om til JSON format
VarSteamGames = VarDataGames.get('response', {}).get('game_count', 0) #Denne koden henter antall spill fra JSON formatet

VarAppId = ['107410', '730', '1938090', '2073850'] #Dette er AppID til spillene som jeg har med for å finne spilletimene mine.
VarGamesTimer = {} 

for game in VarDataGames.get('response', {}).get('games', []): #Dette er en for loop som går igjennom alle spillene som er tilknyttet Steam kontoen min.
    if str(game['appid']) in VarAppId: #Dette er en if statement som sjekker om AppID til spillet er i listen over AppID til spillene som jeg har med.
        VarGamesTimer[game['name']] = round(game['playtime_forever'] / 60, 2 ) #Dette her deler opp spill timene til runde tall

print("Informasjon av Steam brukeren til Ole Marcus \n") #Dette er en print som printer ut informasjon om Steam brukeren til Ole Marcus
print("Steam Hex:",VarSteamHex) #Dette er en print som printer ut SteamHex
print("Brukernavn:",VarBrukerNavn) #Dette er en print som printer ut brukernavn
print("Virklignavn:",VarRealNameUser) #Dette er en print som printer ut virklignavn
print("Profil Bilde:",VarAvatarUser ) #Dette er en print som printer ut profilbilde

print( "\n") #Dette er en print som printer ut en tom linje

print("Kontoens level:") #Dette er en print som printer ut Kontoens level
print("Steam Niva:",SteamLevel) #Dette er en print som printer ut Steam Level
print( "\n") #Dette er en print som printer ut en tom linje
print("Informasjon om Spill\n") #Dette er en print som printer ut informasjon om spill
print("Hvor mange spill som er tilknyttet Steam kontoen:",VarSteamGames, "spill") #Dette er en print som printer ut hvor mange spill som er tilknyttet Steam kontoen

print( "\n") #Dette er en print som printer ut en tom linje

print("Antall spilte timer i forskjellige spill:") #Dette er en print som printer ut Antall spilte timer i forskjellige spill
for game_name, hours in VarGamesTimer.items(): #Dette er en for loop som går igjennom alle spillene som er tilknyttet Steam kontoen min.
    print(f'{game_name}: {hours} timer') #Dette er en print som printer ut spill navn og timer spilt i de forskjellige spillene.

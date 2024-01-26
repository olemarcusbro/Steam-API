
import requests

#SteamHex = 76561198799125478
#SteamApiKey = 28AA5C9A3E2D93A76EE4200B590C77CF

VarUrlLevel = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=28AA5C9A3E2D93A76EE4200B590C77CF&steamids=76561198799125478' 
VarResponseUsername = requests.get(VarUrlLevel) 
VarDataUsername = VarResponseUsername.json() 
VarSteamHex = VarDataUsername.get('response', {}).get('players', [{}])[0].get('steamid') 
VarAvatarUser = VarDataUsername.get('response', {}).get('players', [{}])[0].get('avatarfull') 
VarBrukerNavn = VarDataUsername.get('response', {}).get('players', [{}])[0].get('personaname') 
VarRealNameUser = VarDataUsername.get('response', {}).get('players', [{}])[0].get('realname') 





VarUrlLevel = 'http://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key=28AA5C9A3E2D93A76EE4200B590C77CF&steamid=76561198799125478' 
VarResponseLevel = requests.get(VarUrlLevel) 
DataLevel = VarResponseLevel.json() 
SteamLevel = DataLevel.get('response', {}).get('player_level', 0) 



VarUrlLevel = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=28AA5C9A3E2D93A76EE4200B590C77CF&steamid=76561198799125478&include_appinfo=1&format=json' 
VarResponseGames = requests.get(VarUrlLevel) 
VarDataGames = VarResponseGames.json() 
VarSteamGames = VarDataGames.get('response', {}).get('game_count', 0) 

VarAppId = ['107410', '730', '1938090', '2073850'] 
VarGamesTimer = {} 

for game in VarDataGames.get('response', {}).get('games', []): 
    if str(game['appid']) in VarAppId: 
        VarGamesTimer[game['name']] = round(game['playtime_forever'] / 60, 2 ) 

print("Informasjon av Steam brukeren til Ole Marcus \n") 
print("Steam Hex:",VarSteamHex) 
print("Brukernavn:",VarBrukerNavn) 
print("Virklignavn:",VarRealNameUser) 
print("Profil Bilde:",VarAvatarUser ) 

print( "\n") 

print("Kontoens level:") 
print("Steam Niva:",SteamLevel) 
print( "\n") 
print("Informasjon om Spill\n") 
print("Hvor mange spill som er tilknyttet Steam kontoen:",VarSteamGames, "spill") 

print( "\n") 
print("Antall spilte timer i forskjellige spill:") 
for game_name, hours in VarGamesTimer.items(): 
    print(f'{game_name}: {hours} timer') 

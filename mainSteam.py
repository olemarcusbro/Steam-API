
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

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






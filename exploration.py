#The website changed their API, so I'm not seeing how I can obtain their data at the moment
#Here's an initial exploration to guide further studies:

#%%
import requests

url = "https://offering.begmedia.com/web/offering.access.api/offering.access.api.SportMenuService/GetSportMenu"

payload = "AAAAAAQKAnB0"
headers = {
  'accept': 'application/grpc-web-text',
  'accept-language': 'en-US,en;q=0.9,pt;q=0.8,es;q=0.7',
  'content-type': 'application/grpc-web-text',
  'ngsw-bypass': '1',
  'origin': 'https://www.betclic.pt',
  'priority': 'u=1, i',
  'referer': 'https://www.betclic.pt/',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  'x-bg-regulation': 'PT',
  'x-grpc-web': '1'
}

response = requests.request("POST", url, headers=headers, data=payload,verify=False)

print(response.text)
#%%

#%%
import base64
base64.b64decode(response.text)
#b'\x00\x00\x002\xb2\x1a\xafe\n@\x12\x15Top - Futebol Europeu\x1a\x08football"\x02EU(\x000\x01:\x00B\x11\x03\x04\x05\x06\x07\x08\x13)/2\xd5\x01\xf4\x01\xfd\x1a J\x00\n5\x08\x03\x12\x1bInglaterra - Premier League\x1a\x08football"\x02EN(\x000\x00:\x00J\x00\nb\x08 \x12\x0cLiga Betclic\x1a\x08football"\x02PT(\x000\x00:\x00J<https://dam.begmedia.com/offering/images/competitions/32.png\n/\x08\x05\x12\x15Alemanha - Bundesliga\x1a\x08football"\x02DE(\x000\x00:\x00J\x00\ng\x08\x04\x12\x12Fran\xc3\xa7a - Ligue 1 \x1a\x08football"\x02FR(\x000\x00:\x00J;https://dam.begmedia.com/offering/images/competitions/4.png\n+\x08\x07\x12\x11Espanha - La Liga\x1a\x08football"\x02ES(\x000\x00:\x00J\x00\x12\x9a1\n5\x08\x03\x12\x1bInglaterra - Premier League\x1a\x08football"\x02EN(\x000\x00:\x00J\x00\nb\x08 \x12\x0cLiga Betclic\x1a\x08football"\x02PT(\x000\x00:\x00J<https://dam.begmedia.com/offering/images/competitions/32.png\n/\x08\x05\x12\x15Alemanha - Bundesliga\x1a\x08football"\x02DE(\x000\x00:\x00J\x00\ng\x08\x04\x12\x12Fran\xc3\xa7a - Ligue 1 \x1a\x08football"\x02FR(\x000\x00:\x00J;https://dam.begmedia.com/offering/images/competitions/4.png\n+\x08\x07\x12\x11Espanha - La Liga\x1a\x08football"\x02ES(\x000\x00:\x00J\x00\x12\x08football\x1a\x07Futebol \x01:K\n\x02ZA\x12\x0e\xc3\x81frica do Sul\x1a5\x08\x93$\x12\x1a\xc3\x81frica do Sul - 1.\xc2\xaa Liga\x1a\x08football"\x02ZA(\x000\x00:\x00J\x00:\xa1\x01\n\x02DE\x12\x08Alemanha\x1a-\x08\xaf\r\x12\x12Alemanha - 3. Liga\x1a\x08football"\x02DE(\x000\x00:\x00J\x00\x1a/\x08\x05\x12\x15Alemanha - Bundesliga\x1a\x08football"\x02DE(\x000\x00:\x00J\x00\x1a1\x08\x1d\x12\x17Alemanha - Bundesliga 2\x1a\x08football"\x02DE(\x000\x00:\x00J\x00:M\n\x02SA\x12\x0fAr\xc3\xa1bia Saudita\x1a6\x08\xcc$\x12\x1bAr\xc3\xa1bia Saudita - 1.\xc2\xaa Liga\x1a\x08football"\x02SA(\x000\x00:\x00J\x00:\xda\x01\n\x02AR\x12\tArgentina\x1a.\x08\xe6\x01\x12\x13Argentina - Primera\x1a\x08football"\x02AR(\x000\x00:\x00J\x00\x1a2\x08\xc5\xaa\x01\x12\x16Argentina - Primera F.\x1a\x08football"\x02AR(\x000\x00:\x00J\x00\x1a7\x08\xfb*\x12\x1cArgentina - Primera Nacional\x1a\x08football"\x02AR(\x000\x00:\x00J\x00\x1a,\x08\xcc{\x12\x11Argentina - Ta\xc3\xa7a\x1a\x08football"\x02AR(\x000\x00:\x00J\x00:x\n\x02AU\x12\nAustr\xc3\xa1lia\x1a0\x08\xd2\x0e\x12\x15Austr\xc3\xa1lia - A-League\x1a\x08football"\x02AU(\x000\x00:\x00J\x00\x1a4\x08\xd9\xa1\x01\x12\x18Austr\xc3\xa1lia - A-League F.\x1a\x08football"\x02AU(\x000\x00:\x00J\x00:u\n\x02AT\x12\x08\xc3\x81ustria\x1a3\x08\xd3\x0e\x12\x18\xc3\x81ustria - 1.\xc2\xaa Divis\xc3\xa3o\x1a\x08football"\x02AT(\x000\x00:\x00J\x00\x1a0\x08#\x12\x16\xc3\x81ustria - Bundesliga \x1a\x08football"\x02AT(\x000\x00:\x00J\x00:\x9f\x01\n\x02BE\x12\x08B\xc3\xa9lgica\x1a0\x08\x1a\x12\x16B\xc3\xa9lgica - Divis\xc3\xa3o 1A\x1a\x08football"\x02BE(\x000\x00:\x00J\x00\x1a1\x08\xf4\x03\x12\x16B\xc3\xa9lgica - Divis\xc3\xa3o 1B\x1a\x08football"\x02BE(\x000\x00:\x00J\x00\x1a*\x086\x12\x10B\xc3\xa9lgica - Ta\xc3\xa7a\x1a\x08football"\x02BE(\x000\x00:\x00J\x00::\n\x02BR\x12\x06Brasil\x1a,\x08\xbb\x01\x12\x11Brasil - S\xc3\xa9rie A\x1a\x08football"\x02BR(\x000\x00:\x00J\x00:A\n\x02BG\x12\tBulg\xc3\xa1ria\x1a0\x08\xa4\x04\x12\x15Bulg\xc3\xa1ria - 1.\xc2\xaa Liga\x1a\x08football"\x02BG(\x000\x00:\x00J\x00:9\n\x02CL\x12\x05Chile\x1a,\x08\x8f~\x12\x11Chile - Primera B\x1a\x08football"\x02CL(\x000\x00:\x00J\x00:?\n\x02CY\x12\x06Chipre\x1a1\x08\xb7\x04\x12\x16Chipre - 1.\xc2\xaa Divis\xc3\xa3o\x1a\x08football"\x02CY(\x000\x00:\x00J\x00:n\n\x02CO\x12\tCol\xc3\xb4mbia\x1a+\x08\xd6\x14\x12\x10Col\xc3\xb4mbia - Copa\x1a\x08football"\x02CO(\x000\x00:\x00J\x00\x1a0\x08\xfc*\x12\x15Col\xc3\xb4mbia - Primera A\x1a\x08football"\x02CO(\x000\x00:\x00J\x00:H\n\x02KR\x12\rCoreia do Sul\x1a3\x08\xe8\x19\x12\x18Coreia do Sul - K-League\x1a\x08football"\x02KR(\x000\x00:\x00J\x00:C\n\x02HR\x12\x08Cro\xc3\xa1cia\x1a3\x08\x93\x04\x12\x18Cro\xc3\xa1cia - 1.\xc2\xaa Divis\xc3\xa3o\x1a\x08football"\x02HR(\x000\x00:\x00J\x00:=\n\x02DK\x12\tDinamarca\x1a,\x08\xdb\x03\x12\x11Dinamarca - Ta\xc3\xa7a\x1a\x08football"\x02DK(\x000\x00:\x00J\x00:=\n\x02EC\x12\x07Equador\x1a.\x08\xa5\x14\x12\x13Equador - Primera A\x1a\x08football"\x02EC(\x000\x00:\x00J\x00:\xa9\x01\n\x02ND\x12\x08Esc\xc3\xb3cia\x1a2\x08\xa7\x04\x12\x17Esc\xc3\xb3cia - Championship\x1a\x08football"\x02ND(\x000\x00:\x00J\x00\x1a0\x08!\x12\x16Esc\xc3\xb3cia - Premiership\x1a\x08football"\x02ND(\x000\x00:\x00J\x00\x1a3\x088\x12\x19Esc\xc3\xb3cia - Ta\xc3\xa7a da Liga \x1a\x08football"\x02ND(\x000\x00:\x00J\x00:E\n\x02SK\x12\x0bEslov\xc3\xa1quia\x1a2\x08\xaf\x04\x12\x17Eslov\xc3\xa1quia - 1.\xc2\xaa Liga\x1a\x08football"\x02SK(\x000\x00:\x00J\x00:C\n\x02SI\x12\nEslov\xc3\xa9nia\x1a1\x08\xa5\x04\x12\x16Eslov\xc3\xa9nia - 1.\xc2\xaa Liga\x1a\x08football"\x02SI(\x000\x00:\x00J\x00:\xfe\x01\n\x02ES\x12\x07Espanha\x1a+\x08\x07\x12\x11Espanha - La Liga\x1a\x08football"\x02ES(\x000\x00:\x00J\x00\x1a2\x08\xa2\x81\x02\x12\x16Espanha - Primera RFEF\x1a\x08football"\x02ES(\x000\x00:\x00J\x00\x1a+\x08\x1f\x12\x11Espanha - Segunda\x1a\x08football"\x02ES(\x000\x00:\x00J\x00\x1a/\x08\xd5\x01\x12\x14Espanha - Superta\xc3\xa7a\x1a\x08football"\x02ES(\x000\x00:\x00J\x00\x1a0\x08/\x12\x16Espanha - Ta\xc3\xa7a do Rei\x1a\x08football"\x02ES(\x000\x00:\x00J\x00:F\n\x02US\x12\x1aEstados Unidos da Am\xc3\xa9rica\x1a$\x08\xf8\x03\x12\tEUA - MLS\x1a\x08football"\x02US(\x000\x00:\x00J\x00:b\n\x02EU\x12\x06Europa\x1a,\x08\x08\x12\x12Liga dos Campe\xc3\xb5es\x1a\x08football"\x02EU(\x000\x00:\x00J\x00\x1a&\x08\xfd\x1a\x12\x0bLiga Europa\x1a\x08football"\x02EU(\x000\x00:\x00J\x00:\x8e\x02\n\x02FR\x12\x07Fran\xc3\xa7a\x1ag\x08\x04\x12\x12Fran\xc3\xa7a - Ligue 1 \x1a\x08football"\x02FR(\x000\x00:\x00J;https://dam.begmedia.com/offering/images/competitions/4.png\x1ah\x08\x13\x12\x12Fran\xc3\xa7a - Ligue 2 \x1a\x08football"\x02FR(\x000\x00:\x00J<https://dam.begmedia.com/offering/images/competitions/19.png\x1a,\x085\x12\x12Fran\xc3\xa7a - National\x1a\x08football"\x02FR(\x000\x00:\x00J\x00:\x9b\x01\n\x02GR\x12\x07Gr\xc3\xa9cia\x1a-\x08&\x12\x13Gr\xc3\xa9cia - Superliga\x1a\x08football"\x02GR(\x000\x00:\x00J\x00\x1a1\x08\xc9\xe2\x01\x12\x15Gr\xc3\xa9cia - Superliga 2\x1a\x08football"\x02GR(\x000\x00:\x00J\x00\x1a*\x08\x85\x01\x12\x0fGr\xc3\xa9cia - Ta\xc3\xa7a\x1a\x08football"\x02GR(\x000\x00:\x00J\x00:E\n\x02GT\x12\tGuatemala\x1a4\x08\x9b~\x12\x19Guatemala - Liga Nacional\x1a\x08football"\x02GT(\x000\x00:\x00J\x00:8\n\x02HU\x12\x07Hungria\x1a)\x08\xa9\x04\x12\x0eHungria - NB 1\x1a\x08football"\x02HU(\x000\x00:\x00J\x00:=\n\x02IN\x12\x06\xc3\x8dndia\x1a/\x08\xd7\x9a\x01\x12\x13\xc3\x8dndia - Super Liga\x1a\x08football"\x02IN(\x000\x00:\x00J\x00:C\n\x02ID\x12\nIndon\xc3\xa9sia\x1a1\x08\xb8x\x12\x16Indon\xc3\xa9sia - 1.\xc2\xaa Liga\x1a\x08football"\x02ID(\x000\x00:\x00J\x00:\x97\x02\n\x02EN\x12\nInglaterra\x1a3\x08\x1c\x12\x19Inglaterra - Championship\x1a\x08football"\x02EN(\x000\x00:\x00J\x00\x1a0\x08\xe5\x01\x12\x15Inglaterra - League 1\x1a\x08football"\x02EN(\x000\x00:\x00J\x00\x1a5\x08\x03\x12\x1bInglaterra - Premier League\x1a\x08football"\x02EN(\x000\x00:\x00J\x00\x1a5\x08\xc2\x86\x01\x12\x19Inglaterra - Superliga F.\x1a\x08football"\x02EN(\x000\x00:\x00J\x00\x1a0\x08)\x12\x16Inglaterra - Ta\xc3\xa7a EFL\x1a\x08football"\x02EN(\x000\x00:\x00J\x00:w\n\x02ZZ\x12\rInternacional\x1a1\x08\x87\x1b\x12\x16AFC Champions League 2\x1a\x08football"\x02ZZ(\x000\x00:\x00J\x00\x1a/\x08\x81\n\x12\x14CAF - Liga Campe\xc3\xb5es\x1a\x08football"\x02ZZ(\x000\x00:\x00J\x00:Q\n\x02NT\x12\x10Irlanda do Norte\x1a9\x08\xd5\x0e\x12\x1eIrlanda do Norte - Premiership\x1a\x08football"\x02NT(\x000\x00:\x00J\x00:l\n\x02IL\x12\x06Israel\x1a-\x08\xd4\x0e\x12\x12Israel - 1.\xc2\xaa Liga\x1a\x08football"\x02IL(\x000\x00:\x00J\x00\x1a/\x08\xe0*\x12\x14Israel - Liga Leumit\x1a\x08football"\x02IL(\x000\x00:\x00J\x00:\xec\x02\n\x02IT\x12\x07It\xc3\xa1lia\x1a+\x08\x06\x12\x11It\xc3\xa1lia - Serie A\x1a\x08football"\x02IT(\x000\x00:\x00J\x00\x1a+\x08\x1e\x12\x11It\xc3\xa1lia - Serie B\x1a\x08football"\x02IT(\x000\x00:\x00J\x00\x1a6\x08\xfb\x99\x01\x12\x1aIt\xc3\xa1lia - Serie C Girone A\x1a\x08football"\x02IT(\x000\x00:\x00J\x00\x1a6\x08\xfd\x99\x01\x12\x1aIt\xc3\xa1lia - Serie C Girone B\x1a\x08football"\x02IT(\x000\x00:\x00J\x00\x1a6\x08\xfc\x99\x01\x12\x1aIt\xc3\xa1lia - Serie C Girone C\x1a\x08football"\x02IT(\x000\x00:\x00J\x00\x1a0\x08\xf4\x01\x12\x15It\xc3\xa1lia - Superta\xc3\xa7a \x1a\x08football"\x02IT(\x000\x00:\x00J\x00\x1a)\x082\x12\x0fIt\xc3\xa1lia - Ta\xc3\xa7a\x1a\x08football"\x02IT(\x000\x00:\x00J\x00:;\n\x02JP\x12\x06Jap\xc3\xa3o\x1a-\x08\xf7\x03\x12\x12Jap\xc3\xa3o - J-League \x1a\x08football"\x02JP(\x000\x00:\x00J\x00:B\n\x02JO\x12\tJord\xc3\xa2nia\x1a1\x08\xf2*\x12\x16Jord\xc3\xa2nia - Pro League\x1a\x08football"\x02JO(\x000\x00:\x00J\x00:;\n\x02MX\x12\x07M\xc3\xa9xico\x1a,\x08\xb0\x03\x12\x11M\xc3\xa9xico - Liga MX\x1a\x08football"\x02MX(\x000\x00:\x00J\x00:l\n\x02NO\x12\x07Noruega\x1a0\x08\x9c\x01\x12\x15Noruega - Eliteserien\x1a\x08football"\x02NO(\x000\x00:\x00J\x00\x1a+\x08\xb4\x04\x12\x10Noruega - Ta\xc3\xa7a \x1a\x08football"\x02NO(\x000\x00:\x00J\x00:4\n\x02OM\x12\x04Om\xc3\xa3\x1a(\x08\xeb\x85\x01\x12\x0cOm\xc3\xa3 - Ta\xc3\xa7a\x1a\x08football"\x02OM(\x000\x00:\x00J\x00:P\n\x02WA\x12\x0ePa\xc3\xads de Gales\x1a:\x08\xd5\x14\x12\x1fPa\xc3\xads de Gales - Premier League\x1a\x08football"\x02WA(\x000\x00:\x00J\x00:\x7f\n\x02NL\x12\x0ePa\xc3\xadses Baixos\x1a2\x08\x9b\x04\x12\x17Pa\xc3\xadses Baixos - Eerste\x1a\x08football"\x02NL(\x000\x00:\x00J\x00\x1a5\x08\x15\x12\x1bPa\xc3\xadses Baixos - Eredivisie\x1a\x08football"\x02NL(\x000\x00:\x00J\x00:<\n\x02PY\x12\x08Paraguai\x1a,\x08\xe1\xb6\x01\x12\x10Paraguai - Ta\xc3\xa7a\x1a\x08football"\x02PY(\x000\x00:\x00J\x00:\xdd\x01\n\x02PL\x12\x08Pol\xc3\xb3nia\x1am\x08\xd5\r\x12\x14Pol\xc3\xb3nia - 1.\xc2\xaa Liga\x1a\x08football"\x02PL(\x000\x00:\x00J>https://dam.begmedia.com/offering/images/competitions/1749.png\x1a1\x08\xdd\x01\x12\x16Pol\xc3\xb3nia - Ekstraklasa\x1a\x08football"\x02PL(\x000\x00:\x00J\x00\x1a+\x08\xfa\x08\x12\x10Pol\xc3\xb3nia - Ta\xc3\xa7a\x1a\x08football"\x02PL(\x000\x00:\x00J\x00:\xd5\x01\n\x02PT\x12\x08Portugal\x1ab\x08 \x12\x0cLiga Betclic\x1a\x08football"\x02PT(\x000\x00:\x00J<https://dam.begmedia.com/offering/images/competitions/32.png\x1a-\x08\xf9\xa7\x01\x12\x11Portugal - Liga 3\x1a\x08football"\x02PT(\x000\x00:\x00J\x00\x1a2\x08\xab\x07\x12\x17Portugal - Segunda Liga\x1a\x08football"\x02PT(\x000\x00:\x00J\x00:<\n\x02QA\x12\x05Qatar\x1a/\x08\x92$\x12\x14Catar - Stars League\x1a\x08football"\x02QA(\x000\x00:\x00J\x00:I\n\x02CZ\x12\x10Rep\xc3\xbablica Checa\x1a1\x08\xdc\x01\x12\x16Rep. Checa - 1.\xc2\xaa Liga\x1a\x08football"\x02CZ(\x000\x00:\x00J\x00:\x9a\x01\n\x02RO\x12\x08Rom\xc3\xa9nia\x1a/\x08\x95:\x12\x14Rom\xc3\xa9nia - 2.\xc2\xaa Liga\x1a\x08football"\x02RO(\x000\x00:\x00J\x00\x1a,\x08\xa8\x04\x12\x11Rom\xc3\xa9nia - Liga 1\x1a\x08football"\x02RO(\x000\x00:\x00J\x00\x1a+\x08\xd6\x11\x12\x10Rom\xc3\xa9nia - Ta\xc3\xa7a\x1a\x08football"\x02RO(\x000\x00:\x00J\x00:=\n\x02RS\x12\x07S\xc3\xa9rvia\x1a.\x08\xce,\x12\x13S\xc3\xa9rvia - Superliga\x1a\x08football"\x02RS(\x000\x00:\x00J\x00:\x9d\x01\n\x02CH\x12\x07Su\xc3\xad\xc3\xa7a\x1a3\x08\x9a\r\x12\x18Su\xc3\xad\xc3\xa7a - Liga Challenge\x1a\x08football"\x02CH(\x000\x00:\x00J\x00\x1a-\x08\x1b\x12\x13Su\xc3\xad\xc3\xa7a - Superliga\x1a\x08football"\x02CH(\x000\x00:\x00J\x00\x1a*\x08\xce\x03\x12\x0fSu\xc3\xad\xc3\xa7a - Ta\xc3\xa7a\x1a\x08football"\x02CH(\x000\x00:\x00J\x00:H\n\x02TH\x12\nTail\xc3\xa2ndia\x1a6\x08\xd3~\x12\x1bTail\xc3\xa2ndia - Premier League\x1a\x08football"\x02TH(\x000\x00:\x00J\x00:G\n\x02TZ\x12\tTanz\xc3\xa2nia\x1a6\x08\x89\xb3\x01\x12\x1aTanz\xc3\xa2nia - Premier League\x1a\x08football"\x02TZ(\x000\x00:\x00J\x00:\x98\x01\n\x02TR\x12\x07Turquia\x1a.\x08\x91$\x12\x13Turquia - 1.\xc2\xaa Liga\x1a\x08football"\x02TR(\x000\x00:\x00J\x00\x1a-\x08%\x12\x13Turquia - Superliga\x1a\x08football"\x02TR(\x000\x00:\x00J\x00\x1a*\x08|\x12\x10Turquia - Ta\xc3\xa7a \x1a\x08football"\x02TR(\x000\x00:\x00J\x00:?\n\x02UA\x12\x08Ucr\xc3\xa2nia\x1a/\x08\x92\x04\x12\x14Ucr\xc3\xa2nia - 1.\xc2\xaa Liga\x1a\x08football"\x02UA(\x000\x00:\x00J\x00\x12\x94\x0e\n%\x08\r\x12\tEUA - NBA\x1a\nbasketball"\x02US(\x000\x00:\x00J\x00\n0\x08\x81{\x12\x13Coreia do Sul - KBL\x1a\nbasketball"\x02KR(\x000\x00:\x00J\x00\n$\x08\x0e\x12\x08Euroliga\x1a\nbasketball"\x02EU(\x000\x00:\x00J\x00\n-\x08\xeaz\x12\x10Austr\xc3\xa1lia - NBL\x1a\nbasketball"\x02AU(\x000\x00:\x00J\x00\nh\x08\xc3t\x12\x0cLiga Betclic\x1a\nbasketball"\x02PT(\x000\x00:\x00J?https://dam.begmedia.com/offering/images/competitions/14915.png\x12\nbasketball\x1a\x0bBasquetebol \x01:=\n\x02AR\x12\tArgentina\x1a,\x08\xf4z\x12\x0fArgentina - LNB\x1a\nbasketball"\x02AR(\x000\x00:\x00J\x00:p\n\x02AU\x12\nAustr\xc3\xa1lia\x1a-\x08\xeaz\x12\x10Austr\xc3\xa1lia - NBL\x1a\nbasketball"\x02AU(\x000\x00:\x00J\x00\x1a/\x08\xd6\x93\x01\x12\x11Austr\xc3\xa1lia - WNBL\x1a\nbasketball"\x02AU(\x000\x00:\x00J\x00:@\n\x02AT\x12\x08\xc3\x81ustria\x1a0\x08\xbf \x12\x13\xc3\x81ustria -Superliga\x1a\nbasketball"\x02AT(\x000\x00:\x00J\x00:7\n\x02BR\x12\x06Brasil\x1a)\x08\xf8z\x12\x0cBrasil - NBB\x1a\nbasketball"\x02BR(\x000\x00:\x00J\x00:5\n\x02CN\x12\x05China\x1a(\x08\xd2|\x12\x0bChina - CBA\x1a\nbasketball"\x02CN(\x000\x00:\x00J\x00:E\n\x02KR\x12\rCoreia do Sul\x1a0\x08\x81{\x12\x13Coreia do Sul - KBL\x1a\nbasketball"\x02KR(\x000\x00:\x00J\x00::\n\x02HR\x12\x08Cro\xc3\xa1cia\x1a*\x08\xf1z\x12\rCro\xc3\xa1cia - A1\x1a\nbasketball"\x02HR(\x000\x00:\x00J\x00:F\n\x02DK\x12\tDinamarca\x1a5\x08\xf2z\x12\x18Dinamarca - Basketligaen\x1a\nbasketball"\x02DK(\x000\x00:\x00J\x00:>\n\x02ES\x12\x07Espanha\x1a/\x08\xe2\x9c\x01\x12\x11Espanha - Liga F.\x1a\nbasketball"\x02ES(\x000\x00:\x00J\x00:p\n\x02US\x12\x1aEstados Unidos da Am\xc3\xa9rica\x1a%\x08\r\x12\tEUA - NBA\x1a\nbasketball"\x02US(\x000\x00:\x00J\x00\x1a\'\x08\xd1\x07\x12\nEUA - NCAA\x1a\nbasketball"\x02US(\x000\x00:\x00J\x00:2\n\x02EU\x12\x06Europa\x1a$\x08\x0e\x12\x08Euroliga\x1a\nbasketball"\x02EU(\x000\x00:\x00J\x00:F\n\x02FI\x12\nFinl\xc3\xa2ndia\x1a4\x08\xf3z\x12\x17Finl\xc3\xa2ndia - Korisliiga\x1a\nbasketball"\x02FI(\x000\x00:\x00J\x00:@\n\x02GR\x12\x07Gr\xc3\xa9cia\x1a1\x08\xf6\x03\x12\x14Gr\xc3\xa9cia - A1 Ethniki\x1a\nbasketball"\x02GR(\x000\x00:\x00J\x00:A\n\x02ZZ\x12\rInternacional\x1a,\x08\xb3\x10\x12\x0fLiga Adri\xc3\xa1tica\x1a\nbasketball"\x02ZZ(\x000\x00:\x00J\x00:>\n\x02IL\x12\x06Israel\x1a0\x08\x9d\xa1\x01\x12\x12Israel - Super Lig\x1a\nbasketball"\x02IL(\x000\x00:\x00J\x00::\n\x02MX\x12\x07M\xc3\xa9xico\x1a+\x08\xfbz\x12\x0eM\xc3\xa9xico - LNBP\x1a\nbasketball"\x02MX(\x000\x00:\x00J\x00:C\n\x02PL\x12\x08Pol\xc3\xb3nia\x1a3\x08\x9c\x12\x12\x16Pol\xc3\xb3nia - Ekstraklasa\x1a\nbasketball"\x02PL(\x000\x00:\x00J\x00:x\n\x02PT\x12\x08Portugal\x1ah\x08\xc3t\x12\x0cLiga Betclic\x1a\nbasketball"\x02PT(\x000\x00:\x00J?https://dam.begmedia.com/offering/images/competitions/14915.png:E\n\x02CZ\x12\x10Rep\xc3\xbablica Checa\x1a-\x08\xd3 \x12\x10Rep. Checa - NBL\x1a\nbasketball"\x02CZ(\x000\x00:\x00J\x00:A\n\x02SE\x12\x07Su\xc3\xa9cia\x1a2\x08\xfez\x12\x15Su\xc3\xa9cia - Basketligan\x1a\nbasketball"\x02SE(\x000\x00:\x00J\x00:9\n\x02TR\x12\x07Turquia\x1a*\x08\xd7\x13\x12\rTurquia - BSL\x1a\nbasketball"\x02TR(\x000\x00:\x00J\x00\x12\xaf\t\n/\x08\xa0\x04\x12\x12Finl\xc3\xa2ndia - Liiga\x1a\nice_hockey"\x02FI(\x000\x00:\x00J\x00\n%\x08S\x12\tEUA - NHL\x1a\nice_hockey"\x02US(\x000\x00:\x00J\x00\n*\x08\x8c\x04\x12\rSu\xc3\xa9cia - SHL\x1a\nice_hockey"\x02SE(\x000\x00:\x00J\x00\n&\x08\xd0\x10\x12\tEUA - AHL\x1a\nice_hockey"\x02US(\x000\x00:\x00J\x00\n3\x08\xe3\x0f\x12\x16Rep. Checa - Extraliga\x1a\nice_hockey"\x02CZ(\x000\x00:\x00J\x00\x12\nice_hockey\x1a\x0fH\xc3\xb3quei no Gelo \x01:;\n\x02DE\x12\x08Alemanha\x1a+\x08\x98\x03\x12\x0eAlemanha - DEL\x1a\nice_hockey"\x02DE(\x000\x00:\x00J\x00:9\n\x02AT\x12\x08\xc3\x81ustria\x1a)\x08\x82\x10\x12\x0c\xc3\x81ustria ICE\x1a\nice_hockey"\x02AT(\x000\x00:\x00J\x00:@\n\x02DK\x12\tDinamarca\x1a/\x08\xdc\x13\x12\x12Dinamarca - Ligaen\x1a\nice_hockey"\x02DK(\x000\x00:\x00J\x00:G\n\x02SK\x12\x0bEslov\xc3\xa1quia\x1a4\x08\xcb\x0f\x12\x17Eslov\xc3\xa1quia - Extraliga\x1a\nice_hockey"\x02SK(\x000\x00:\x00J\x00:o\n\x02US\x12\x1aEstados Unidos da Am\xc3\xa9rica\x1a&\x08\xd0\x10\x12\tEUA - AHL\x1a\nice_hockey"\x02US(\x000\x00:\x00J\x00\x1a%\x08S\x12\tEUA - NHL\x1a\nice_hockey"\x02US(\x000\x00:\x00J\x00:A\n\x02FI\x12\nFinl\xc3\xa2ndia\x1a/\x08\xa0\x04\x12\x12Finl\xc3\xa2ndia - Liiga\x1a\nice_hockey"\x02FI(\x000\x00:\x00J\x00:B\n\x02FR\x12\x07Fran\xc3\xa7a\x1a3\x08\x89\x02\x12\x16Fran\xc3\xa7a - Ligue Magnus\x1a\nice_hockey"\x02FR(\x000\x00:\x00J\x00:E\n\x02ZZ\x12\rInternacional\x1a0\x08\x9d\xa5\x01\x12\x12Alps Hockey League\x1a\nice_hockey"\x02ZZ(\x000\x00:\x00J\x00:<\n\x02NO\x12\x07Noruega\x1a-\x08\xdd\x13\x12\x10Noruega - Ligaen\x1a\nice_hockey"\x02NO(\x000\x00:\x00J\x00:C\n\x02PL\x12\x08Pol\xc3\xb3nia\x1a3\x08\xca\x0f\x12\x16Pol\xc3\xb3nia - Ekstraklasa\x1a\nice_hockey"\x02PL(\x000\x00:\x00J\x00:K\n\x02CZ\x12\x10Rep\xc3\xbablica Checa\x1a3\x08\xe3\x0f\x12\x16Rep. Checa - Extraliga\x1a\nice_hockey"\x02CZ(\x000\x00:\x00J\x00:`\n\x02SE\x12\x07Su\xc3\xa9cia\x1a%\x08\xdc\xd1\x01\x12\x07SDHL F.\x1a\nice_hockey"\x02SE(\x000\x00:\x00J\x00\x1a*\x08\x8c\x04\x12\rSu\xc3\xa9cia - SHL\x1a\nice_hockey"\x02SE(\x000\x00:\x00J\x00:9\n\x02CH\x12\x07Su\xc3\xad\xc3\xa7a\x1a*\x08\xc1\x0f\x12\rSu\xc3\xad\xc3\xa7a - NLA\x1a\nice_hockey"\x02CH(\x000\x00:\x00J\x00\x12\xe7\x07\n,\x08n\x12\x12Liga dos Campe\xc3\xb5es\x1a\x08handball"\x02EU(\x000\x00:\x00J\x00\n-\x08\xd0\x02\x12\x12Camp. da Europa F.\x1a\x08handball"\x02EU(\x000\x00:\x00J\x00\n+\x08\xfb\x01\x12\x10Fran\xc3\xa7a - Liga 1\x1a\x08handball"\x02FR(\x000\x00:\x00J\x00\n+\x08\xfd\x01\x12\x10Espanha - Asobal\x1a\x08handball"\x02ES(\x000\x00:\x00J\x00\n0\x08\xfc\x01\x12\x15Alemanha - Bundesliga\x1a\x08handball"\x02DE(\x000\x00:\x00J\x00\x12\x08handball\x1a\x07Andebol \x01:@\n\x02DE\x12\x08Alemanha\x1a0\x08\xfc\x01\x12\x15Alemanha - Bundesliga\x1a\x08handball"\x02DE(\x000\x00:\x00J\x00:9\n\x02AT\x12\x08\xc3\x81ustria\x1a)\x08\xb7x\x12\x0e\xc3\x81ustria - HLA\x1a\x08handball"\x02AT(\x000\x00:\x00J\x00:D\n\x02HR\x12\x08Cro\xc3\xa1cia\x1a4\x08\xc9\xb2\x01\x12\x18Cro\xc3\xa1cia - Premijer Liga\x1a\x08handball"\x02HR(\x000\x00:\x00J\x00:>\n\x02DK\x12\tDinamarca\x1a-\x08\xfa\x0e\x12\x12Dinamarca - Ligaen\x1a\x08handball"\x02DK(\x000\x00:\x00J\x00::\n\x02ES\x12\x07Espanha\x1a+\x08\xfd\x01\x12\x10Espanha - Asobal\x1a\x08handball"\x02ES(\x000\x00:\x00J\x00:i\n\x02EU\x12\x06Europa\x1a-\x08\xd0\x02\x12\x12Camp. da Europa F.\x1a\x08handball"\x02EU(\x000\x00:\x00J\x00\x1a,\x08n\x12\x12Liga dos Campe\xc3\xb5es\x1a\x08handball"\x02EU(\x000\x00:\x00J\x00::\n\x02FR\x12\x07Fran\xc3\xa7a\x1a+\x08\xfb\x01\x12\x10Fran\xc3\xa7a - Liga 1\x1a\x08handball"\x02FR(\x000\x00:\x00J\x00:?\n\x02NO\x12\x07Noruega\x1a0\x08\x86\x1d\x12\x15Noruega - Eliteserien\x1a\x08handball"\x02NO(\x000\x00:\x00J\x00:?\n\x02PL\x12\x08Pol\xc3\xb3nia\x1a/\x08\xcbz\x12\x14Pol\xc3\xb3nia - Superliga\x1a\x08handball"\x02PL(\x000\x00:\x00J\x00:?\n\x02PT\x12\x08Portugal\x1a/\x08\x91\x1a\x12\x14Portugal 1A Divis\xc3\xa3o\x1a\x08handball"\x02PT(\x000\x00:\x00J\x00:>\n\x02SE\x12\x07Su\xc3\xa9cia\x1a/\x08\xb2\x04\x12\x14Su\xc3\xa9cia - Elitserien\x1a\x08handball"\x02SE(\x000\x00:\x00J\x00\x12\x81\x01\x12\x0cmartial_arts\x1a\x0eArtes Marciais*a\x08\xca|\x12\x03UFC\x1a\x0cmartial_arts"\x02ZZ(\x000\x00:\x00J?https://dam.begmedia.com/offering/images/competitions/15946.png\x12}\x12\tbadminton\x1a\tBadminton*-\x08\xf6\x8a\x02\x12\x10Guwahati Masters\x1a\tbadminton"\x02IN(\x000\x00:\x00J\x00*6\x08\xf9\x8a\x02\x12\x19Guwahati Masters Pares F.\x1a\tbadminton"\x02IN(\x000\x00:\x00J\x00\x124\x12\x08baseball\x1a\x07Basebol*\x1f\x08\x9b\xba\x01\x12\x03ABL\x1a\x08baseball"\x02AU(\x000\x00:\x00J\x00\x12;\x12\x05darts\x1a\x06Dardos**\x08\xb8 \x12\x12Camp. do Mundo PDC\x1a\x05darts"\x02EN(\x000\x00:\x00J\x00\x12\x84\x01\x12\x11american_football\x1a\x11Futebol Americano*.\x08\x95\x06\x12\nEUA - NCAA\x1a\x11american_football"\x02US(\x000\x00:\x00J\x00*,\x08T\x12\tEUA - NFL\x1a\x11american_football"\x02US(\x000\x00:\x00J\x00\x12m\x12\x06futsal\x1a\x06Futsal*-\x08\xad\x0f\x12\x14Espanha - Div. Honra\x1a\x06futsal"\x02ES(\x000\x00:\x00J\x00*,\x08\xdd\xa7\x01\x12\x12Polish Ekstraklasa\x1a\x06futsal"\x02PL(\x000\x00:\x00J\x00\x12\xd1\x01\x12\x0brugby_union\x1a\x08Rugby XV \x01::\n\x02EU\x12\x06Europa\x1a,\x08\x9d\x98\x02\x12\rChampions Cup\x1a\x0brugby_union"\x02EU(\x000\x00:\x00J\x00:z\n\x02FR\x12\x07Fran\xc3\xa7a\x1ak\x08\xf0\x05\x12\x10Fran\xc3\xa7a - Pro D2\x1a\x0brugby_union"\x02FR(\x000\x00:\x00J=https://dam.begmedia.com/offering/images/competitions/752.png\x12E\x12\x07snooker\x1a\x07Snooker*1\x08\x9dr\x12\x17World Snooker Shoot-Out\x1a\x07snooker"\x02EN(\x000\x00:\x00J\x00\x12\x84\x02\x12\x06tennis\x1a\x06T\xc3\xa9nis \x022\xef\x01\n\x0bChallengers\x12/\x08\x94\xea\x01\x12\x15Angers WTA Challenger\x1a\x06tennis"\x02FR(\x000\x00:\x00J\x00\x127\x08\x95\xea\x01\x12\x1dAngers WTA Challenger - Pares\x1a\x06tennis"\x02FR(\x000\x00:\x00J\x00\x126\x08\x96\x8a\x02\x12\x1cFlorianopolis WTA Challenger\x1a\x06tennis"\x02BR(\x000\x00:\x00J\x00\x12>\x08\x97\x8a\x02\x12$Florianopolis WTA Challenger - Pares\x1a\x06tennis"\x02BR(\x000\x00:\x00J\x00\x12\x9e\x07\n*\x08\x8f\xa7\x01\x12\x0cChina - Liga\x1a\nvolleyball"\x02CN(\x000\x00:\x00J\x00\n4\x08\xf3(\x12\x17Coreia do Sul - Liga F.\x1a\nvolleyball"\x02KR(\x000\x00:\x00J\x00\n1\x08\xbf$\x12\x14Coreia do Sul - Liga\x1a\nvolleyball"\x02KR(\x000\x00:\x00J\x00\n,\x08\xe4p\x12\x0fTa\xc3\xa7a Challenge\x1a\nvolleyball"\x02EU(\x000\x00:\x00J\x00\n7\x08\xb1\xab\x01\x12\x19Rep. Checa - Extraliga F.\x1a\nvolleyball"\x02CZ(\x000\x00:\x00J\x00\x12\nvolleyball\x1a\x08Voleibol \x01:7\n\x02CN\x12\x05China\x1a*\x08\x8f\xa7\x01\x12\x0cChina - Liga\x1a\nvolleyball"\x02CN(\x000\x00:\x00J\x00:|\n\x02KR\x12\rCoreia do Sul\x1a1\x08\xbf$\x12\x14Coreia do Sul - Liga\x1a\nvolleyball"\x02KR(\x000\x00:\x00J\x00\x1a4\x08\xf3(\x12\x17Coreia do Sul - Liga F.\x1a\nvolleyball"\x02KR(\x000\x00:\x00J\x00:\xba\x01\n\x02EU\x12\x06Europa\x1a/\x08\x8f\x02\x12\x12Liga dos Campe\xc3\xb5es\x1a\nvolleyball"\x02EU(\x000\x00:\x00J\x00\x1a%\x08\xfd|\x12\x08MEVZA F.\x1a\nvolleyball"\x02EU(\x000\x00:\x00J\x00\x1a&\x08\xf9\x1f\x12\tTa\xc3\xa7a CEV\x1a\nvolleyball"\x02EU(\x000\x00:\x00J\x00\x1a,\x08\xe4p\x12\x0fTa\xc3\xa7a Challenge\x1a\nvolleyball"\x02EU(\x000\x00:\x00J\x00:F\n\x02PL\x12\x08Pol\xc3\xb3nia\x1a6\x08\x8e\x1d\x12\x19Pol\xc3\xb3nia - Tauron Liga F.\x1a\nvolleyball"\x02PL(\x000\x00:\x00J\x00:\x84\x01\n\x02CZ\x12\x10Rep\xc3\xbablica Checa\x1a3\x08\x80M\x12\x16Rep. Checa - Extraliga\x1a\nvolleyball"\x02CZ(\x000\x00:\x00J\x00\x1a7\x08\xb1\xab\x01\x12\x19Rep. Checa - Extraliga F.\x1a\nvolleyball"\x02CZ(\x000\x00:\x00J\x00:E\n\x02RO\x12\x08Rom\xc3\xa9nia\x1a5\x08\xa6u\x12\x18Rom\xc3\xa9nia - 1.\xc2\xaa Divis\xc3\xa3o\x1a\nvolleyball"\x02RO(\x000\x00:\x00J\x00\x12\x89\x01\x12\x0cbeach_volley\x1a\x11Voleibol de Praia*2\x08\xa0\xfb\x01\x12\x12Doha The Finals F.\x1a\x0cbeach_volley"\x02QA(\x000\x00:\x00J\x00*2\x08\x9f\xfb\x01\x12\x12Doha The Finals M.\x1a\x0cbeach_volley"\x02QA(\x000\x00:\x00J\x00'
#%%

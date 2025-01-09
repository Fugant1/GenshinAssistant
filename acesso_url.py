import requests
from bs4 import BeautifulSoup

lista_bonecos_game8 = {
    "Arlecchino":382103, "Mavuika":461999, "Yelan":372781, "Xingqiu":297531,
    "Xiangling":297530, "Raiden Shogun":337161, "Kazuha":332826, "Xilonen":461997,
    "Zhongli":305858, "Mualani":461994, "Kinich":461991, "Navia":417194,
    "Alhaitham":383712, "Hu tao":314347, "Lyney":345540, "Chasca":462001,
    "Clorinde":417218, "Nilou":383715, "Fischl":297524, "Yae Miko":327533,
    "Kuki Shinobu":346199, "Emilie":422493, "Chiori":382793, "Citlali":461989,
    "Chevreuse":426201, "Baizhu":314348, "Kokomi":337140, "Shenhe":346620,
    "Jean":297536, "Sucrose":297525, "Xiao":297527, "Ayaka":315215, "Tartaglia":305862,
    "Diluc":297518, "Ayato":345514, "Tighnari":382082, "Wanderer":309656, "Ganyu":312173,
    "Ororon":461993, "Beidou":297528, "Collei":382079, "Rosaria":314177, "Faruzan":391897,
    "Diona":305872, "Yun Jin":314345, "Yaoyao":314174, "Charlotte":412428, "Kujou Sara":336727,
    "Yoimiya":333497, "Sethos":451024, "Itto":345461, "Cyno":315233, "Noelle":297523,
    "Eula":328764, "Albedo":312182, "Thoma":337141, "Lynette":345879, "Gorou":336726,
    "Kirara":409556, "Mika":390096, "Sigewinne":352956, "Layla":386486, "Sayu":333496,
    "Yanfei":328765, "Heizou":345516, "Klee":297521, "Freminet":417207, "Ningguang":297529,
    "Kachina":462004, "Kaeya":297516, "Chongyun":297532, "Qiqi":297533, "Barbara":297517,
    "Candace":386384, "Dori":380569, "Razor":297519, "Xinyan":305873, "Aloy":337957,
    "Amber":297535
}

url = "https://game8.co/games/Genshin-Impact/archives/"
specific_name = input('Digite o nome do personagem: ')
if(specific_name in lista_bonecos_game8):
    numero_string = str(lista_bonecos_game8[f"{specific_name}"])
    url += numero_string
else:
    url += specific_name 
    url += '-Best-Builds'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    #elemento = soup.find('h2', class_='a-header--2')
    #if(elemento):
    #   print(elemento.text)
    #else:
    #    print('') 

    elementos_td = soup.select('tr > td[width="70%"]')
    itens_especificos = ["CRIT Rate", "CRIT DMG", "Energy Recharge", "HP%", 
                         "Hydro DMG Bonus", "ATK%", 
                         "Elemental Mastery", "DEF%", "Pyro DMG Bonus",
                         "Anemo DMG Bonus", "Geo DMG Bonus", "Cryo DMG Bonus",
                         "Electro DMG Bonus", "Dendro DMG Bonus"]  
    print(f"Atributos relevantes para {specific_name}: ")

    itens_encontrados = set()

    for elemento_td in elementos_td:
        texto_completo = elemento_td.text.strip()  
        lista_itens = [item.strip() for item in texto_completo.split(',')]  
        
        for item in lista_itens:
            if item in itens_especificos:  
                itens_encontrados.add(item)

    for item in itens_encontrados:
        print(f'{item}')
        


    
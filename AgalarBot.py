import discord
from discord.ext.commands import Bot

import requests
from bs4 import BeautifulSoup

cs = requests.get('https://www.gametracker.com/server_info/217.195.202.175:27025')
cs16 = BeautifulSoup(cs.content,"lxml")

#BURAYA TOKEN GİRİLECEK

client = discord.Client()
bot = Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Bot Hazır " + str(bot.user))  

@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ".top":
        top = requests.get('https://www.gametracker.com/server_info/159.146.61.231:27025')
        topindex = BeautifulSoup(top.content,"lxml")
        
        toplist = []
        sayi = 1
        while sayi <= 10:
            isim = topindex.find("td", text="""
					%s.
				""" % str(sayi)).findNext().text.strip()

            puan = topindex.find("td", text="""
					%s.
				""" % str(sayi)).findNext().findNext().findNext().text.strip()

            sure = topindex.find("td", text="""
					%s.
				""" % str(sayi)).findNext().findNext().findNext().findNext().text.strip()


            toplist.append(str(sayi) + ".\t"+ isim + "\t\t\t" + puan + "\t" + sure + "\n")
            sayi+=1

        await message.channel.send(
            toplist[0]+
            toplist[1]+
            toplist[2]+
            toplist[3]+
            toplist[4]+
            toplist[5]+
            toplist[6]+
            toplist[7]+
            toplist[8]+
            toplist[9]
        )

    if message.content == "banner":
        await message.channel.send("https://cache.gametracker.com/server_info/159.146.61.231:27025/b_560_95_1.png")

    if message.content == ".sven" or message.content == ".Sven" or message.content == ".SvenCoop" or message.content == ".sc" or message.content == ".SC" or message.content == ".Sc" or message.content == ".Sven Coop":
        sven = requests.get('https://www.gametracker.com/server_info/159.146.61.231:27025')
        svencoop = BeautifulSoup(sven.content,"lxml")
        
        sven_harita = (svencoop.find("div",attrs={"id":"HTML_curr_map"}).text).strip()
        if sven_harita == "Unknown":
            sven_harita = "Bilinmeyen"
        sven_campaign = sven_harita[0:3]
        if sven_campaign == "hl_":
            sven_campaign = "Half-Life"
        elif sven_campaign == "th_":
            sven_campaign = "They Hunger"
        elif sven_campaign[0:2] == "of" and sven_campaign[3] != "_":
            sven_campaign = "Opposing Force"
        elif sven_campaign == "ba_":
            sven_campaign = "Blue Shift"
        elif sven_campaign == "dy_":
            sven_campaign = "Decay"
        elif sven_campaign == "upl":
            sven_campaign = "Uplink"
        elif sven_campaign == "ins":
            sven_campaign = "Instinct"
        elif sven_campaign[0:2] == "ss":
            sven_campaign = "Ultimate Attack"
        elif sven_campaign == "of_":
            sven_campaign = "Under The Black Moon"
        elif sven_campaign == "Bla":
            sven_campaign = "Black Mesa EPF"
        elif sven_campaign == "dyn":
            sven_campaign = "Dinamik Harita Seçimi"
        else:
            sven_campaign = "Diğer"

        sven_oyuncu_sayisi = (svencoop.find("span",attrs={"id":"HTML_num_players"}).text).strip()
        sven_durum = (svencoop.find("span",attrs={"class":"item_color_success"}).text).strip()
        sven_rank = (svencoop.find("div",attrs={"class":"gttable_crank_marker"}).text).strip()
        sven_rank = sven_rank[0]
        sven_rankint = int(sven_rank)

        sven_rankint = int(458 - 458*(sven_rankint/100))
            
        if sven_durum == "Dead":
            sven_durum = "Bakımda..."
        elif sven_durum == "Alive":
            sven_durum = "Aktif !"

        sven_guncelleme = (svencoop.find("div",attrs={"id":"last_scanned"}).text).strip()
        print(sven_guncelleme)

        dakika = ""
        saniye = ""
        
        if sven_guncelleme[13].isnumeric() and sven_guncelleme[14].isnumeric():
            if sven_guncelleme[23].isnumeric() and sven_guncelleme[24].isnumeric():
                sven_guncelleme = "%s dakika %s saniye önce güncellendi1" % (sven_guncelleme[13:14],sven_guncelleme[23:24])
            elif sven_guncelleme[23].isnumeric():
                sven_guncelleme = "%s dakika %s saniye önce güncellendi2" % (sven_guncelleme[13:14], sven_guncelleme[23])
            else:
                sven_guncelleme = "%s saniye önce güncellendi3" % (sven_guncelleme[13:14])

        elif sven_guncelleme[13].isnumeric():
            if sven_guncelleme[23].isnumeric() and sven_guncelleme[24].isnumeric():
                sven_guncelleme = "%s dakika %s saniye önce güncellendi4" % (sven_guncelleme[13],sven_guncelleme[20:25])
            elif sven_guncelleme[23].isnumeric():
                sven_guncelleme = "%s dakika %s saniye önce güncellendi5" % (sven_guncelleme[13], sven_guncelleme[22])
            else:
                sven_guncelleme = "%s saniye önce güncellendi6" % (sven_guncelleme[13])

        else:
            sven_guncelleme = "%s saniye önce güncellendi7" % (sven_guncelleme[13])

        await message.channel.send("""
        Harita: %s(%s)\nOyuncu Sayısı: %s\nDurum: %s\nServer Rank: %s\nSon güncelleme: %s""" %(sven_campaign,sven_harita,sven_oyuncu_sayisi,sven_durum,str(sven_rankint),sven_guncelleme)
        )

    if message.content == ".cs" or message.content == ".Cs" or message.content == ".CS":
        cs = requests.get('https://www.gametracker.com/server_info/159.146.61.231:27015')
        cs16 = BeautifulSoup(cs.content,"lxml")

        cs_harita = (cs16.find("div",attrs={"id":"HTML_curr_map"}).text).strip()
        cs_oyuncu_sayisi = (cs16.find("span",attrs={"id":"HTML_num_players"}).text).strip()
        cs_durum = (cs16.find("a",attrs={"href":"/server_info/159.146.61.231:27015/manage/"}).text).strip()
        if cs_durum.strip() == "Dead":
            cs_durum = "Offline"
        cs_guncelleme = (cs16.find("div",attrs={"id":"last_scanned"}).text).strip()

        await message.channel.send(
        "Harita: " + cs_harita+"\n"+
        "Oyuncu Sayısı: " + cs_oyuncu_sayisi+"\n"+
        "Durum: " + cs_durum+"\n"+
        "Son güncelleme: " + cs_guncelleme+"."
        )

bot.run(TOKEN)
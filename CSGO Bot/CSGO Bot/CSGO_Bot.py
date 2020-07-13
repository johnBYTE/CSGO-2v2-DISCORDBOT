from PIL import Image, ImageDraw
from PIL import ImageFont, ImageDraw
from PIL import Image, ImageOps, ImageDraw
import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
import pysftp
from discord.utils import get
from itertools import cycle
import asyncio
import datetime
import json
import valve.source.a2s
import valve.source.master_server
import valve.rcon
from valve.source.master_server import MasterServerQuerier
from valve.source.a2s import ServerQuerier, NoResponseError
from ftplib import FTP
import traceback
import string
import time
import math
import os
ranks = ['https://i.imgur.com/YlkddRr.jpg', 'https://i.imgur.com/vlLGymA.jpg', 'https://i.imgur.com/wqF7lME.jpg', 'https://i.imgur.com/EzSgWUW.jpg', 'https://imgur.com/1CtvVCC', 'https://i.imgur.com/Yd1D5N7.jpg', 'https://i.imgur.com/043aoWH.jpg', 'https://i.imgur.com/jLftEZf.jpg', 'https://i.imgur.com/hmZ0p0w.jpg', 'https://i.imgur.com/dYFF57X.jpg', 'https://i.imgur.com/UfBQcpR.jpg', 'https://i.imgur.com/17kz6wy.jpg', 'https://i.imgur.com/bs4bHft.jpg', 'https://i.imgur.com/UR4es3m.jpg', 'https://i.imgur.com/MaCMLLI.jpg', 'https://i.imgur.com/mCzaEHx.jpg', 'https://i.imgur.com/o47ORQW.jpg', 'https://i.imgur.com/eohQA1g.jpg'] 
main_logo = 'https://cdn.discordapp.com/attachments/725118433439645819/725490392736465056/2v2.png'

csgo_logo = 'https://cdn.discordapp.com/attachments/265291806999052288/715765438897848360/ZfAJNyw.png'

#---------------bot event--------------6-#
pref = "!"
bot = commands.Bot(command_prefix=pref)
bot.remove_command('help')
file_name = "5v5bot"
def print_cyan(skk): print("\033[96m{}\033[00m" .format(skk))
def print_green(skk): print("\033[92m{}\033[00m" .format(skk))
def print_yellow(skk): print("\033[93m{}\033[00m" .format(skk))
def print_red(skk): print("\033[91m{}\033[00m" .format(skk))

player_ids = []
player_list = []
running_games_list = []
ended_games_list = []
suggestions = []
average_perms = ["724754012364079155","724754013085630535","724754014184407141","724754019268165653"]
middle_perms = ["724754013085630535","724754014184407141","724754019268165653"]
high_perms = ["724754014184407141","724754019268165653"]


server0_pass = ''
server1_pass = ''
server2_pass = ''
server3_pass = ''

async def removeroles(team1, team2):
    for i in bot.servers:
        server1 = i
        for x in server1.members:
            role_ids = [role.id for role in x.roles]

            if team1.id in role_ids:
                await bot.remove_roles(x,team1)
                print(f'removed + {team1.name}')
            if team2.id in role_ids:
                await bot.remove_roles(x,team2)
                print(f'removed + {team2.name}')
    print('done!')

blacklisted_members = []
async def file_exists():
    try:
        open(f"{file_name}" , "r")
        return True
    except:
        return False

async def save_empty():
    fo = open(f"{file_name}", "r")
    counter = 0
    for i in fo:
        counter += 1
    if counter != 0:
        return False
    else:
        return True

async def get_discord_member(id):
    for i in bot.servers:
        return discord.utils.get(i.members, id=f"{id}")

    return None

async def get_player_member(id):
    for i in player_list:
        if i.id == id:
            return i

async def check_players():
    while(True):
        for i in player_list:
            counter = 0
            for x in player_list:
                if x.id == i.id:
                    counter += 1
            if counter > 1:
                player_list.remove(x)
        await asyncio.sleep(10)

async def save_players():
    f = open(f'{file_name}', 'w') #write mode
    used_players = []
    for player in player_list:
        try:
            if player.id not in used_players:
                f.write(f"ID:{player.id}\nWINS:{int(player.wins)}\nLOSES:{int(player.loses)}\nELO:{int(player.elo)}\nWINSTREAK:{int(player.winstreak)}\nEND_PLAYER\n")
                used_players.append(player.id)
        except:
            print_red(f"FMM {player.id}")
    f.close()


async def randomPass_west():
    string_lol = ''
    letters = string.ascii_uppercase 
    return ''.join(random.choice(letters) for i in range(8))

async def change_map(finalmap, server, over=True):


    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None   
    do_ftp = False

    ftp_add = ''
    ftp_port = 0
    ftp_cred = []
    ftp_direct = ''
    address = []
    final_map = ''

    if finalmap == 'dust':
        final_map = 'de_dust_bg5v5'
    elif finalmap == 'dust2_old':
        final_map = 'de_dust2_old_bg5v5'
    elif finalmap == 'nuke':
        final_map = 'de_nuke'
    elif finalmap == 'train':
        final_map = 'de_train'   
    else:
        final_map = finalmap




    finalmap = final_map
    do_ftp = True
    if int(server) == 2:
        ftp_add = '98.174.158.25'
        ftp_port = 22
        ftp_cred = ['csgo', 'PoopButt123']
        ftp_direct = '/home/csgo/Steam/csgo-ds/csgo'



        final_name = 'Match.cfg'
        address = [("98.174.158.25", 27015), 'PoopButt123'] 
        ip = '98.174.158.25:27015'




        
        do_ftp = False


    if int(server) == 3:
        
        ftp_add = 'east5v5.game.nfoservers.com'
        ftp_port = 21
        ftp_cred = ['dylanlua', 'Thewall10']
        ftp_direct = '/csgo'

        address = [("east5v5.game.nfoservers.com", 27015), 'QJXjjq'] 

        ip = 'east5v5.game.nfoservers.com:27015'

        final_name = 'Match.cfg'


        do_ftp = True

    if int(server) == 0:
        ftp_add = '3.7.164.232'
        ftp_port = 21
        ftp_cred = ['ftpuser', 'casioctk230']
        ftp_direct = '/'



        final_name = 'Match.cfg'
        address = [("3.7.164.232", 27066), 'j7utiqiv'] 
        ip = '3.7.164.232:27066'






        do_ftp = True
    if int(server) == 1:



        ftp_add = 'twoversustwo.game.nfoservers.com'
        ftp_port = 21
        ftp_cred = ['twoversustwo', 'RyzjgXZGqD6GgWy']
        ftp_direct = '/csgo'




        final_name = 'Match.cfg'
        
        address = [("twoversustwo.game.nfoservers.com", 27015), 'nC9nLQ83274HPFhfhI424']

        ip = 'twoversustwo.game.nfoservers.com:27015'

        do_ftp = True




    if do_ftp:  
        my_ftp = FTP()
        my_ftp.connect(ftp_add, ftp_port)
        my_ftp.login(ftp_cred[0], ftp_cred[1])
        print(my_ftp.getwelcome())
        my_ftp.cwd(ftp_direct)
        files = my_ftp.nlst()
        
        for file in files:
            if final_name == str(file):
                filename = file
                print(file)

                with open(filename, 'wb') as fp:
                    my_ftp.retrbinary('RETR ' + filename, fp.write)

                with open(final_name, 'r') as f:
                    lines = f.readlines()
                    map = lines[20].strip()
                    f.close
                with open(final_name, 'rt') as f:
                    data = f.read()
                    data = data.replace(map, str(finalmap))
                    f.close()
                with open(final_name, 'wt') as f:
                    f.write(data)
                    f.close()

                    
                with open(filename, 'rb') as fp:
                    print('success')
                    res = my_ftp.storlines("STOR " + filename, fp)
                    print(str(res))
                    
                    if not res.startswith('226 Transfer complete'):
                
                        print('Upload failed')
                my_ftp.quit()



        os.remove(final_name) 

    if not do_ftp:   
        with pysftp.Connection(host=ftp_add, username=ftp_cred[0], port=ftp_port, password=ftp_cred[1], cnopts=cnopts) as sftp:
            print("connected")
            sftp.cwd(ftp_direct)

            sftp.get(final_name)

            with open(final_name, 'r') as f:
                lines = f.readlines()
                map = lines[20].strip()
                f.close()
            with open(final_name, 'rt') as f:
                data = f.read()
                data = data.replace(map, str(finalmap))
                f.close()
            with open(final_name, 'wt') as f:
                f.write(data)
                f.close()

            sftp.put(final_name)

        os.remove(final_name)

    if over:
        with valve.rcon.RCON(address[0], address[1]) as rcon:
            response = rcon.execute("sm_endmatch")

            print(str(response))
        with valve.rcon.RCON(address[0], address[1]) as rcon:
            print(str(final_name))
            response = rcon.execute(f"sm_load {final_name}")

            print(str(response))


async def change_password(server, t1=[], t2=[]):

    global server1_pass
    global server2_pass
    global server3_pass
    global server0_pass

    #print('men')


    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None   

    ftp_add = ''
    ftp_port = 0
    ftp_cred = []
    ftp_direct = ''
    address = []

    strip_num = ''

    final_name = ''

    new_pass = await randomPass_west()
    print(str(new_pass))
    do_ftp = False



    #server = 2
    print(str(server))
    if int(server) == 2:
        ftp_add = '98.174.158.25'
        ftp_port = 22
        ftp_cred = ['csgo', 'PoopButt123']
        ftp_direct = '/home/csgo/Steam/csgo-ds/csgo/cfg'



        final_name = 'server.cfg'
        address = [("98.174.158.25", 27015), 'PoopButt123'] 
        ip = '98.174.158.25:27015'

        strip_num = 5

        server3_pass = new_pass
        
        do_ftp = False
         


    if int(server) == 3:
        return
        ftp_add = 'east5v5.game.nfoservers.com'
        ftp_port = 21
        ftp_cred = ['dylanlua', 'Thewall10']
        ftp_direct = '/csgo/cfg'

        address = [("east5v5.game.nfoservers.com", 27015), 'QJXjjq'] 

        ip = 'east5v5.game.nfoservers.com:27015'

        final_name = 'server.cfg'

        strip_num = 193

        server1_pass = new_pass
        do_ftp = True

    if int(server) == 0:
        ftp_add = '3.7.164.232'
        ftp_port = 21
        ftp_cred = ['ftpuser', 'casioctk230']
        ftp_direct = '/cfg'

        

        final_name = 'csgoserver.cfg'
        address = [("3.7.164.232", 27066), 'j7utiqiv'] 
        ip = '3.7.164.232:27066'

        strip_num = 3

        server2_pass = new_pass
        do_ftp = True
    if int(server) == 1:
        ftp_add = 'twoversustwo.game.nfoservers.com'
        ftp_port = 21
        ftp_cred = ['twoversustwo', 'RyzjgXZGqD6GgWy']
        ftp_direct = '/csgo/cfg'




        final_name = 'server.cfg'
        
        address = [("twoversustwo.game.nfoservers.com", 27015), 'nC9nLQ83274HPFhfhI424']

        ip = 'twoversustwo.game.nfoservers.com:27015'

        strip_num = 5

        server0_pass = new_pass
        do_ftp = True

    if int(server) == 4:
        return

   
    print(str(new_pass))
    print(str(address[0]))
    print(str(address[1]))

   # try:
    with valve.rcon.RCON(address[0], address[1]) as rcon:
        response = rcon.execute('sv_password ' + str(new_pass))
        #response = rcon.execute("sm_map mirage")
        print(str(response))

    with valve.rcon.RCON(address[0], address[1]) as rcon:
        response = rcon.execute("sm_reloadadmins")
        #response = rcon.execute("sm_map mirage")
        print(str(response))
 #   except:
        #print('y fail " (') 



    if do_ftp:
        my_ftp = FTP()
        my_ftp.connect(ftp_add, ftp_port)
        my_ftp.login(ftp_cred[0], ftp_cred[1])
        print(my_ftp.getwelcome())
        my_ftp.cwd(ftp_direct)
        files = my_ftp.nlst()
        
        for file in files:
            if final_name == str(file):
                filename = file
                print(file)

                with open(filename, 'wb') as fp:
                    my_ftp.retrbinary('RETR ' + filename, fp.write)

                with open(final_name, 'r') as f:
                    lines = f.readlines()
                    password = lines[strip_num].strip()
                    f.close
                with open(final_name, 'rt') as f:
                    data = f.read()
                    data = data.replace(password, 'sv_password ' + str(new_pass))
                    f.close()
                with open(final_name, 'wt') as f:
                    f.write(data)
                    f.close()

                    
                with open(filename, 'rb') as fp:
                    print('success')
                    res = my_ftp.storlines("STOR " + filename, fp)
                    print(str(res))
                    
                    if not res.startswith('226 Transfer complete'):
                
                        print('Upload failed')

        
            

                my_ftp.quit()
        os.remove(final_name)
    if not do_ftp:   
        with pysftp.Connection(host=ftp_add, username=ftp_cred[0], port=ftp_port, password=ftp_cred[1], cnopts=cnopts) as sftp:
            print("connected")
            sftp.cwd(ftp_direct)

            sftp.get(final_name)

            with open(final_name, 'r') as f:
                lines = f.readlines()
                password = lines[strip_num].strip()
                f.close
            with open(final_name, 'rt') as f:
                data = f.read()
                data = data.replace(password, 'sv_password ' + str(new_pass))
                f.close()
            with open(final_name, 'wt') as f:
                f.write(data)
                f.close()

            sftp.put(final_name)

        os.remove(final_name)

    with valve.rcon.RCON(address[0], address[1]) as rcon:
        response = rcon.execute('sv_password ' + str(new_pass))
        #response = rcon.execute("sm_map mirage")
        print(str(response))

    if t1 != []:
        serverip = discord.Embed(description=f"```\nconnect {ip}; password {new_pass}```" ,color = 0xfe4040)
        serverip.set_footer(text = f'CS:GO 5v5 bot', icon_url = csgo_logo)
        serverip.set_author(name="Server IP:", icon_url = csgo_logo)
        serverip.add_field(name="**Direct connect:**", value=f"[steam://connect/{ip};/{new_pass}](steam://connect/{ip};/{new_pass})", inline=False)
        serverip.set_thumbnail(url=main_logo)
        for i in range(len(t1)):
            try:


                await bot.send_message(t1[i], embed=serverip)
                await bot.send_message(t1[i], "If the match is full you have to join through console.\n \nIf it says 'Bad password' or 'You are not a player in this match' simply type retry in console. If this issue persists message an Admin. ")
            except:
                 print('co')
    if t2 != []:
        embed1 = discord.Embed(title="PASSWORD: " + new_pass, description=f"\n```connect {ip}; password {new_pass}```" ,color=discord.Color.blue())
        embed2 = discord.Embed(title="JOIN: ", description=f'steam://connect/{ip};/{new_pass}' ,color=discord.Color.blue())
        for i in range(len(t2)):
            try:
                await bot.send_message(t2[i], embed=serverip)
                await bot.send_message(t2[i], "If the match is full you have to join through console.\n \nIf it says 'Bad password' or 'You are not a player in this match' simply type retry in console. If this issue persists message an Admin. ")
            except:
                print('a')



async def oldpasschangeIGNORE(server, t1=[], t2=[]):
   
    return
    global server1_pass
    global server2_pass
    global server3_pass
    global server0_pass

    print('men')




    ftp_add = ''
    ftp_port = 0
    ftp_cred = []
    ftp_direct = ''
    address = []

    strip_num = ''

    final_name = ''

    new_pass = await randomPass_west()
    print(str(new_pass))
    do_ftp = False




    print(str(server))
    if int(server) == 1: #2020 server 



     








        ftp_add = 'twoversustwo.game.nfoservers.com'
        ftp_port = 21
        ftp_cred = ['twoversustwo', 'RyzjgXZGqD6GgWy']
        ftp_direct = '/csgo/cfg'




        final_name = 'server.cfg'
        
        address = [("twoversustwo.game.nfoservers.com", 27015), 'nC9nLQ83274HPFhfhI424']

        ip = 'twoversustwo.game.nfoservers.com:27015'

        strip_num = 5

        server0_pass = new_pass
        do_ftp = True


    if int(server) == 3: #2v2 server 2
        ftp_add = '176.57.158.200'
        ftp_port = 21
        ftp_cred = ['gpftp1122507392175613', 'm5FD0MDJ']
        ftp_direct = '/csgo/cfg'

        address = [("176.57.158.200", 27015), 'sefumati23'] 

        ip = '176.57.158.200:27015'

        final_name = 'server.cfg'

        strip_num = 3

        server1_pass = new_pass
        do_ftp = True

    if int(server) == 0:#5v5 server 1

        print('3')
        ftp_add = '176.57.158.203'
        ftp_port = 21
        ftp_cred = ['gpftp1122507392177713', 'w19jmFw7']
        ftp_direct = '/csgo/cfg'

        final_name = 'server.cfg'

        ip = '176.57.158.203:27015'

        strip_num = 3
        address = [("176.57.158.203", 27015), 'sefumati23'] 

        server2_pass = new_pass
        do_ftp = True
    if int(server) == 2: #2v2 server 1
       # return
        print('4')
        ftp_add = '176.57.158.181'
        ftp_port = 21
        ftp_cred = ['gpftp1122507392174413', 'cmYdiRXA']
        ftp_direct = '/csgo/cfg'

        final_name = 'server.cfg'

        ip = '176.57.158.181:27015'

        strip_num = 1


        address = [("176.57.158.181", 27015), 'sefumati23'] 

        server3_pass = new_pass
        do_ftp = True


   
    print(str(new_pass))
    print(str(address[0]))
    print(str(address[1]))

    #try:
    with valve.rcon.RCON(address[0], address[1]) as rcon:
        response = rcon.execute('sv_password "' + str(new_pass) + '"')
        #response = rcon.execute("sm_map mirage")
        print(str(response))


 #   with valve.rcon.RCON(address[0], address[1]) as rcon:
  #      response = rcon.execute("sm_map mirage")
   #     #response = rcon.execute("sm_map mirage")
   #     print(str(response))
   # except:
    #$    print('y fail " (') 



    if do_ftp:
        my_ftp = FTP()
        my_ftp.connect(ftp_add, ftp_port)
        my_ftp.login(ftp_cred[0], ftp_cred[1])
        print(my_ftp.getwelcome())
        my_ftp.cwd(ftp_direct)
        files = my_ftp.nlst()
        
        for file in files:
            if final_name == str(file):
                filename = file
                print(file)

                with open(filename, 'wb') as fp:
                    my_ftp.retrbinary('RETR ' + filename, fp.write)

                with open(final_name, 'r') as f:
                    #lines = f.read().splitlines()
                    lines = [line[:-1] for line in f]
                    password = lines[strip_num].strip()
                    f.close()
                with open(final_name, 'rt') as f:
                    data = f.read()
                    data = data.replace(password, 'sv_password ' + str(new_pass) + '')
                    f.close()
                with open(final_name, 'wt') as f:
                    f.write(data)
                    f.close()

                    
                with open(filename, 'rb') as fp:
                    print('success')
                    res = my_ftp.storbinary("STOR " + filename, fp)
                    print(str(res))
                    
                    if not res.startswith('226 Transfer complete'):
                
                        print('Upload failed')

        
            

                my_ftp.quit()
        os.remove(final_name)





    if t1 != []:


        serverip = discord.Embed(description=f"```\nconnect {ip}; password {new_pass}```" ,color = 0xfe4040)
        serverip.set_footer(text = f'2v2', icon_url = main_logo)
        serverip.set_author(name="Server IP:", icon_url = main_logo)
        serverip.add_field(name="**Direct connect:**", value=f"[steam://connect/{ip};/{new_pass}](steam://connect/{ip};/{new_pass})", inline=False)
        serverip.set_thumbnail(url=main_logo)



        for i in range(len(t1)):
            try:
                await bot.send_message(t1[i], embed=serverip)
                await bot.send_message(t1[i], "If the match is full you have to join through console.\n \nIf it says 'Bad password' or 'You are not a player in this match' simply type retry in console. If this issue persists message an Admin. ")
            except:
                 print('co')
    if t2 != []:
        serverip2 = discord.Embed(description=f"```\nconnect {ip}; password {new_pass}```" ,color = 0xfe4040)
        serverip2.set_footer(text = f'2v2', icon_url = main_logo)
        serverip2.set_author(name="Server IP:", icon_url = main_logo)
        serverip2.add_field(name="**Direct connect:**", value=f"[steam://connect/{ip};/{new_pass}](steam://connect/{ip};/{new_pass})", inline=False)
        serverip2.set_thumbnail(url=main_logo)
        for i in range(len(t2)):
            try:
                await bot.send_message(t2[i], embed=serverip2)
                await bot.send_message(t2[i], "If the match is full you have to join through console.\n \nIf it says 'Bad password' or 'You are not a player in this match' simply type retry in console. If this issue persists message an Admin. ")
            except:
                print('a')



async def load_players():
            # Open a file
    fo = open(f"{file_name}", "r")
    player_name = ""
    player_id = 0
    player_wins = 0
    player_loses = 0
    player_elo = 0
    player_winstreak= 0
    counter_loaded = 0
    counter = 0
    for x in fo:

        if(counter == 0):
            player_id = x[x.find(":") + 1:len(x) - 1]
        if(counter == 1):
            player_wins = int(x[x.find(":") + 1:len(x) - 1])
        if(counter == 2):
            player_loses = int(x[x.find(":") + 1:len(x) - 1])
        if(counter == 3):
            player_elo = int(x[x.find(":") + 1:len(x) - 1])
        if(counter == 4):
            player_winstreak = int(x[x.find(":") + 1:len(x) - 1])

        counter += 1

        if x == "END_PLAYER\n":
            counter = 0
            member = await get_discord_member(player_id)
            if not player_id in player_ids:
                player_list.append(Player(player_id , member, player_elo , player_wins , player_loses ,player_winstreak))
                player_ids.append(player_id)
                try:
                    print_cyan(f"Loaded {member.name} with ID:{player_id}")
                except:
                    print_cyan(f"Loaded ¯\_(ツ)_/¯ with ID:{player_id}")
                counter_loaded += 1

    print_green(f"Finished loading {counter_loaded} players")

class Player:
    def __init__(self, id, member = None, elo = 0,wins = 0 , loses = 0 , winstreak = 0):
        self.id = id
        self.member = member
        self.wins = wins
        self.loses = loses
        self.winstreak = winstreak
        self.elo = elo
        self.leaderboard_rank = len(player_list) + 1
        self.blackcapt = False
    def add_elo(self , elo):
        self.elo += elo

    def set_elo(self , elo):
        self.elo = elo

    def add_win(self , win_amount = 1):
        self.wins += win_amount

    def add_lose(self , lose_amount = 1):
        self.loses += lose_amount


cooldown = []
class Blacklist:
    def __init__(self , time,expire_time,user):
        self.time = time
        self.expire_time = expire_time
        self.user = user

maplist = ['inferno', 'shortnuke', 'overpass', 'shortdust', 'train', 'rialto', 'de_cbble', 'lake']
class Game:
    def __init__(self , team1 , team2 , hoster , waiting_players):
        self.game_id = len(running_games_list) + len(ended_games_list) + 1
        self.match_channel_number = 0
        self.team1 = team1
        self.team2 = team2
        self.winning_team = []
        self.losing_team = []
        self.winning_team_elo = [0,0,0,0,0]
        self.losing_team_elo = [0,0,0,0,0]
        self.hoster = hoster
        self.waiting_players = waiting_players
        self.captain_team1 = None
        self.captain_team2 = None
        self.turn = None
        self.elox = 1
        self.veto_stage = False
        self.maps = ['inferno', 'shortnuke', 'overpass', 'shortdust', 'train', 'rialto', 'cbble', 'lake']
        self.game_id = 0
        self.embed_msg = ''
        self.stats_msg = ''
        self.picks = 0
        self.update_this_tick = True
        self.playing_players = []
        self.is_2v2 = True
        self.msg_channel = ''
        self.lby = False
        self.game_join_stage_ended = False
        self.game_has_started = False
        self.game_has_ended = False
        self.game_has_been_canceled = False
        self.picked_players = []

async def find_player(id):
    for i in player_list:
        if i.id == id:
            return i
@bot.event
async def on_member_join(member):
    if not member.bot and not (member.id in player_ids): # if the player hasn't been added go ahead and add him
        player_list.append(Player(member.id , member ,1000))
        player_ids.append(member.id) # store added ids for faster and cleaner code duplicate check
        print_green(f"Added {member.name}")

@bot.event
async def on_user_update(before, after):
    if before.bot:
        return
    for i in player_list:
        if i.id == before.id:
            i.member = after
@bot.event
async def on_member_remove(member):
    if member.bot:
        return
    for i in player_list:
        if i.id == member.id:
            i.member = None

@bot.event
async def on_ready():
      #  await change_map('mirage',1)
        await change_password(1)
        await change_password(2)

        await bot.change_presence(game=discord.Game(url="https://www.twitch.tv/pokimane", type=1, name='!commands'))

     #   await change_password(0)
      #  await change_map('mirage')
       # await change_password(1)
     #   await change_password(2)
     #   await change_password(3)

        print_red('---------------|')
        print_red('Bot is online. |')
        print_red('---------------|')

        length = len('---------------|')
        spaces = ""
        for i in range(length - len(bot.user.name) - 1):
            spaces += " "
        print_red(bot.user.name+ spaces + "|")
        print_red('---------------|')

        if(not await file_exists() or await save_empty()):
            await add_players()
            await save_players()
        else:
            await load_players()
            await add_players()
            await save_players()

        await check_players()
        
        print(180 / 3.141592653589793238462643383279502884197169399)

async def is_allowed(member , role_list):
    role_ids = [role.id for role in member.roles]

    for i in role_ids:
        if i in role_list:
            return True

    return False
async def add_players():
    counter = 0
    for i in bot.servers:
        for x in i.members:
            if not x.bot and not (x.id in player_ids): # if the player hasn't been added go ahead and add him
                player_list.append(Player(x.id , x ,1000))
                player_ids.append(x.id) # store added ids for faster and cleaner code duplicate check
                print_green(f"Added {x.name}")
                counter += 1
    print_cyan(f"Added {counter} players")

async def update_leaderboard():
    player_list.sort(key=lambda x: x.elo, reverse=True)
    counter = 1
    for i in player_list:
        i.leaderboard_rank = counter
        counter += 1
@bot.command(pass_context = True)
async def suggest(ctx , *suggestion):
    str_suggestion = ""
    for i in suggestion:
        str_suggestion += i + " "
    suggestions.append(str_suggestion)

@bot.command(pass_context = True)
async def see_suggestions(ctx , id = None):
    counter = 0
    if not await is_allowed(ctx.message.author , high_perms):
        return await bot.say("You're not allowed to see suggestions!")
    if id == None:
        for i in suggestions:
            counter += 1
            await bot.say(f"Suggestion #{counter}: {i}")
    else:
        try:
            id = int(id)
        except:
            return await bot.say("Suggestion ID has to be a number!")
        if id >= len(suggestions):
            return await bot.say(f"Suggestion ID #{id} doesn't exist!")
            await bot.say(f"Suggestion #{id}: {suggestions[id - 1]}")


@bot.command(pass_context = True)
async def delete_suggestion(ctx , id):
#    try:
    try:
        id = int(id)
    except:
        await bot.say("ID has to be a number!")
    try:
        suggestions.remove(suggestions[id - 1])
    except:
        await bot.say("Some error idk cbb to finish this rn")





@bot.command(pass_context = True)
async def resetleaderboard(ctx):
    if ctx.message.author.id == "697324319751012383":
        for i in player_list:
            i.elo = 1000
            i.wins = 0
            i.loses = 0
            i.winstreak = 0
        await save_players()
   
    
@bot.command(pass_context = True, aliases=['blacklists'])
async def blackinfo(ctx):
    str = ''
    finalname = ''

    for i in blacklisted_members:

      #  member = await get_discord_member(i.user.id)

     #   if member == None:
    #        str += ''f
     #   else:
      #      finalname = member.name

        
        hours = (i.expire_time - time.time()) / 3600
        minutes = int((hours - int(hours)) * 60)
        rounded_hours = int((i.expire_time - time.time()) / 3600)
        finalname = f'<@{i.user.id}>'
      

        if hours < 1:
            str += f'{finalname} is blacklisted for another **{minutes}m.**\n'
        else:
            str += f'{finalname} is blacklisted for another **{rounded_hours}h** and **{minutes}m.**\n'

    if not str == '':

        embed = discord.Embed(title='Blacklisted users:', description=str, color=0xfe4040)
        return await bot.say(embed=embed)
    else:
        return await bot.say(f"Nobody is currently blacklisted.")

@bot.command(pass_context = True, aliases=['top'])
async def leaderboard(ctx , page = 1):
    if ctx.message.channel.name != "stats":
       stats_channel = discord.utils.get(ctx.message.server.channels, id="709107232830259240")
       return await bot.say(f"You can only use this command in {stats_channel.mention}")

    
    page = max(1,page)
    await update_leaderboard()
    await save_players()
    server = ctx.message.server
    str_1 = ''
    player_per_page = 10

    if(type((len(player_list)) / player_per_page) != int):
        pages = math.ceil(len(player_list)/ player_per_page)
    else:
        pages = (len(player_list)) / player_per_page



    if(page > pages and pages > 1):
        return await bot.say(f"I'm afraid there's only {pages} pages")
    if(page > pages and pages == 1):
        return await bot.say(f"I'm afraid there's only {pages} page")
    for y in range(player_per_page * page - player_per_page, player_per_page * page):
        int_elo = int(player_list[y].elo)
        try:
            member = await bot.get_user_info(str(player_list[y].id))
            appname = member.name[0:12]
        except:

            appname = 'Invalid User'

        remainder = 6 - len(appname) 
        remainder1 = 6 - len(str(player_list[y].elo)) 
        remainder2 = 2 - len(str(player_list[y].wins)) 
        remainder3 = 2 - len(str(player_list[y].loses)) 

        if y == 9:
            remainder = remainder - 1
        str_1 += f"{str(y + 1)}. {appname}" + ''.join(' ' for i in range(11+ remainder)) + f'{str(player_list[y].elo)}' + ''.join(' ' for i in range(2+ remainder1)) +f'  {str(player_list[y].wins)}' + ''.join(' ' for i in range(3+ remainder2)) + f' {str(player_list[y].loses)}' + ''.join(' ' for i in range(4+ remainder3))+f'{str(player_list[y].winstreak)}\n'
        
    cool = ctx.message.author.avatar_url.split('/avatars/')
    try:
        final = cool[1].split('.jpg')
        final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
    except:
        final_av = ctx.message.author.default_avatar_url


    embed = discord.Embed(title=f"Leaderboard Ranks", color=0xfe4040, timestamp=datetime.datetime.utcnow())
    embed.description = ('```css\nRank Player         Elo      Wins  Losses Streak\n``` \n' + f"```yaml\n{str_1}```")
    embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=final_av)
    embed.set_thumbnail(url=main_logo)
    embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=final_av)
    return await bot.say(embed=embed)

@bot.command(pass_context = True)
async def stats(ctx , user: discord.Member = None):
    if ctx.message.channel.name != "stats":
        return await bot.say("You can only use this command in #stats-leaderboard", delete_after=3.0)
    user = ctx.message.author if not user else user
    await update_leaderboard()
    await save_players()
    for y in player_list:
        if y.id == user.id:

            cool = ctx.message.author.avatar_url.split('/avatars/')
            try:
                final = cool[1].split('.jpg')
                final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
            except:
                final_av = ctx.message.author.default_avatar_url

            find_rank = y.elo
            final_rank = round(find_rank / 1000)
            print(final_rank)

            
            rank_p = y.leaderboard_rank
            print(rank_p)
            rank_p = int(rank_p)
            if rank_p > 0 and rank_p < 5:
                rank = ranks[len(ranks)-1] # 18
            elif rank_p >= 5 and rank_p < 15:
                rank = ranks[len(ranks)-2]    # 17   
            elif rank_p >= 15 and rank_p < 30:
                rank = ranks[len(ranks)-2]# 16
            elif rank_p >= 30 and rank_p < 50:
                rank = ranks[len(ranks)-3]# 15
            elif rank_p >= 50 and rank_p < 70:
                rank = ranks[len(ranks)-4]# 14
            elif rank_p >= 70 and rank_p < 100:
                rank = ranks[len(ranks)-5]# 13
            elif rank_p >= 100 and rank_p < 120:
                rank = ranks[len(ranks)-6]# 12
            elif rank_p >= 120 and rank_p < 140:
                rank = ranks[len(ranks)-7]# 11
            elif rank_p >= 140 and rank_p < 160:
                rank = ranks[len(ranks)-8]# 10
            elif rank_p >= 160 and rank_p < 140:
                rank = ranks[len(ranks)-8]# 9
            elif rank_p >= 160 and rank_p < 180:
                rank = ranks[len(ranks)-10]# 8
            elif rank_p >= 180 and rank_p < 200:
                rank = ranks[len(ranks)-11]# 7
            elif rank_p >= 200 and rank_p < 220:
                rank = ranks[len(ranks)-12]# 6
            elif rank_p >= 220 and rank_p < 240:
                rank = ranks[len(ranks)-13]# 5
            elif rank_p >= 240 and rank_p < 260:
                rank = ranks[len(ranks)-14]# 4
            elif rank_p >= 260 and rank_p < 280:
                rank = ranks[len(ranks)-15]# 3
            elif rank_p >= 280 and rank_p < 300:
                rank = ranks[len(ranks)-16]# 2
            elif rank_p >= 300 and rank_p < 320:
                rank = ranks[len(ranks)-17]# 1  
            else:
                rank = ranks[0]# 0 


            remainder = 7 - len(user.name) 
            remainder1 = 6 - len(str(y.elo)) 
            remainder2 = 2 - len(str(y.wins)) 
            remainder3 = 2 - len(str(y.loses)) 
            if rank_p < 10:
                remainder = remainder + 2


            embed = discord.Embed(title=f"Stats for {user.name}", color=0xfe4040, timestamp=datetime.datetime.utcnow())

            embed.description = ('```css\nRank Player            Elo   Wins  Losses Streak\n``` \n' + f'```yaml\n{y.leaderboard_rank}.{user.name}'+''.join(' ' for i in range(11+ remainder))+              f' {y.elo}   {y.wins}     {y.loses}     {y.winstreak}\n```')
            embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=final_av)
            print(rank)
            embed.set_image(url=f'{rank}')


            return await bot.say(embed=embed)

@bot.command(pass_context = True)
async def rank(ctx , rank):
    await update_leaderboard()
    y = None
    rank = int(rank)
    if rank == 0:
        return await bot.say(f"There's no player ranked 0")
    try:
        y = player_list[rank - 1]
    except:
        return await bot.say(f"There's no player ranked {rank}")
    name = ""
    member = await get_discord_member(y.id)
    if member != None:
        name = member.name
    else:
        name = "¯\_(ツ)_/¯"

    cool = ctx.message.author.avatar_url.split('/avatars/')
    try:
        final = cool[1].split('.jpg')
        final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
    except:
        final_av = ctx.message.author.default_avatar_url

    find_rank = y.elo
    final_rank = round(find_rank / 1000)
    print(final_rank)

    #REDO THIS CODE IS SOOOO DISGUSTINGLY BAD
    rank_p = y.leaderboard_rank
    print(rank_p)
    rank_p = int(rank_p)
    if rank_p > 0 and rank_p < 5:
        rank = ranks[len(ranks)-1] # 18
    elif rank_p >= 5 and rank_p < 15:
        rank = ranks[len(ranks)-2]    # 17   
    elif rank_p >= 15 and rank_p < 30:
        rank = ranks[len(ranks)-2]# 16
    elif rank_p >= 30 and rank_p < 50:
        rank = ranks[len(ranks)-3]# 15
    elif rank_p >= 50 and rank_p < 70:
        rank = ranks[len(ranks)-4]# 14
    elif rank_p >= 70 and rank_p < 100:
        rank = ranks[len(ranks)-5]# 13
    elif rank_p >= 100 and rank_p < 120:
        rank = ranks[len(ranks)-6]# 12
    elif rank_p >= 120 and rank_p < 140:
        rank = ranks[len(ranks)-7]# 11
    elif rank_p >= 140 and rank_p < 160:
        rank = ranks[len(ranks)-8]# 10
    elif rank_p >= 160 and rank_p < 140:
        rank = ranks[len(ranks)-8]# 9
    elif rank_p >= 160 and rank_p < 180:
        rank = ranks[len(ranks)-10]# 8
    elif rank_p >= 180 and rank_p < 200:
        rank = ranks[len(ranks)-11]# 7
    elif rank_p >= 200 and rank_p < 220:
        rank = ranks[len(ranks)-12]# 6
    elif rank_p >= 220 and rank_p < 240:
        rank = ranks[len(ranks)-13]# 5
    elif rank_p >= 240 and rank_p < 260:
        rank = ranks[len(ranks)-14]# 4
    elif rank_p >= 260 and rank_p < 280:
        rank = ranks[len(ranks)-15]# 3
    elif rank_p >= 280 and rank_p < 300:
        rank = ranks[len(ranks)-16]# 2
    elif rank_p >= 300 and rank_p < 320:
        rank = ranks[len(ranks)-17]# 1  
    else:
        rank = ranks[0]# 0 


    remainder = 7 - len(name) 
    remainder1 = 6 - len(str(y.elo)) 
    remainder2 = 2 - len(str(y.wins)) 
    remainder3 = 2 - len(str(y.loses)) 
    if rank_p < 10:
        remainder = remainder + 2


    embed = discord.Embed(title=f"Stats for {name}", color=0xfe4040, timestamp=datetime.datetime.utcnow())

    embed.description = ('```css\nRank Player            Elo   Wins  Losses Streak\n``` \n' + f'```yaml\n{y.leaderboard_rank}.{name}'+''.join(' ' for i in range(11+ remainder))+              f' {y.elo}   {y.wins}     {y.loses}     {y.winstreak}\n```')
    embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=final_av)
    print(rank)
    embed.set_image(url=f'{rank}')

    return await bot.say(embed=embed)



@bot.command(pass_context = True)
async def addelo(ctx , user: discord.Member , elo):
    elo = int(elo)
    if not await is_allowed(ctx.message.author , high_perms):
        return
    await save_players()
    for y in player_list:
        if y.id == user.id:
            y.add_elo(elo)

            cool = ctx.message.author.avatar_url.split('/avatars/')
            try:
                final = cool[1].split('.jpg')
                final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
            except:
                final_av = ctx.message.author.default_avatar_url


            embed = discord.Embed(description = f"**Added {elo} elo to {user.name}**" ,color = 0xfe4040)
            embed.set_footer(text = f'{ctx.message.author.name}' ,icon_url = final_av)
            #embed.set_footer(text=f"{ctx.message.author}", icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
            msg = await bot.say(embed=embed)
            await bot.delete_message(ctx.message)
            return await save_players()


@bot.command(pass_context = True)
async def removeelo(ctx , user: discord.Member , elo):
    elo = int(elo)
    if not await is_allowed(ctx.message.author , high_perms):
        return
    await save_players()
    for y in player_list:
        if y.id == user.id:
            if y.elo >= elo:
                y.add_elo(-elo)



                cool = ctx.message.author.avatar_url.split('/avatars/')
                try:
                    final = cool[1].split('.jpg')
                    final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
                except:
                    final_av = ctx.message.author.default_avatar_url


                embed = discord.Embed(description = f"**Removed {elo} elo from {user.name}**" ,color = 0xfe4040)
                embed.set_footer(text = f'{ctx.message.author.name}' ,icon_url = final_av)
                #embed.set_footer(text=f"{ctx.message.author}", icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
                msg = await bot.say(embed=embed)
                await bot.delete_message(ctx.message)
                return await save_players()
            else:
                await bot.say("You can't have negative elo")


@bot.command(pass_context = True)
async def setelo(ctx , user: discord.Member , elo):
    elo = int(elo)
    if not await is_allowed(ctx.message.author , high_perms):
        return
    if elo < 0:
        await bot.say("Can't set negative elo!")
    await save_players()
    for y in player_list:
        if y.id == user.id:



            cool = ctx.message.author.avatar_url.split('/avatars/')
            try:
                final = cool[1].split('.jpg')
                final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
            except:
                final_av = ctx.message.author.default_avatar_url


            embed = discord.Embed(description = f"**Set {user.name}'s elo to {elo}**" ,color = 0xfe4040)
            embed.set_footer(text = f'{ctx.message.author.name}' ,icon_url = final_av)
            #embed.set_footer(text=f"{ctx.message.author}", icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
            msg = await bot.say(embed=embed)
            await bot.delete_message(ctx.message)
            y.set_elo(elo)
            return await save_players()


@bot.command(pass_context = True)
async def addwin(ctx , user: discord.Member = None):
    if not await is_allowed(ctx.message.author , average_perms):
        return
    if not user:
        user = ctx.message.author
    await save_players()
    for y in player_list:
        if y.id == user.id:
            y.add_win(1)
            cool = ctx.message.author.avatar_url.split('/avatars/')
            try:
                final = cool[1].split('.jpg')
                final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
            except:
                final_av = ctx.message.author.default_avatar_url


            embed = discord.Embed(description = f"**Added 1 win to {user.name}**" ,color = 0xfe4040)
            embed.set_footer(text = f'{ctx.message.author.name}' ,icon_url = final_av)
            #embed.set_footer(text=f"{ctx.message.author}", icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
            msg = await bot.say(embed=embed)
            await bot.delete_message(ctx.message)
            return await save_players()

@bot.command(pass_context = True)
async def removewin(ctx , user: discord.Member = None):
    if not await is_allowed(ctx.message.author , average_perms):
        return
    if not user:
        user = ctx.message.author
    await save_players()
    for y in player_list:
        if y.id == user.id:
            if y.wins > 0:
                y.add_win(-1)
                cool = ctx.message.author.avatar_url.split('/avatars/')
                try:
                    final = cool[1].split('.jpg')
                    final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
                except:
                    final_av = ctx.message.author.default_avatar_url


                embed = discord.Embed(description = f"**Removed 1 win from {user.name}**" ,color = 0xfe4040)
                embed.set_footer(text = f'{ctx.message.author.name}' ,icon_url = final_av)
                #embed.set_footer(text=f"{ctx.message.author}", icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
                msg = await bot.say(embed=embed)
                await bot.delete_message(ctx.message)
                return await save_players()
            else:
                await bot.say(f"{user.name} has 0 wins!")

@bot.command(pass_context = True,aliases=['addloss'])
async def addlose(ctx , user: discord.Member = None):
    if not await is_allowed(ctx.message.author , average_perms):
        return
    if not user:
        user = ctx.message.author
    await save_players()
    for y in player_list:
        if y.id == user.id:
            y.add_lose(1)

            cool = ctx.message.author.avatar_url.split('/avatars/')
            try:
                final = cool[1].split('.jpg')
                final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
            except:
                final_av = ctx.message.author.default_avatar_url

            embed = discord.Embed(description = f"**Added 1 lose to {user.name}**" ,color = 0xfe4040)
            embed.set_footer(text = f'{ctx.message.author.name}' ,icon_url = final_av)
            #embed.set_footer(text=f"{ctx.message.author}", icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
            msg = await bot.say(embed=embed)
            await bot.delete_message(ctx.message)
            return await save_players()

@bot.command(pass_context = True, aliases=['removeloss'])
async def removelose(ctx , user: discord.Member = None):
    if not await is_allowed(ctx.message.author , average_perms):
        return
    if not user:
        user = ctx.message.author
    await save_players()
    for y in player_list:
        if y.id == user.id:
            if y.loses > 0:
                y.add_lose(-1)
                cool = ctx.message.author.avatar_url.split('/avatars/')
                try:
                    final = cool[1].split('.jpg')
                    final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
                except:
                    final_av = ctx.message.author.default_avatar_url
                embed = discord.Embed(description = f"**Removed 1 lose from {user.name}**" ,color = 0xfe4040)
                embed.set_footer(text = f'{ctx.message.author.name}' ,icon_url = final_av)
                #embed.set_footer(text=f"{ctx.message.author}", icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
                msg = await bot.say(embed=embed)
                await bot.delete_message(ctx.message)
                return await save_players()
            else:
                await bot.say(f"{user.name} has 0 loses!")



@bot.command(pass_context=True, aliases=['changepass'])
async def changepassword(ctx):


    print('?') 
    await bot.delete_message(ctx.message)
    if not await is_allowed(ctx.message.author , average_perms):
        return

    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == "725499864854560818":
        match_channel_number = 1
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        match_channel_number = 2
    if ctx.message.channel.name == "hosting-server3":
        match_channel_number = 3
    if ctx.message.channel.name == "hosting-server4":
        match_channel_number = 4


    server_num = match_channel_number 



 
    final = [ctx.message.author]

    await change_password(int(server_num), final)



@bot.command(pass_context=True)
async def penis(ctx , member:discord.User = None):
    member = ctx.message.author if not member else member
    if member.bot:
        return
    random_number = random.randint(1,27)
    penis = "8"
    for i in range(random_number):
        penis += "="
        if i == random_number - 1:
            penis += "D"
    embed = discord.Embed(title="Penis size machine", description=f"{member.name}'s penis: \n{penis}", color=0xc6c600, timestamp=datetime.datetime.utcnow())
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def penisbattle(ctx , member:discord.User):
    if member.name == ctx.message.author.name:
        embed = discord.Embed(title="You can't battle yourself you idiot ? :face_palm:", color=0xc6c600, timestamp=datetime.datetime.utcnow())
        await bot.say(embed=embed)
        return
    if member.bot:
        embed = discord.Embed(title="You can't battle a robot you idiot ? :face_palm:", color=0xc6c600, timestamp=datetime.datetime.utcnow())
        await bot.say(embed=embed)
        return
    random_number = random.randint(1,27)
    penis = "8"
    for i in range(random_number):
        penis += "="
        if i == random_number - 1:
            penis += "D"

    random_number2 = random.randint(1,27)
    penis2 = "8"
    for i in range(random_number2):
        penis2 += "="
        if i == random_number2 - 1:
            penis2 += "D"
    winner = ""
    if(penis > penis2):
        winner = member.name
        embed = discord.Embed(title="Penis battle machine", description=f"{ctx.message.author.name}'s penis: \n{penis}\n\n{member.name}'s penis: \n{penis2} \n \n {winner} won!" ,color=0xc6c600, timestamp=datetime.datetime.utcnow())
    if(penis < penis2):
        winner = ctx.message.author.name
        embed = discord.Embed(title="Penis battle machine", description=f"{ctx.message.author.name}'s penis: \n{penis}\n\n{member.name}'s penis: \n{penis2} \n \n {winner} won!" ,color=0xc6c600, timestamp=datetime.datetime.utcnow())
    if(penis == penis2):
        embed = discord.Embed(title="Penis battle machine", description=f"{ctx.message.author.name}'s penis: \n{penis}\n\n{member.name}'s penis: \n{penis2} \n \n Tie!" ,color=0xc6c600, timestamp=datetime.datetime.utcnow())
    await bot.say(embed=embed)

@bot.command(pass_context = True)
async def test(ctx):
    team1_role_lst = ["724754010573111296",  "729363219151454279", "724754010573111296", "724754010573111296"]
    team2_role_lst = ["724754011164639412",  "729363380170784789", "724754011164639412", "724754011164639412"]

    team1_role = discord.utils.get(ctx.message.server.roles, id = team1_role_lst[2 - 1])
    team2_role = discord.utils.get(ctx.message.server.roles, id = team2_role_lst[2 - 1])
    await removeroles(team1_role, team2_role)



async def purge(ctx, number : int):
    number += 1

    if number <= 100 and number >= 2:
        mgs = [] #Empty list to put all the messages in the log
        number = int(number) #Converting the amount of messages to delete to an integer
        async for x in bot.logs_from(ctx.message.channel, limit = number):
           # mgs.append(x)
           try:
                bot.delte_message(x)
           except:
                print('ello mate')
     #   if len(mgs) >= 2 and len(mgs) <= 100:
        #    await bot.delete_messages(mgs)
      #  if len(mgs) == 1:
       #     try:
         #       await bot.delete_message(msgs[0])
         #   except:
          #      print(':9')


@bot.command(pass_context = True)
async def changemap(ctx, arg1=''):
    await bot.delete_message(ctx.message)
    if not await is_allowed(ctx.message.author , average_perms):
        return


   # if arg1 == '':
   #     await bot.say('Please specify a map.')
    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == '725499864854560818':
        canal1 = discord.utils.get(ctx.message.server.channels, id="725499864854560818")
        canal2 = discord.utils.get(ctx.message.server.channels, id="709107214564196393")
        queue = discord.utils.get(ctx.message.server.channels, id="709107209581232309")
        match_channel_number = 1
        is_2v2 = True
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        canal1 = discord.utils.get(ctx.message.server.channels, id="729146306387509269")
        canal2 = discord.utils.get(ctx.message.server.channels, id="729146324531937391")
        queue = discord.utils.get(ctx.message.server.channels, id="729146344773648444")
        match_channel_number = 2
        is_2v2 = False
    if ctx.message.channel.name == "hosting-server3":
        match_channel_number = 3
    if ctx.message.channel.name == "hosting-server4":
        match_channel_number = 4


    server_num = (match_channel_number)

    if not arg1 in maplist:
        return await bot.say(f'Invalid map. Valid maps are: \n{maplist}', delete_after=4.0)

    final = [ctx.message.author]

    await change_map(arg1, int(server_num))
    print(server_num)

def sort_function(e):
    return e.elo

@bot.command(pass_context = True)
async def host(ctx):
    await bot.delete_message(ctx.message)


    if not await is_allowed(ctx.message.author , average_perms):
        return
    match_channel_number = 0

    canal1 = None
    canal2 = None
    queue = None
    is_2v2 = True

    cool = ctx.message.author.avatar_url.split('/avatars/')
    try:
        final = cool[1].split('.jpg')
        final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
    except:
        final_av = ctx.message.author.default_avatar_url

    team1_role_lst = ["724754010573111296",  "729363219151454279", "724754010573111296", "724754010573111296"]
    team2_role_lst = ["724754011164639412",  "729363380170784789", "724754011164639412", "724754011164639412"]



    
    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == '725499864854560818':
        canal1 = discord.utils.get(ctx.message.server.channels, id="725499864854560818")
        canal2 = discord.utils.get(ctx.message.server.channels, id="709107214564196393")
        queue = discord.utils.get(ctx.message.server.channels, id="709107209581232309")
        match_channel_number = 1
        is_2v2 = True
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        canal1 = discord.utils.get(ctx.message.server.channels, id="729146306387509269")
        canal2 = discord.utils.get(ctx.message.server.channels, id="729146324531937391")
        queue = discord.utils.get(ctx.message.server.channels, id="729146344773648444")
        match_channel_number = 2
        is_2v2 = True
    if ctx.message.channel.name == "hosting-server3":
        canal1 = discord.utils.get(ctx.message.server.channels, id="709107227356823605")
        canal2 = discord.utils.get(ctx.message.server.channels, id="709107229558833267")
        queue = discord.utils.get(ctx.message.server.channels, id="709107224877727885")
        match_channel_number = 3
        is_2v2 = True
    if ctx.message.channel.name == "hosting-server4":
        canal1 = discord.utils.get(ctx.message.server.channels, id="709107233983561768")
        canal2 = discord.utils.get(ctx.message.server.channels, id="709107236512858276")
        queue = discord.utils.get(ctx.message.server.channels, id="709107231718899821")
        match_channel_number = 4
        is_2v2 = True

        


    if(match_channel_number != 1 and match_channel_number != 2 and match_channel_number != 3 and match_channel_number != 4 and match_channel_number != 5 and match_channel_number != 6):
        return await bot.say("You can't host in this channel!")

    for i in running_games_list:
        if i.match_channel_number == match_channel_number and not i.game_has_ended:
            return await bot.say("There's a game being played in here please host in the other channel!", delete_after=3.0)
    c = 0
    for i in running_games_list:
        if not i.game_has_ended and not i.game_join_stage_ended:
            c += 1


    for i in running_games_list:
        if (ctx.message.author in i.waiting_players or ctx.message.author in i.team1 or ctx.message.author in i.team2) and not i.game_has_ended:
            return await bot.say("You're already in a game")


    # for i in running_games_list:
    #     if ctx.message.author == i.hoster and not i.game_has_ended:
    #         return await bot.say("You can't be the hoster of 2 games at the same time.Please ask another hoster to do !host")
    team1 = []
    team2 = []

    team1_role = discord.utils.get(ctx.message.server.roles, id = team1_role_lst[match_channel_number - 1])
    team2_role = discord.utils.get(ctx.message.server.roles, id = team2_role_lst[match_channel_number - 1])

    waitingplayers = []
    place = len(running_games_list)
    newgame = Game(team1 , team2 , ctx.message.author, waitingplayers)
    running_games_list.append(newgame)




    if match_channel_number == 2:
        newgame.lby = True







    if newgame.lby == True:
        newgame.maps = ['de_train',
                        'de_inferno',
                        'de_shortdust',
                        'gd_rialto',
                        'de_overpass',
                        'de_nuke',
                        'de_lake',
                        'de_cbble']

    game = running_games_list[place]
    game.msg_channel = ctx.message.channel.id
    #game.match_channel_number = c + 1
    msgevery = await bot.say("@here")
    #msgevery = await bot.say("no tag")
    await bot.delete_message(msgevery)
    game.match_channel_number = match_channel_number
    game.is_2v2 = is_2v2
    game.game_id = len(ended_games_list) + place + 1
    embed = discord.Embed(title = 'Players in lobby', description = f"**Game #{game.game_id} has begun! Type {pref}join** {ctx.message.author.mention}\n```css\n[Waiting for players to join!]```", color = 0xfe4040, timestamp=datetime.datetime.utcnow())
    embed.set_footer(text = f'Hosted by {ctx.message.author.name}',  icon_url = final_av)
    
    embed1 = discord.Embed(title = f'', color = discord.Color.dark_grey())
    embed1.add_field(name=f"Multiplier", value=f"{game.elox}", inline=True)
    embed1.add_field(name=f"Team1 Bet", value=f"100", inline=True)
    embed1.add_field(name=f"Team2 Bet", value=f"100", inline=True)
  #  embed1.add_field(name=f"Team 2", value=f"```ini\n{teamB}```", inline=False)

    embed_edit = await bot.say(embed=embed)
    #embed_edit1 = await bot.say(embed=embed1)

    game.embed_msg = embed_edit
  #  game.stats_msg = embed_edit1 
    run_for_10s = 0
    number_of_players = 4
    if(not game.is_2v2):
        number_of_players = 10

    while(len(game.waiting_players) < number_of_players):
        if(game.game_has_been_canceled == True):

            return 
        waiting_players = ""



        for i in range(len(game.waiting_players)):
            player = await find_player(game.waiting_players[i].id)
            waiting_players += str(i + 1) + ": " + game.waiting_players[i].name + " [" + str(player.elo) + " Elo]" + "\n"


        for i in range(len(game.waiting_players)  , number_of_players):
            waiting_players += str(i + 1) + ": " +"\n"
    #    print(f"Waiting for {10 - len(game.waiting_players)} more players")
        if(len(game.waiting_players) >= 0):
            embed2 = discord.Embed(title = '5v5' if number_of_players == 10 else '2v2', description = f"**Game [{game.game_id}] has started! Type {pref}join**\n```css\n{waiting_players}```", color = discord.Color.dark_orange(),stamp=datetime.datetime.utcnow())
            embed2.set_footer(text = f'Host: {ctx.message.author.name}', icon_url=final_av)
            try:
                if game.update_this_tick:
                    await bot.edit_message(embed_edit , embed=embed2)
            except:
                pass
        game.update_this_tick = False
        if run_for_10s >= 10:
            game.game_join_stage_ended = True
            break
        await asyncio.sleep(0.5)
        if len(game.waiting_players) >= number_of_players:
            run_for_10s += 0.5
    game.update_this_tick = True
    game.game_join_stage_ended = True
    elo_waiting_players = []
    for pl in game.waiting_players:
        person = await get_player_member(pl.id)
        if not person.blackcapt:
            elo_waiting_players.append(person)
    if len(elo_waiting_players) < 2:
        elo_waiting_players = []
        for pl in game.waiting_players:
            person = await get_player_member(pl.id)
            elo_waiting_players.append(person)
    elo_waiting_players.sort(key=sort_function)
    capt1_int = random.randint(0,len(elo_waiting_players) - 1)
    capt1 = elo_waiting_players[capt1_int]
    for i in game.waiting_players:
        if i.id == capt1.id:
            capt1 = i
    game.waiting_players.remove(capt1)


    #await bot.say(f"{capt1.name} has been choosen as captain for team A")
    adder = 0
    if capt1_int == len(elo_waiting_players) - 1:
        adder = -1
    else:
        adder = 1
    capt2 = elo_waiting_players[capt1_int + adder]
    for i in game.waiting_players:
        if i.id == capt2.id:
            capt2 = i
    game.waiting_players.remove(capt2)
    #await bot.say(f"{capt2.name} has been choosen as captain for team B")

    game.team1.append(capt1)
    game.team2.append(capt2)
    game.captain_team1 = capt1
    game.captain_team2 = capt2
    game.turn = game.captain_team1
    #game_counter += 1
    #await bot.say(f"Pick players with 5v5 pick @TAG")
    turn = game.turn
    #await bot.say(f"Now it's {turn.name}'s turn!")
    num = 2

    while(True):
        if(game.game_has_been_canceled == True):
            game.game_has_ended = True
            #await bot.delete_message(msgevery)
          #  await bot.delete_message(embed_edit)
            return# await bot.delete_message(embed32_edit)

        waiting_players = ""
        teamA = ""
        teamB = ""

        for i in range(len(game.waiting_players)):
            if game.waiting_players[i] == -1:
                continue
            if not i == len(game.waiting_players) - 1:
                waiting_players += str(i + 1) + ": " + game.waiting_players[i].name + '\n'
            else:
                waiting_players += str(i + 1) + ": " + game.waiting_players[i].name +'\nGood luck on 64 Tick!'
        if is_2v2:
            num = 2
        else:
            num = 5

        for i in range(num):
            if i <= len(game.team1) - 1:
                # if not i == len(game.team1) - 1:

                #teamA += '[' + str(i + 1) + ": " + game.team1[i].name  + ']' + "\n"
                try:
                    remainder = 15 - len(game.team1[i].name[0:8])
                except:
                    remainder = 0
                teamA += '[' + str(i + 1) + ": " + game.team1[i].name[0:8]  + ''.join(' ' for i in range(5+ remainder))+ ']'  + "\n"
                # else:
                    #  teamA += '[' + str(i + 1) + ". " + game.team1[i].name + ']'
            else:
                try:
                    remainder = 15 - len(game.team1[i].name[0:8])
                except:
                    remainder = 15
                teamA += '[' + str(i + 1) + ": " + ''.join(' ' for i in range(5+ remainder)) + ']' + "\n"

        for i in range(num):

            if i <= len(game.team2) - 1:
                # if not i == len(game.team1) - 1:

                #teamA += '[' + str(i + 1) + ": " + game.team1[i].name  + ']' + "\n"
                try:
                    remainder = 15 - len(game.team2[i].name[0:8])
                except:
                    remainder = 0
                teamB += '[' + str(i + 1) + ": " + game.team2[i].name[0:8]  + ''.join(' ' for i in range(5+ remainder))+ ']'  + "\n"
                # else:
                    #  teamA += '[' + str(i + 1) + ". " + game.team1[i].name + ']'
            else:
                try:
                    remainder = 15 - len(game.team2[i].name[0:8])
                except:
                    remainder = 15
                teamB += '[' + str(i + 1) + ": " + ''.join(' ' for i in range(5+ remainder)) + ']' + "\n"

        #print(f"Waiting for {10 - len(game.waiting_players)} more players")
        game_maps = ""
        maps_counter = 1
        for i in range(len(game.maps)):
            if game.maps[i] != -1:
                game_maps += f"{i + 1}: {game.maps[i]}" + "\n"
        game_maps += 'Type the number next to the map!'
        embed2 = discord.Embed(title = '5v5' if number_of_players == 10 else '2v2' , color = discord.Color.dark_orange(), timestamp=datetime.datetime.utcnow())
        if len(waiting_players) != 0:
            embed2.add_field(name="Remaning Pick Pool", value=f"```yaml\n{waiting_players}```", inline=True)
        if game.veto_stage:
            embed2.add_field(name="Remaining Map Pool", value = f"```yaml\n{game_maps}```" , inline=True)
        embed2.add_field(name="Game Info", value=f"Host: ***{ctx.message.author.name}***\nTeam 1 Captain: ***{game.captain_team1.name}***\nTeam 2 Captain: ***{game.captain_team2.name}***\nMap: ***TBD***\nTurn: {game.turn.mention}", inline=True)
        embed2.add_field(name=f"Team 1", value=f"```css\n{teamA}```", inline=False)
        embed2.add_field(name=f"Team 2", value=f"```ini\n{teamB}```", inline=False)
        embed2.set_footer(text = f'Host: {ctx.message.author.name}', icon_url=final_av)

        if game.update_this_tick:
            await bot.edit_message(embed_edit , embed=embed2)
        game.update_this_tick = False
        await asyncio.sleep(1)
        if game.game_has_started == True:
            await bot.edit_message(embed_edit , embed=embed2)
            break
    game.waiting_players = []
    #await startgameimage(game , ctx)

    #serverip = discord.Embed(description=f"```\n{msg_ip}```" ,color = 0xfe4040)
    #serverip.set_footer(text = f'GalaxyHVH TEAM', icon_url = "https://cdn.discordapp.com/attachments/709710979596025856/709743930689716304/aaaaa.png")
    #serverip.set_author(name="Server IP:", icon_url = "https://cdn.discordapp.com/attachments/709710979596025856/709743930689716304/aaaaa.png")
    #serverip.add_field(name="**Direct connect:**", value=f"[steam://connect/{msg_ipp}:27015;/{msg_pass}](steam://connect/{msg_ipp}:27015;/{msg_pass})", inline=False)
    #serverip.set_thumbnail(url="https://cdn.discordapp.com/attachments/709710979596025856/709743930689716304/aaaaa.png")

    teamB = ''
    for i in range(num):
        try:
            print(game.team2[i].name)
        except:
            print(num)
        if i <= len(game.team2) - 1:
            # if not i == len(game.team1) - 1:

            #teamA += '[' + str(i + 1) + ": " + game.team1[i].name  + ']' + "\n"
            try:
                remainder = 15 - len(game.team2[i].name[0:8])
            except:
                remainder = 0
            teamB += '[' + str(i + 1) + ": " + game.team2[i].name[0:8]  + ''.join(' ' for i in range(5+ remainder))+ ']'  + "\n"
            # else:
                #  teamA += '[' + str(i + 1) + ". " + game.team1[i].name + ']'
        else:
            try:
                remainder = 15 - len(game.team2[i].name[0:8])
            except:
                remainder = 15
            teamB += '[' + str(i + 1) + ": " + ''.join(' ' for i in range(5+ remainder)) + ']' + "\n"

    for i in range(len(game.maps)):
        if game.maps[i] != -1:
            final_map = game.maps[i]
            print(str(final_map))

    await asyncio.sleep(1)
    embed3 = discord.Embed(title = '5v5' if number_of_players == 10 else '2v2' , color = discord.Color.dark_orange(), timestamp=datetime.datetime.utcnow())
    embed3.add_field(name="Remaining Map Pool", value = f"```yaml\nGood luck on 64 tick!```" , inline=True)
    embed3.add_field(name="Game Info", value=f"Host: ***{ctx.message.author.name}***\nTeam 1 Captain: ***{game.captain_team1.name}***\nTeam 2 Captain: ***{game.captain_team2.name}***\nMap: ***{final_map}***", inline=True)
    embed3.add_field(name=f"Team 1", value=f"```css\n{teamA}```", inline=False)
    embed3.add_field(name=f"Team 2", value=f"```ini\n{teamB}```", inline=False)
    embed3.set_footer(text = f'Host: {ctx.message.author.name}', icon_url=final_av)


    await bot.edit_message(embed_edit, embed=embed3)
    

    await change_password(game.match_channel_number, game.team1, game.team2)
    await change_map(final_map, game.match_channel_number)

    str3 = ''
    for x in game.team1:
        str3 += f'{x.mention}  '
        try:
            game.playing_players.append(x)
            
            await bot.add_roles(x,team1_role)
            #await bot.send_message(x ,embed=serverip)
            await bot.move_member(x, canal1)

        except:
            continue
    await asyncio.sleep(0.5)

    for y in game.team2:
        str3 += f'{y.mention}  '
        try:
            game.playing_players.append(y)
            
            await bot.add_roles(y,team2_role)
            #await bot.send_message(y ,embed=serverip)
            await bot.move_member(y, canal2)

        except:
            continue





    #await change_password(match_channel_number - 1, game.team1, game.team2)

    while(True):
        #await bot.delete_message(embed_edit)
        #await bot.delete_message(embed32_edit)
        if(game.game_has_been_canceled == True):
            game.game_has_ended = True
        #    await bot.delete_message(msgevery)
            return

        if game.game_has_ended == True:
            return
        await asyncio.sleep(1)










@bot.command(pass_context = True, aliases=['2v2'])
async def twovtwo(ctx, user: discord.Member, user1: discord.Member, user2: discord.Member, user3: discord.Member,):
    await bot.delete_message(ctx.message)
    if not await is_allowed(ctx.message.author , average_perms):
        return
    match_channel_number = 0

    canal1 = None
    canal2 = None
    queue = None
    is_2v2 = True
    cool = ctx.message.author.avatar_url.split('/avatars/')
    try:
        final = cool[1].split('.jpg')
        final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
    except:
        final_av = ctx.message.author.default_avatar_url
    team1_role_lst = ["724754010573111296",  "729363219151454279", "724754010573111296", "724754010573111296"]
    team2_role_lst = ["724754011164639412",  "729363380170784789", "724754011164639412", "724754011164639412"]
    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == '725499864854560818':
        canal1 = discord.utils.get(ctx.message.server.channels, id="709107212622102580")
        canal2 = discord.utils.get(ctx.message.server.channels, id="709107214564196393")
        queue = discord.utils.get(ctx.message.server.channels, id="709107209581232309")
        match_channel_number = 1
        is_2v2 = True
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        canal1 = discord.utils.get(ctx.message.server.channels, id="729146306387509269")
        canal2 = discord.utils.get(ctx.message.server.channels, id="729146324531937391")
        queue = discord.utils.get(ctx.message.server.channels, id="729146344773648444")
        match_channel_number = 2
        is_2v2 = True
    if ctx.message.channel.name == "hosting-server3":
        canal1 = discord.utils.get(ctx.message.server.channels, id="709107227356823605")
        canal2 = discord.utils.get(ctx.message.server.channels, id="709107229558833267")
        queue = discord.utils.get(ctx.message.server.channels, id="709107224877727885")
        match_channel_number = 3
        is_2v2 = True
    if ctx.message.channel.name == "hosting-server4":
        canal1 = discord.utils.get(ctx.message.server.channels, id="709107233983561768")
        canal2 = discord.utils.get(ctx.message.server.channels, id="709107236512858276")
        queue = discord.utils.get(ctx.message.server.channels, id="709107231718899821")
        match_channel_number = 4
        is_2v2 = True




    if(match_channel_number != 1 and match_channel_number != 2 and match_channel_number != 3 and match_channel_number != 4 and match_channel_number != 5 and match_channel_number != 6):
        return await bot.say("You can't force a 2v2 in this channel!")

    for i in running_games_list:
        if i.match_channel_number == match_channel_number and not i.game_has_ended:
            return await bot.say("There's a game being played in here please host in the other channel!", delete_after=3.0)
    c = 0
    for i in running_games_list:
        if not i.game_has_ended and not i.game_join_stage_ended:
            c += 1


    for i in running_games_list:
        if (ctx.message.author in i.waiting_players or ctx.message.author in i.team1 or ctx.message.author in i.team2) and not i.game_has_ended:
            return await bot.say("You're already in a game")


    # for i in running_games_list:
    #     if ctx.message.author == i.hoster and not i.game_has_ended:
    #         return await bot.say("You can't be the hoster of 2 games at the same time.Please ask another hoster to do !host")
    team1 = []
    team2 = []

    team1_role = discord.utils.get(ctx.message.server.roles, id = team1_role_lst[match_channel_number - 1])
    team2_role = discord.utils.get(ctx.message.server.roles, id = team2_role_lst[match_channel_number - 1])

    waitingplayers = []
    place = len(running_games_list)
    running_games_list.append(Game(team1 , team2 , ctx.message.author, waitingplayers))

    game = running_games_list[place]
    game.msg_channel = ctx.message.channel.id
    embed = discord.Embed(title = 'Generating 2v2', description = f"**Game #{game.game_id} has begun! Game forced by {ctx.message.author.mention}```", color = 0xfe4040, timestamp=datetime.datetime.utcnow())
    embed.set_footer(text = f'Host: {ctx.message.author.name}',  icon_url = final_av)
    embed_edit = await bot.say(embed=embed)
    game.embed_msg = embed_edit
    #game.match_channel_number = c + 1
    #msgevery = await bot.say("@here")
    #msgevery = await bot.say("no tag")
  #  await bot.delete_message(msgevery)
    game.match_channel_number = match_channel_number
    game.is_2v2 = is_2v2
    game.game_id = len(ended_games_list) + place + 1
    run_for_10s = 0
    number_of_players = 4


    game.waiting_players.append(user)
    game.waiting_players.append(user1)
    game.waiting_players.append(user2)
    game.waiting_players.append(user3)



    if(not game.is_2v2):
        number_of_players = 10

    while(len(game.waiting_players) < number_of_players):
        if(game.game_has_been_canceled == True):

            return# await bot.delete_message(embed_edit)
        waiting_players = ""



        for i in range(len(game.waiting_players)):
            player = await find_player(game.waiting_players[i].id)
            waiting_players += str(i + 1) + ": " + game.waiting_players[i].name + " [" + str(player.elo) + " Elo]" + "\n"


        for i in range(len(game.waiting_players)  , number_of_players):
            waiting_players += str(i + 1) + ": " +"\n"
    #    print(f"Waiting for {10 - len(game.waiting_players)} more players")
        if(len(game.waiting_players) >= 0):
            embed2 = discord.Embed(title = '5v5' if number_of_players == 10 else '2v2', description = f"**Game [{game.game_id}] has started! Type {pref}join**\n```css\n{waiting_players}```", color = discord.Color.dark_orange(),stamp=datetime.datetime.utcnow())
            embed2.set_footer(text = f'Host: {ctx.message.author.name}', icon_url=final_av)
            try:
                if game.update_this_tick:
                    await bot.edit_message(embed_edit , embed=embed2)
            except:
                pass
        game.update_this_tick = False
        if run_for_10s >= 10:
            game.game_join_stage_ended = True
            break
        await asyncio.sleep(0.5)
        if len(game.waiting_players) >= number_of_players:
            run_for_10s += 0.5
    game.update_this_tick = True
    game.game_join_stage_ended = True
    elo_waiting_players = []
    for pl in game.waiting_players:
        person = await get_player_member(pl.id)
        if not person.blackcapt:
            elo_waiting_players.append(person)
    if len(elo_waiting_players) < 2:
        elo_waiting_players = []
        for pl in game.waiting_players:
            person = await get_player_member(pl.id)
            elo_waiting_players.append(person)
    elo_waiting_players.sort(key=sort_function)
    capt1_int = random.randint(0,len(elo_waiting_players) - 1)
    capt1 = elo_waiting_players[capt1_int]
    for i in game.waiting_players:
        if i.id == capt1.id:
            capt1 = i


    

    #await bot.say(f"{capt1.name} has been choosen as captain for team A")
   # adder = 0
  #  if capt1_int == len(elo_waiting_players) - 1:
  #      adder = -1
  #  else:
  #      adder = 1
 #   capt2 = elo_waiting_players[capt1_int + adder]
 #   for i in game.waiting_players:
  #      if i.id == capt2.id:
     #       capt2 = i
    
    #await bot.say(f"{capt2.name} has been choosen as captain for team B")
    capt1 = game.waiting_players[0]
    capt2 =  game.waiting_players[2]

    game.team1.append(capt1)
    game.team2.append(capt2)
    
    game.captain_team1 = capt1
    game.captain_team2 = capt2

    game.waiting_players.remove(capt1)
    game.waiting_players.remove(capt2)
 #   game.team1.append(capt1)
  #  game.team2.append(capt2)
    game.captain_team1 = capt1
    game.captain_team2 = capt2
    game.turn = game.captain_team1
    #game_counter += 1
    #await bot.say(f"Pick players with 5v5 pick @TAG")
    turn = game.turn
    #await bot.say(f"Now it's {turn.name}'s turn!")
    num = 2

    while(True):
        if(game.game_has_been_canceled == True):
            game.game_has_ended = True
            #await bot.delete_message(msgevery)
          #  await bot.delete_message(embed_edit)
            return# await bot.delete_message(embed32_edit)

        waiting_players = ""
        teamA = ""
        teamB = ""

        for i in range(len(game.waiting_players)):
            if game.waiting_players[i] == -1:
                continue
            if not i == len(game.waiting_players) - 1:
                waiting_players += str(i + 1) + ": " + game.waiting_players[i].name + '\n'
            else:
                waiting_players += str(i + 1) + ": " + game.waiting_players[i].name +'\nGood luck on 64 Tick!'
        if is_2v2:
            num = 2
        else:
            num = 5

        for i in range(num):
            if i <= len(game.team1) - 1:
                # if not i == len(game.team1) - 1:

                #teamA += '[' + str(i + 1) + ": " + game.team1[i].name  + ']' + "\n"
                try:
                    remainder = 15 - len(game.team1[i].name[0:8])
                except:
                    remainder = 0
                teamA += '[' + str(i + 1) + ": " + game.team1[i].name[0:8]  + ''.join(' ' for i in range(5+ remainder))+ ']'  + "\n"
                # else:
                    #  teamA += '[' + str(i + 1) + ". " + game.team1[i].name + ']'
            else:
                try:
                    remainder = 15 - len(game.team1[i].name[0:8])
                except:
                    remainder = 15
                teamA += '[' + str(i + 1) + ": " + ''.join(' ' for i in range(5+ remainder)) + ']' + "\n"

        for i in range(num):

            if i <= len(game.team2) - 1:
                # if not i == len(game.team1) - 1:

                #teamA += '[' + str(i + 1) + ": " + game.team1[i].name  + ']' + "\n"
                try:
                    remainder = 15 - len(game.team2[i].name[0:8])
                except:
                    remainder = 0
                teamB += '[' + str(i + 1) + ": " + game.team2[i].name[0:8]  + ''.join(' ' for i in range(5+ remainder))+ ']'  + "\n"
                # else:
                    #  teamA += '[' + str(i + 1) + ". " + game.team1[i].name + ']'
            else:
                try:
                    remainder = 15 - len(game.team2[i].name[0:8])
                except:
                    remainder = 15
                teamB += '[' + str(i + 1) + ": " + ''.join(' ' for i in range(5+ remainder)) + ']' + "\n"

        #print(f"Waiting for {10 - len(game.waiting_players)} more players")
        game_maps = ""
        maps_counter = 1
        for i in range(len(game.maps)):
            if game.maps[i] != -1:
                game_maps += f"{i + 1}: {game.maps[i]}" + "\n"
        game_maps += 'Type the number next to the map!'
        embed2 = discord.Embed(title = '5v5' if number_of_players == 10 else '2v2' , color = discord.Color.dark_orange(), timestamp=datetime.datetime.utcnow())
        if len(waiting_players) != 0:
            embed2.add_field(name="Remaning Pick Pool", value=f"```yaml\n{waiting_players}```", inline=True)
        if game.veto_stage:
            embed2.add_field(name="Remaining Map Pool", value = f"```yaml\n{game_maps}```" , inline=True)
        embed2.add_field(name="Game Info", value=f"Host: ***{ctx.message.author.name}***\nTeam 1 Captain: ***{game.captain_team1.name}***\nTeam 2 Captain: ***{game.captain_team2.name}***\nMap: ***TBD***\nTurn: {game.turn.mention}", inline=True)
        embed2.add_field(name=f"Team 1", value=f"```css\n{teamA}```", inline=False)
        embed2.add_field(name=f"Team 2", value=f"```ini\n{teamB}```", inline=False)
        embed2.set_footer(text = f'Host: {ctx.message.author.name}', icon_url=final_av)

        if game.update_this_tick:
            await bot.edit_message(embed_edit , embed=embed2)
        game.update_this_tick = False
        await asyncio.sleep(1)
        if game.game_has_started == True:
            await bot.edit_message(embed_edit , embed=embed2)
            break
    game.waiting_players = []
    #await startgameimage(game , ctx)

    #serverip = discord.Embed(description=f"```\n{msg_ip}```" ,color = 0xfe4040)
    #serverip.set_footer(text = f'GalaxyHVH TEAM', icon_url = "https://cdn.discordapp.com/attachments/709710979596025856/709743930689716304/aaaaa.png")
    #serverip.set_author(name="Server IP:", icon_url = "https://cdn.discordapp.com/attachments/709710979596025856/709743930689716304/aaaaa.png")
    #serverip.add_field(name="**Direct connect:**", value=f"[steam://connect/{msg_ipp}:27015;/{msg_pass}](steam://connect/{msg_ipp}:27015;/{msg_pass})", inline=False)
    #serverip.set_thumbnail(url="https://cdn.discordapp.com/attachments/709710979596025856/709743930689716304/aaaaa.png")

    teamB = ''
    for i in range(num):
        try:
            print(game.team2[i].name)
        except:
            print(num)
        if i <= len(game.team2) - 1:
            # if not i == len(game.team1) - 1:

            #teamA += '[' + str(i + 1) + ": " + game.team1[i].name  + ']' + "\n"
            try:
                remainder = 15 - len(game.team2[i].name[0:8])
            except:
                remainder = 0
            teamB += '[' + str(i + 1) + ": " + game.team2[i].name[0:8]  + ''.join(' ' for i in range(5+ remainder))+ ']'  + "\n"
            # else:
                #  teamA += '[' + str(i + 1) + ". " + game.team1[i].name + ']'
        else:
            try:
                remainder = 15 - len(game.team2[i].name[0:8])
            except:
                remainder = 15
            teamB += '[' + str(i + 1) + ": " + ''.join(' ' for i in range(5+ remainder)) + ']' + "\n"

    for i in range(len(game.maps)):
        if game.maps[i] != -1:
            final_map = game.maps[i]
            print(str(final_map))

    await asyncio.sleep(1)
    embed3 = discord.Embed(title = '5v5' if number_of_players == 10 else '2v2' , color = discord.Color.dark_orange(), timestamp=datetime.datetime.utcnow())
    embed3.add_field(name="Remaining Map Pool", value = f"```yaml\nGood luck on 64 tick!```" , inline=True)
    embed3.add_field(name="Game Info", value=f"Host: ***{ctx.message.author.name}***\nTeam 1 Captain: ***{game.captain_team1.name}***\nTeam 2 Captain: ***{game.captain_team2.name}***\nMap: ***{final_map}***", inline=True)
    embed3.add_field(name=f"Team 1", value=f"```css\n{teamA}```", inline=False)
    embed3.add_field(name=f"Team 2", value=f"```ini\n{teamB}```", inline=False)
    embed3.set_footer(text = f'Host: {ctx.message.author.name}')


    await bot.edit_message(embed_edit, embed=embed3)
    

    await change_password(0, game.team1, game.team2)
    await change_map(final_map)

    str3 = ''
    for x in game.team1:
        str3 += f'{x.mention}  '
        try:
            game.playing_players.append(x)
            
            await bot.add_roles(x,team1_role)
            #await bot.send_message(x ,embed=serverip)
            await bot.move_member(x, canal1)

        except:
            continue
    await asyncio.sleep(0.5)

    for y in game.team2:
        str3 += f'{y.mention}  '
        try:
            game.playing_players.append(y)
            
            await bot.add_roles(y,team2_role)
            #await bot.send_message(y ,embed=serverip)
            await bot.move_member(y, canal2)

        except:
            continue


   # await bot.say(str3+ f'\nThe 2v2 Game has been started. Please join your respective team VCs.')


    #await change_password(match_channel_number - 1, game.team1, game.team2)

    while(True):
        #await bot.delete_message(embed_edit)
        #await bot.delete_message(embed32_edit)
        if(game.game_has_been_canceled == True):
            game.game_has_ended = True
        #    await bot.delete_message(msgevery)
            return

        if game.game_has_ended == True:
            return
        await asyncio.sleep(1)
























async def remove_cooldown(name):
    await asyncio.sleep(5)
    cooldown.remove(name)

@bot.event
async def on_message(message):
    content = message.content
    ch = message.channel
    await bot.process_commands(message)
    if 'thank' in content.lower() or 'thanks' in content.lower():
        await bot.send_message(ch, "You're welcome :)")



    if(message.channel.name == "hosting-server1" or message.channel.name == "hosting-server2" or message.channel.name == "hosting-server3" or message.channel.name == "hosting-server4"  or message.channel.name == "hosting-server-oldhvh1" or message.channel.name == "hosting-5v5" or message.channel.id == "729821342215438408" or message.channel.id == '725499864854560818' and not message.author.bot ):
        if message.channel.name in cooldown and content == "!host":
            try:
                await bot.delete_message(message)
                return
            except:
                pass
        elif content == "!host":
            cooldown.append(message.channel.name)
            bot.loop.create_task(remove_cooldown(message.channel.name))

        try:
            t = int(content)
            if t > 0:
                for i in running_games_list:
                    if i.turn == message.author and not i.game_has_started and i.game_join_stage_ended and not i.game_has_ended and i.veto_stage:
                        if i.maps[int(content) - 1] == -1:
                            return await bot.delete_message(message)
                        i.maps[int(content) - 1] = -1
                        if i.turn == i.captain_team1:
                            i.turn = i.captain_team2
                            msg1 = await bot.send_message(message.channel, f"{i.captain_team2.mention}")
                            
                            await bot.delete_message(msg1)
                        else:
                            msg1 = await bot.send_message(message.channel, f"{i.captain_team1.mention}")
                            
                            await bot.delete_message(msg1)
                            i.turn = i.captain_team1
                        i.update_this_tick = True
                        good_maps = 0
                        for maps in i.maps:
                            if maps != -1:
                                good_maps += 1
                        if good_maps == 1:
                            i.game_has_started = True
                        return await bot.delete_message(message)


                for i in running_games_list:
                    if i.turn == message.author and not i.game_has_started and i.game_join_stage_ended and not i.game_has_ended and not i.veto_stage:
                        member = None
                        players_perteam = 2
                        print(str(i.picks))
                        if not i.is_2v2:
                            players_perteam = 5
                        try:
                             member = i.waiting_players[int(content) - 1]
                             if member == -1:
                                 try:
                                     await bot.delete_message(message)
                                     return 
                                 except:
                                     return
                        except:
                            try:
                                await bot.delete_message(message)
                                return  
                            except:
                                return
                        if i.waiting_players[int(content) - 1] == -1:
                            try:
                                return await bot.delete_message(message)
                            except:
                                return
                        if i.turn == i.captain_team1:
                            i.picks += 1
                            i.waiting_players[int(content) - 1] = -1
                            #i.waiting_players.remove(member)
                            i.team1.append(member)
                            if not i.is_2v2:
                                print(str(i.picks))
                                if i.picks in [3, 4, 6, 8, 10]:
                                    i.turn = i.captain_team1    
                                    msg1 = await bot.send_message(message.channel, f"{i.captain_team1.mention}")
                            
                                    await bot.delete_message(msg1)
                                if i.picks in [1, 2, 5, 7, 9]:
                                    msg1 = await bot.send_message(message.channel, f"{i.captain_team2.mention}")
                            
                                    await bot.delete_message(msg1)
                                    i.turn = i.captain_team2
                            else:
                                i.turn = i.captain_team2



                            i.update_this_tick = True
                            try:
                                await bot.delete_message(message)
                                return 
                            except:
                                return

                        if i.turn == i.captain_team2:
                            i.picks += 1
                            i.waiting_players[int(content) - 1] = -1
                            #i.waiting_players.remove(member)
                            i.team2.append(member)
                            if not i.is_2v2:
                                print(str(i.picks))
                                if i.picks in [3, 4, 6, 8, 10]:
                                    msg1 = await bot.send_message(message.channel, f"{i.captain_team1.mention}")
                            
                                    await bot.delete_message(msg1)
                                    i.turn = i.captain_team1
                                if i.picks in [1, 2, 5, 7, 9]:
                                    msg1 = await bot.send_message(message.channel, f"{i.captain_team2.mention}")
                            
                                    await bot.delete_message(msg1)
                                    i.turn = i.captain_team2


                            else:
                                i.turn = i.captain_team1


                            i.update_this_tick = True


                        if len(i.team1) == len(i.team2) == players_perteam:
                            i.veto_stage = True
                            #i.game_has_started = True
                            i.update_this_tick = True
                            i.waiting_players = []
                            return await bot.say(f"The game #{i.game_id} has started!", delete_after=4.0)

        except:
            pass

        if not message.author.bot:
            try:
                await bot.delete_message(message)
            except:
                pass


@bot.command(pass_context = True)
async def redraft(ctx):
    if not await is_allowed(ctx.message.author , average_perms):
            return
    for i in running_games_list:
        if not i.game_has_ended and i.game_join_stage_ended and not i.game_has_started:
            if i.msg_channel == ctx.message.channel.id:
                for x in i.waiting_players:
                    if x == -1:
                        i.waiting_players.remove(x)

                for x in i.team1:
                    i.waiting_players.append(x)

                for x in i.team2:
                    i.waiting_players.append(x)

                i.team1 = []
                i.team2 = []
                oldcapt1 = i.captain_team1
                oldcapt2 = i.captain_team2
                capt1 = i.captain_team1
                capt2 = i.captain_team2
                waiting = []

                while( (capt1 == oldcapt1 or capt1 == oldcapt2) and (capt2 == oldcapt2 or capt2 == oldcapt1) ):
                    waiting = []
                    for t in i.waiting_players:
                        waiting.append(t)
                    capt1 = random.choice(waiting)
                    waiting.remove(capt1)
                    capt2 = random.choice(waiting)
                    waiting.remove(capt2)

                capt1_index = 0
                capt2_index = 0
                i.waiting_players.remove(capt1)
                i.waiting_players.remove(capt2)

                i.team1.append(capt1)
                i.team2.append(capt2)
                i.captain_team1 = capt1
                i.captain_team2 = capt2




                i.update_this_tick = True
                i.turn = i.captain_team1
                i.veto_stage = False
                i.picks = 0

                sv = bot.get_server("724753968508698674")
                bot_commands_chan = discord.utils.get(sv.channels, name="5v5-logs")
                team1_role_lst = ["724754010573111296",  "729363219151454279", "724754010573111296", "724754010573111296"]
                team2_role_lst = ["724754011164639412",  "729363380170784789", "724754011164639412", "724754011164639412"]

                match_channel_number = 0

                canal1 = None
                canal2 = None
                queue = None
                is_2v2 = True

                if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == '725499864854560818':
                    canal1 = discord.utils.get(ctx.message.server.channels, id="696477335742054483")
                    canal2 = discord.utils.get(ctx.message.server.channels, id="696477335742054482")
                    queue = discord.utils.get(ctx.message.server.channels, id="696477335742054481")

                    match_channel_number = 1
                    is_2v2 = False
                elif ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
                    canal1 = discord.utils.get(ctx.message.server.channels, id="696477335742054487")
                    canal2 = discord.utils.get(ctx.message.server.channels, id="696477335742054488")
                    queue = discord.utils.get(ctx.message.server.channels, id="696477335742054486")
                    match_channel_number = 2
                    is_2v2 = False
                elif ctx.message.channel.name == "hosting-server3":
                    canal1 = discord.utils.get(ctx.message.server.channels, id="696478430505730059")
                    canal2 = discord.utils.get(ctx.message.server.channels, id="696478489473318914")
                    queue = discord.utils.get(ctx.message.server.channels, id="701856677846057000")
                    match_channel_number = 3
                    is_2v2 = True
                elif ctx.message.channel.name == "hosting-server4":
                    canal1 = discord.utils.get(ctx.message.server.channels, id="696479503349842000")
                    canal2 = discord.utils.get(ctx.message.server.channels, id="696479557628329995")
                    queue = discord.utils.get(ctx.message.server.channels, id="696479375289352242")
                    match_channel_number = 4
                    is_2v2 = False
                else:
                    return await send_error('wrong_chan', ctx)
                    await bot.send_message(bot_commands_chan, f'Game #{i.game_id} has been redrafted; request from {ctx.message.author.mention}')
                team1_role = discord.utils.get(ctx.message.server.roles, id = team1_role_lst[match_channel_number - 1])
                team2_role = discord.utils.get(ctx.message.server.roles, id = team2_role_lst[match_channel_number - 1])

                await removeroles(team1_role, team2_role)


@bot.command(pass_context = True)
async def drop(ctx):
    for i in running_games_list:
        if ctx.message.author in i.waiting_players and not i.game_join_stage_ended and not i.game_has_started:
            i.waiting_players.remove(ctx.message.author)
            await bot.delete_message(ctx.message)
            i.update_this_tick = True

@bot.command(pass_context = True)
async def forcedrop(ctx , number):
    if not await is_allowed(ctx.message.author , average_perms):
        return
    try:
        number = int(number)
    except:
        await bot.say("The syntax is: !forcedrop PLAYER_NUMBER. Like !forcedrop 1")
    match_channel_number = 0

    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == "725499864854560818":
        match_channel_number = 1
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        match_channel_number = 2
    if ctx.message.channel.name == "hosting-server3":
        match_channel_number = 3
    if ctx.message.channel.name == "hosting-server4":
        match_channel_number = 4

    if match_channel_number == 0:
        await bot.say("Please use forcedrop command in the channel that is hosting the game where you want to drop that person")

    for i in running_games_list:
        if i.match_channel_number == match_channel_number and not i.game_join_stage_ended and not i.game_has_started:
            if number == 0 or number > len(i.waiting_players):
                return

            embed = discord.Embed(description = f"**{i.waiting_players[number-1].name} got force dropped!**" ,color = 0xfe4040)
            embed.set_footer(text = f'Force dropped by: {ctx.message.author}' ,icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
            embed.set_author(name=f"Game {i.game_id}", icon_url =main_logo)
            log_channel = discord.utils.get(ctx.message.server.channels, name="5v5-logs")
            await bot.send_message(log_channel ,embed=embed)
            i.waiting_players.remove(i.waiting_players[number - 1])
            await bot.delete_message(ctx.message)
            i.update_this_tick = True

@bot.command(pass_context = True)
async def leave(ctx):
    for i in running_games_list:
        if ctx.message.author in i.waiting_players and not i.game_join_stage_ended and not i.game_has_started:
            i.waiting_players.remove(ctx.message.author)
            await bot.delete_message(ctx.message)
            i.update_this_tick = True


@bot.command(pass_context = True)
async def game(ctx , result):
    team1_role_lst = ["724754010573111296",  "729363219151454279", "724754010573111296", "724754010573111296"]
    team2_role_lst = ["724754011164639412",  "729363380170784789", "724754011164639412", "724754011164639412"]
    print('hello?')
    sv = bot.get_server(ctx.message.server.id)
    await bot.delete_message(ctx.message)
    if not await is_allowed(ctx.message.author , average_perms):
        return
    match_channel_number = 0

    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == '725499864854560818':
        match_channel_number = 1
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        match_channel_number = 2
    if ctx.message.channel.name == "hosting-server3":
        match_channel_number = 3
    if ctx.message.channel.name == "hosting-server4":
        match_channel_number = 4

    team1_role = discord.utils.get(sv.roles, id = team1_role_lst[match_channel_number - 1])
    team2_role = discord.utils.get(sv.roles, id = team2_role_lst[match_channel_number - 1])


    if match_channel_number == 0:
        return await bot.say("You can't use this command here!", delete_after=3.0)

    c = 0
    game = None
    for i in running_games_list:
        if i.match_channel_number == match_channel_number and not i.game_has_ended:
            game = i
            break

    if game == None:
        return await bot.say(f"There's no game running in this channel.", delete_after=3.0)

    await save_players()
    try:
        result = int(result)
        if not game.game_has_started:
            return await bot.say("This game hasn't started yet!")
        if(result != 1 and result != 2):
            return await bot.say(f"Use {pref}game [WINNING TEAM : 1 OR 2 OR TIE]")

        if(result == 1):
            game.winning_team = game.team1
            game.losing_team = game.team2
        if(result == 2):
            game.winning_team = game.team2
            game.losing_team = game.team1

        average_elo = 0
        countelo = 0
        winids = []
        loseids = []
        for i in game.winning_team:
            winids.append(i.id)
        for i in game.losing_team:
            loseids.append(i.id)
        elo_modifier = 1
        if not game.is_2v2:
            elo_modifier = 1.5
        winning_team = []
        losing_team = []
        l_elo = 0
        w_elo = 0

        for i in player_list:
            if i.id in winids:
                winning_team.append(i)
            if i.id in loseids:
                losing_team.append(i)

        for i in winning_team:
            average_elo = 0
            l_elo = 0
            for x in losing_team:
                l_elo += x.elo
                #average_elo += EloRating(i.elo,x.elo,60,1)[0]
            test = int(i.elo) / 100 + 13
            random_elo1 = math.floor(test)
            mathshit = int(l_elo) / (random_elo1 * 10)
            if game.is_2v2:
                random_elo = math.floor(mathshit) * 2.5
            else:
                random_elo = math.floor(mathshit)

            i.elo += random_elo * game.elox

            game.winning_team_elo[countelo] = random_elo * game.elox
            print(random_elo)
                
            i.winstreak += 1
            i.add_win()

            countelo += 1
        average_elo = 0
        countelo = 0
        for i in losing_team:
            average_elo = 0
            for x in winning_team:
                w_elo += x.elo
            test = int(i.elo) / 100 + 3
            random_elo5 = math.floor(test) + 5
            i.elo -= random_elo5 * game.elox * game.elox
            print(random_elo5)
            game.losing_team_elo[countelo] = random_elo5

            average_elo = 0
            i.winstreak = 0
            i.add_lose()
            countelo += 1

        game.game_has_ended = True
        game.game_has_started = True
        game.game_join_stage_ended = True
        sv = bot.get_server(ctx.message.author.server.id)
        #canal = discord.utils.get(sv.channels, name="bot-logs")
        ended_games_list.append(game)
        running_games_list.remove(game)
        return await endgameimage(game)
    except:
        try:
            result = int(result)
        except:
            if result.lower() == "tie":
                game.game_has_been_handled = True
                game.game_has_ended = True
                game.game_has_started = True
                game.game_join_stage_ended = True
                ended_games_list.append(game)
                running_games_list.remove(game)
                return await bot.say(f"Game {game.game_id} has been tied")
                


                try:
                    for x in game.team1:
                        try:
                            await bot.remove_roles(x,team1_role)
                        except:
                            continue

                    for y in game.team2:
                        try:
                            await bot.remove_roles(y,team2_role)
                        except:
                            continue
                except:
                    print('error')
                    
@bot.command(pass_context = True)
async def gamesrunning(ctx):
    nr = len(running_games_list)
    if nr == 0:
        nr = "0"
    await bot.say(nr)

@bot.command(pass_context = True)
async def gamesplayed(ctx):
    nr = len(ended_games_list)
    if nr == 0:
        nr = "0"
    await bot.say(nr)

@bot.command(pass_context = True)
async def blacklist(ctx , user: discord.Member,timer: int):
    if not await is_allowed(ctx.message.author , average_perms):
        return
    #await bot.add_roles(user,role)
    await bot.say(f"{user.mention} is now blacklisted for {timer}h")
    bl = Blacklist(timer,time.time() + timer * 3600,user)
    blacklisted_members.append(bl)
    await asyncio.sleep(timer * 3600)
    try:
        blacklisted_members.remove(bl)
    except:
        pass

@bot.command(pass_context = True)
async def blackcapt(ctx , user: discord.Member = None):
    user = ctx.message.author if not user else user
    if not await is_allowed(ctx.message.author , middle_perms) and user != ctx.message.author:
        return

    player = await get_player_member(user.id)
    player.blackcapt = True


@bot.command(pass_context = True, aliases=['currentpassword', 'currentpass'])
async def password(ctx):
   


    pass_send = ''
    
    username = ctx.message.author.name
    channel = ctx.message.channel.id
    author = ctx.message.author


    #debuglog = client.get_channel(debuglog_id)

    global server0_pass
    global server1_pass
    global server2_pass
    global server3_pass

    server_num = ''

    if not await is_allowed(ctx.message.author , average_perms):
        return

    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == '725499864854560818':
        server_num = 1
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        server_num = 2
    if ctx.message.channel.name == "hosting-server3":
        server_num = 3
    if ctx.message.channel.name == "hosting-server4":
        server_num = 4

    
    



            

    #player = get(member.guild.roles, name='player')
    if int(server_num) == 1: #5v5 server 2
        ftp_add = 'twoversustwo.game.nfoservers.com'
        ftp_port = 21
        ftp_cred = ['twoversustwo', 'RyzjgXZGqD6GgWy']
        ftp_direct = '/csgo/cfg'




        final_name = 'server.cfg'
        
        address = [("twoversustwo.game.nfoservers.com", 27015), 'nC9nLQ83274HPFhfhI424']

        ip = 'twoversustwo.game.nfoservers.com:27015'

        strip_num = 5

        pass_send = server0_pass
        do_ftp = True


    if int(server_num) == 3: #2v2 server 2
        ftp_add = '176.57.158.200'
        ftp_port = 21
        ftp_cred = ['gpftp1122507392175613', 'm5FD0MDJ']
        ftp_direct = '/csgo/cfg'

        address = [("176.57.158.181", 27015), 'GalaxyHvH2v2'] 

        ip = '176.57.158.181:27015'

        final_name = 'server.cfg'

        strip_num = 3

        pass_send = server1_pass
        do_ftp = True

    if int(server_num) == 0:#5v5 server 1

        print('3')
        ftp_add = '176.57.158.203'
        ftp_port = 21
        ftp_cred = ['gpftp1122507392177713', 'w19jmFw7']
        ftp_direct = '/csgo/cfg'

        final_name = 'server.cfg'

        ip = '176.57.158.203:27015'

        strip_num = 3
        address = [("176.57.158.203", 27015), 'sefumati23'] 

        pass_send = server2_pass
        do_ftp = True

    if int(server_num) == 2: #2v2 server 1
       # return
        print('4')
        ftp_add = '98.174.158.25'
        ftp_port = 22
        ftp_cred = ['csgo', 'PoopButt123']
        ftp_direct = '/home/csgo/Steam/csgo-ds/csgo/cfg'



        final_name = 'server.cfg'
        address = [("98.174.158.25", 27015), 'PoopButt123'] 
        ip = '98.174.158.25:27015'

        pass_send = server3_pass 





    serverip = discord.Embed(description=f"```\nconnect {ip}; password {pass_send}```" ,color = 0xfe4040)
    serverip.set_footer(text = f'Darius bot', icon_url = main_logo)
    serverip.set_author(name="Server IP:", icon_url = main_logo)
    serverip.add_field(name="**Direct connect:**", value=f"[steam://connect/{ip};/{pass_send}](steam://connect/{ip};/{pass_send})", inline=False)
    serverip.set_thumbnail(url=main_logo)

    await bot.send_message(author, embed=serverip)



@bot.command(pass_context = True)
async def resendpw(ctx):


    print('1')
    pass_send = ''
    
    username = ctx.message.author.name
    channel = ctx.message.channel.id
    author = ctx.message.author

    games = []
    #debuglog = client.get_channel(debuglog_id)

    global server0_pass
    global server1_pass
    global server2_pass
    global server3_pass

    server_num = ''

    if not await is_allowed(ctx.message.author , average_perms):
        return

    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == '725499864854560818':
        server_num = 1
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        server_num = 2
    if ctx.message.channel.name == "hosting-server3":
        server_num = 3
    if ctx.message.channel.name == "hosting-server4":
        server_num = 4


    server_num_ip= int(server_num - 1)
    print(str(server_num))
    server = 2

    #player = get(member.guild.roles, name='player')
    if int(server_num) == 2: #5v5 server 2
        ftp_add = 'na2v2.game.nfoservers.com'
        ftp_port = 21
        ftp_cred = ['na2v2', 'SGgLdpWfX5n6sQ3dZXUA']
        ftp_direct = '/csgo/cfg'




        final_name = 'server.cfg'

        address = [("na2v2.game.nfoservers.com", 27015), 'XpNzyp'] 

        ip = 'na2v2.game.nfoservers.com:27015'

        strip_num = 3

        pass_send = server0_pass
        do_ftp = True


    if int(server_num) == 4: #2v2 server 2
        ftp_add = '176.57.158.200'
        ftp_port = 21
        ftp_cred = ['gpftp1122507392175613', 'm5FD0MDJ']
        ftp_direct = '/csgo/cfg'

        address = [("176.57.158.181", 27015), 'GalaxyHvH2v2'] 

        ip = '176.57.158.181:27015'

        final_name = 'server.cfg'

        strip_num = 3

        pass_send = server1_pass
        do_ftp = True

    if int(server_num) == 1:#5v5 server 1

        print('3')
        ftp_add = '176.57.158.203'
        ftp_port = 21
        ftp_cred = ['gpftp1122507392177713', 'w19jmFw7']
        ftp_direct = '/csgo/cfg'

        final_name = 'server.cfg'

        ip = '176.57.158.203:27015'

        strip_num = 3
        address = [("176.57.158.203", 27015), 'sefumati23'] 

        pass_send = server2_pass
        do_ftp = True
    if int(server_num) == 3: #2v2 server 1
       # return
        print('4')
        ftp_add = '176.57.158.181'
        ftp_port = 21
        ftp_cred = ['gpftp1122507392174413', 'cmYdiRXA']
        ftp_direct = '/csgo/cfg'

        final_name = 'server.cfg'

        ip = '176.57.158.181:27015'

        strip_num = 1


        address = [("176.57.158.181", 27015), 'sefumati23'] 

        pass_send = server3_pass 
        do_ftp = True


    print('2')
    if server_num == 0:
        return await bot.say("You can only resend the password in a channel with a live game!", delete_after=3.0)

    for i in running_games_list:
        try:
            print(str(i.match_channel_number))
            print(str(server_num + 1))
        except:
            print('sjit languasdnasd;')
        if i.match_channel_number == server_num and not i.game_has_ended:
            games.append(i)

    if len(games) == 0:
        return await bot.say("There aren't any games running in this channel!", delete_after=4.0)

    game = games[len(games) - 1]

    print('close')
    serverip2 = discord.Embed(description=f"```\nconnect {ip}; password {pass_send}```" ,color = 0xfe4040)
    serverip2.set_footer(text = f'2v2', icon_url = main_logo)
    serverip2.set_author(name="Server IP:", icon_url = main_logo)
    serverip2.add_field(name="**Direct connect:**", value=f"[steam://connect/{ip};/{pass_send}](steam://connect/{ip};/{pass_send})", inline=False)
    serverip2.set_thumbnail(url=main_logo)

    for i in range(len(game.team1)):

        await bot.send_message(game.team1[i], embed=serverip2)
    for i in range(len(game.team2)):

        await bot.send_message(game.team2[i], embed=serverip2)

   # await bot.send_message(author, embed=serverip)










@bot.command(pass_context = True)
async def bltime(ctx,user: discord.Member = None):
    user = ctx.message.author if not user else user
    for i in blacklisted_members:
        if i.user.id == user.id:
            hours = (i.expire_time - time.time()) / 3600
            rounded_hours = int((i.expire_time - time.time()) / 3600)
            return await bot.say(f"{user.name} is blacklisted for another {rounded_hours}h and {int((hours - rounded_hours) * 60)}m")
    await bot.say(f"{user.name} is not blacklisted!")

@bot.command(pass_context = True, aliases=['whitelist'])
async def removeblacklist(ctx ,user: discord.Member):
    if not await is_allowed(ctx.message.author , average_perms):
        return
    #await bot.add_roles(user,role)
    await bot.say(f"{user.name} has been whitelisted!", delete_after=5.0)
    for i in blacklisted_members:
        if i.user == user:
            blacklisted_members.remove(i)

@bot.command(pass_context = True)
async def join(ctx):
    number = 0

    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == "725499864854560818":
        number = 1
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        number = 2
    if ctx.message.channel.name == "hosting-server3":
        number = 3
    if ctx.message.channel.name == "hosting-server4":
        number = 4

    if number == 0:
        return await bot.say("You can't join in this channel!")

    c = 0
    for i in running_games_list:
        if not i.game_join_stage_ended and not i.game_has_been_canceled:
            c += 1
    if c == 0:
        return await bot.say("There's no open queue in this channel!", delete_after=5.0)
    for i in blacklisted_members:
        if i.user == ctx.message.author:
            return await bot.say(f"You can't join this game because you are blacklisted for {i.time}h, {ctx.message.author.mention}!", delete_after=10.0)
    for i in running_games_list:
        if (ctx.message.author in i.waiting_players or ctx.message.author in i.team1 or ctx.message.author in i.team2) and not i.game_has_ended:
            await bot.delete_message(ctx.message)
            msg = await bot.say("You're already in a game!")
            return await bot.delete_message(msg)

    for i in running_games_list:
        #print(i.hoster.name)
        if i.match_channel_number == number and not i.game_join_stage_ended and not i.game_has_ended:
            #print('test')
            for x in i.waiting_players:
                if x.id == ctx.message.author.id:
                    return
            i.waiting_players.append(ctx.message.author)
            #msg = await bot.say(f"{ctx.message.author.name} joined the game!")
            #await asyncio.sleep(0.1)
            #await bot.delete_message(msg)
            i.update_this_tick = True

    await bot.delete_message(ctx.message)



@bot.command(pass_context = True)
async def forcejoin(ctx,user: discord.Member = None):
    number = 0
    if user.bot:
        return await bot.say("You can't forcejoin a bot")
    if user == None:
        return await bot.say("You have to specifiy the person you want to forcejoin")

    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == "725499864854560818":
        number = 1
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        number = 2
    if ctx.message.channel.name == "hosting-server3":
        number = 3
    if ctx.message.channel.name == "hosting-server4":
        number = 4

    if number == 0:
        return await bot.say("You can't join in this channel!")

    c = 0
    for i in running_games_list:
        if not i.game_join_stage_ended and not i.game_has_been_canceled:
            c += 1
    if c == 0:
        return await bot.say("There's no games running in this channel")
    for i in blacklisted_members:
        if i.user == user:
            return await bot.say(f"You can't join this game because you are blacklisted for {i.time}h")
    for i in running_games_list:
        if (user in i.waiting_players or user in i.playing_players) and not i.game_has_ended:
            await bot.delete_message(ctx.message)
            msg = await bot.say("You're already in a game!")
            return await bot.delete_message(msg)

    for i in running_games_list:
        #print(i.hoster.name)
        if i.match_channel_number == number and not i.game_join_stage_ended and not i.game_has_ended:
            #print('test')
            for x in i.waiting_players:
                if x.id == user.id:
                    return
            i.waiting_players.append(user)
            #msg = await bot.say(f"{ctx.message.author.name} joined the game!")
            #await asyncio.sleep(0.1)
            #await bot.delete_message(msg)
            i.update_this_tick = True

    await bot.delete_message(ctx.message)


@bot.command(pass_context = True, aliases=['end'])
async def cancel(ctx):
    games = []
    if not await is_allowed(ctx.message.author , average_perms):
        return
    team1_role_lst = ["724754010573111296",  "729363219151454279", "724754010573111296", "724754010573111296"]
    team2_role_lst = ["724754011164639412",  "729363380170784789", "724754011164639412", "724754011164639412"]
    number = 0
    sv = bot.get_server("724753968508698674")
    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == "725499864854560818":
        number = 1
        ch = discord.utils.get(sv.channels, id="725499864854560818")
        queue = discord.utils.get(sv.channels, id="709107209581232309")
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        number = 2
        ch = discord.utils.get(sv.channels, name="hosting-server2")
        queue = discord.utils.get(sv.channels, id="729146344773648444")
    if ctx.message.channel.name == "hosting-server3":
        number = 3
        ch = discord.utils.get(sv.channels, name="hosting-server3")
        queue = discord.utils.get(sv.channels, id="709107224877727885")
    if ctx.message.channel.name == "hosting-server4":
        number = 4
        ch = discord.utils.get(sv.channels, name="hosting-server4")
        queue = discord.utils.get(sv.channels, id="709107231718899821")

    for i in running_games_list:
        if ctx.message.author == i.hoster and not i.game_has_ended == True and not i.game_has_started and i.match_channel_number == number:
            games.append(i)

    cool = ctx.message.author.avatar_url.split('/avatars/')
    try:
        final = cool[1].split('.jpg')
        final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
    except:
        final_av = ctx.message.author.default_avatar_url

    if len(games) == 0:
        return await bot.say("You're not hosting any games!", delete_after=5.0)
    game = games[len(games) - 1]
    game.game_has_been_canceled = True
    game.game_has_ended = True
    ended_games_list.append(game)
    running_games_list.remove(game)
 #   await purge(ctx, 99)
    embed = discord.Embed(description = "**Canceled!**" ,color = 0xfe4040)
    embed.set_footer(text = f'Host: {game.hoster}\nCanceled by: {ctx.message.author}' ,icon_url = final_av)
    embed.set_author(name=f"Game {game.game_id}", icon_url =final_av)
    #embed.set_footer(text=f"{ctx.message.author}", icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
    await bot.edit_message(game.embed_msg, embed=embed)
    log_channel = discord.utils.get(ctx.message.server.channels, name="5v5-logs")
    await bot.send_message(log_channel,embed=embed)
    await bot.delete_message(ctx.message)

    sv = ctx.message.server
    team1_role = discord.utils.get(sv.roles, id = team1_role_lst[game.match_channel_number - 1])
    team2_role = discord.utils.get(sv.roles, id = team2_role_lst[game.match_channel_number - 1])
    for x in game.team1:
        try:
            await bot.remove_roles(x,team1_role)
            await bot.move_member(x, queue)
        except:
            continue

    for y in game.team2:
        try:
            await bot.remove_roles(y,team2_role)
            await bot.move_member(y, queue)
        except:
            continue
    asyncio.sleep(30)
    await bot.delete_message(game.embed_msg)
    #return await bot.delete_message(msg)


@bot.command(pass_context = True, aliases=['forceend'])
async def forcecancel(ctx):

    games = []
    if not await is_allowed(ctx.message.author , average_perms):
        return

    sv = bot.get_server("724753968508698674")
    team1_role_lst = ["724754010573111296",  "729363219151454279", "724754010573111296", "724754010573111296"]
    team2_role_lst = ["724754011164639412",  "729363380170784789", "724754011164639412", "724754011164639412"]

    number = 0
    if ctx.message.channel.name == "hosting-server1" or ctx.message.channel.id == "725499864854560818":
        number = 1
        ch = discord.utils.get(sv.channels, name="hosting-server1")
        queue = discord.utils.get(sv.channels, id="709107209581232309")
    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        number = 2
        ch = discord.utils.get(sv.channels, name="hosting-server2")
        queue = discord.utils.get(sv.channels, id="729146344773648444")
    if ctx.message.channel.name == "hosting-server3":
        number = 3
        ch = discord.utils.get(sv.channels, name="hosting-server3")
        queue = discord.utils.get(sv.channels, id="709107224877727885")
    if ctx.message.channel.name == "hosting-server4":
        number = 4
        ch = discord.utils.get(sv.channels, name="hosting-server4")
        queue = discord.utils.get(sv.channels, id="709107231718899821")
   # await purge(ctx, 99)
    if number == 0:
        return await bot.say("Go forcecancel in the channel with the game you want to end!")

    for i in running_games_list:
        if i.match_channel_number == number:
            games.append(i)

    if len(games) == 0:
        return await bot.say("There aren't any games running in this channel!")





    cool = ctx.message.author.avatar_url.split('/avatars/')
    try:
        final = cool[1].split('.jpg')
        final_av = f"https://cdn.discordapp.com/avatars/{ctx.message.author.id}/" + final[0] + '.png' + '?size=256&f=.png'
    except:
        final_av = ctx.message.author.default_avatar_url



    game = games[len(games) - 1]
    game.game_has_been_canceled = True
    game.game_has_ended = True
    ended_games_list.append(game)
    running_games_list.remove(game)
    embed = discord.Embed(description = "**Canceled!**" ,color = 0xfe4040)
    embed.set_footer(text = f'Host: {game.hoster}\nCanceled by: {ctx.message.author}' ,icon_url = final_av)
    embed.set_author(name=f"Game {game.game_id}", icon_url =final_av)
    await bot.edit_message(game.embed_msg, embed=embed)
    log_channel = discord.utils.get(ctx.message.server.channels, name="5v5-logs")
    await bot.send_message(log_channel,embed=embed)
    await bot.delete_message(ctx.message)

    
    team1_role = discord.utils.get(sv.roles, id = team1_role_lst[game.match_channel_number - 1])
    team2_role = discord.utils.get(sv.roles, id = team2_role_lst[game.match_channel_number - 1])
    for x in game.team1:
        try:
            await bot.remove_roles(x,team1_role)
            await bot.move_member(x, queue)
        except:
            continue

    for y in game.team2:
        try:
            await bot.remove_roles(y,team2_role)
            await bot.move_member(y, queue)
        except:
            continue
    #return await bot.delete_message(msg)


@bot.command(pass_context = True, aliases=['sub'])
async def replace(ctx, user1: discord.Member = None , user2: discord.Member = None): # user1 - to be replaced ----- user2 - is replacement
    pass_send = ''
    games = []
    if not await is_allowed(ctx.message.author , average_perms):
        return

    number = 0

    if ctx.message.channel.name == "queue" or ctx.message.channel.id == "725499864854560818":
        canal1 = discord.utils.get(ctx.message.server.channels, id="709107212622102580")
        canal2 = discord.utils.get(ctx.message.server.channels, id="709107214564196393")
        queue = discord.utils.get(ctx.message.server.channels, id="709107209581232309")
        number = 1

    if ctx.message.channel.name == "hosting-server2" or ctx.message.channel.id == '729821342215438408':
        canal1 = discord.utils.get(ctx.message.server.channels, id="729146306387509269")
        canal2 = discord.utils.get(ctx.message.server.channels, id="729146324531937391")
        queue = discord.utils.get(ctx.message.server.channels, id="729146344773648444")
        number = 2
    if ctx.message.channel.name == "hosting-server3":
        canal1 = discord.utils.get(ctx.message.server.channels, id="709107227356823605")
        canal2 = discord.utils.get(ctx.message.server.channels, id="709107229558833267")
        queue = discord.utils.get(ctx.message.server.channels, id="709107224877727885")
        number = 3
    if ctx.message.channel.name == "hosting-server4":
        canal1 = discord.utils.get(ctx.message.server.channels, id="709107233983561768")
        canal2 = discord.utils.get(ctx.message.server.channels, id="709107236512858276")
        queue = discord.utils.get(ctx.message.server.channels, id="709107231718899821")
        number = 4
    if number == 2: #5v5 server 2
        ip = '176.57.158.204:27015'
        pass_send = server0_pass
    if number == 3: #2v2 server 2
        ip = '176.57.158.181:27015'
        pass_send = server1_pass
    if number == 1:#5v5 server 1
        ip = '176.57.158.203:27015'
        pass_send = server2_pass
    if number == 4: #2v2 server 1
        ip = '176.57.158.181:27015'
        pass_send = server3_pass 

    for i in running_games_list:
        if i.match_channel_number == number:
            if i.game_join_stage_ended and i.game_has_started:
                games.append(i)
            else:
                return await bot.say("Game has to start first before you can replace anyone!")

    if len(games) == 0:
        return await bot.say("You're not hosting any games!")

    if user1.bot:
        return await bot.say("You can't replace a bot as they're not part of a team!")
    if user2.bot:
        return await bot.say("You can't replace an user with a bot!")

    if user1.id == user2.id:
        return await bot.say("You can't replace this user with himself!")


    for i in running_games_list:
        if user2 in i.team1 or user2 in i.team2 or user2 in i.waiting_players:
            return await bot.say(f"{user2.name} is playing a game right now and therefore can't be a replacement")


    game = games[len(games) - 1]
    team1 = 0
    team2 = 0
    for i in game.team1:
        if i.id == user1.id:
            team1 = 1
        if i.id == user2.id:
            team2 = 1
    for i in game.team2:
        if i.id == user1.id:
            team1 = 2
        if i.id == user2.id:
            team2 = 2

    if team1 == 0:
        return await bot.say(f"{user1.name} isn't part of any team therefore you can't replace him with {user2.name}!")

    if team2 != 0:
        return await bot.say(f"{user2.name} is already part of a team!")


    team1_role_lst = ["724754010573111296",  "729363219151454279", "724754010573111296", "724754010573111296"]
    team2_role_lst = ["724754011164639412",  "729363380170784789", "724754011164639412", "724754011164639412"]
    sv = bot.get_server("724753968508698674")
    team1_role = discord.utils.get(sv.roles, id = team1_role_lst[number - 1])
    team2_role = discord.utils.get(sv.roles, id = team2_role_lst[number - 1])
    try:
        print(team1_role.name)
        print(team2_role.name)
    except:
        pass
    for i in game.playing_players:
        if i.id == user1.id:
            game.playing_players.remove(i)

    for i in game.waiting_players:
        if i.id == user1.id:
            game.waiting_players.remove(i)

    serverreplaceip = discord.Embed(description=f"```\nconnect {ip}; password {pass_send}```" ,color = 0xfe4040)
    serverreplaceip.set_footer(text = f'2v2 TEAM', icon_url = main_logo)
    serverreplaceip.set_author(name="Server IP:", icon_url = main_logo)
    serverreplaceip.add_field(name="**Direct connect:**", value=f"[steam://connect/{ip};/{pass_send}](steam://connect/{ip};/{pass_send})", inline=False)
    serverreplaceip.set_thumbnail(url=main_logo)

    for i in game.team1:
        if i.id == user1.id:
            game.team1.remove(i)
            game.team1.append(user2)
            try:
                await bot.remove_roles(i,team1_role)
                await bot.add_roles(user2,team1_role)
                await bot.send_message(user2,embed=serverreplaceip)
                await bot.move_member(i, queue)
                await bot.move_member(user2,canal1)
            except:
                pass


    for i in game.team2:
        if i.id == user1.id:
            game.team2.remove(i)
            game.team2.append(user2)
            try:
                await bot.add_roles(user2,team2_role)
                await bot.send_message(user2,embed=serverreplaceip)
                await bot.move_member(i, queue)
                await bot.move_member(user2,canal2)
            except:
                pass

    embed = discord.Embed(description = f"{user1.name} was replaced with {user2.name}" ,color = 0xfe4040)
    embed.set_footer(text = f'Replaced by: {ctx.message.author.name}' ,icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
    embed.set_author(name=f"Member replaced!", icon_url =main_logo)
    #embed.set_footer(text=f"{ctx.message.author}", icon_url = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
    msg = await bot.say(embed=embed)
    log_channel = discord.utils.get(ctx.message.server.channels, name="5v5-logs")
    await bot.send_message(log_channel , embed=embed)
    await bot.delete_message(ctx.message)


    #return await bot.delete_message(msg)


# 16 stanga/dreapta si 9 sus / jos
async def startgameimage(game , ctx):
    im = Image.open("2v2galaxy.png")
    number = 0
    number2 = 0
    mult = 0
    number3 = 0
    number4 = 0
    sv = bot.get_server("724753968508698674")
    ch2 = discord.utils.get(sv.channels, name="gm")
    font = ImageFont.truetype("arial.ttf", 28)
    if game.is_2v2:
        number = 190
        number2 = 23
        number3 = 125
        number4 = 375
        mult = 50

    else:
        number = 118
        number2 = 20
        number3 = 125
        number4 = 350
        mult = 50
        font = ImageFont.truetype("arial.ttf", 26)
        im = Image.open("5v5galaxy.png")


    draw = ImageDraw.Draw(im)


    counter = 0
    for i in game.team1:
        place = number + mult * counter
        if(counter == 4):
            place -= 1.5
        draw.text((number2,place ), i.name[:13],(255,255,255), font=font)
        counter += 1
    counter = 0
    for i in game.team2:
        place = number + mult * counter
        if(counter == 4):
            place -= 1.5
        draw.text((im.size[0] / 2 + number3 , place), i.name[:13],(255,255,255), font=font)
        counter += 1
    draw.text((im.size[0] / 2 - font.getsize(f"Hoster: {game.hoster.name}")[0] / 2, number4), f"Hoster: {game.hoster.name}",(255,255,255), font=font)
    im.save("image.png")
    embed2 = discord.Embed(colour=0xfc1016) #red
    msg = await bot.send_file(ch2, 'image.png')
    embed2.set_image(url=msg.attachments[0]['url'])
    print(msg.attachments[0]['url'])
    embed2.set_author(name=f"Game #{game.game_id}! Good luck and have fun!", icon_url=msg.attachments[0]['url'])
  #  await bot.send_message(ctx.message.channel , f"")
    await bot.say(embed=embed2)
    mentions = ''

    for i in range(len(game.team1)):
        mention = game.team1[i].mention
        mention2 = game.team2[i].mention
        mentions += f'{mention} {mention2} '

    await bot.say(mentions + '\nCheck your PMs for the ip & password to the CS:GO Server.\n\n If you get the Error Bad password type "retry" in console.\nIf the error does not fix itself message a staff member.')

# @bot.command(pass_context = True)
# async def teststartgameimage(ctx):
#     im = Image.open("2v2galaxy.png")
#     #im = Image.open("2v2project2v2.png")
#     draw = ImageDraw.Draw(im)
#     font = ImageFont.truetype("arial.ttf", 26)
#     counter = 0
#     names = [ "louisiana" , "conrad"]
#     is_2v2 = False
#     number = 190
#     for i in names:
#         place = number + 50 * counter
#         if(counter == 4):
#             place -= 1.5
#         draw.text((23,place ), i,(255,255,255), font=font)
#         counter += 1
#     counter = 0
#     for i in names:
#         place = number + 50 * counter
#         if(counter == 4):
#             place -= 1.5
#         draw.text((im.size[0] / 2 + 125 , place), i,(255,255,255), font=font)
#         counter += 1
#     draw.text((im.size[0] / 2 - font.getsize(f"Hoster: louisiana")[0] / 2, 320), f"Hoster:  louisiana",(255,255,255), font=font)
#     im.save("image.png")
#
#     await bot.send_message(ctx.message.channel , f"**Game #1! Good luck and have fun!**")
#     await bot.send_file(ctx.message.channel, 'image.png')


# @bot.command(pass_context = True)
# async def teststartgame(ctx):
#     im = Image.open("2v2project2v2.png")
#     number = 0
#     number2 = 0
#     if False:
#         number = 75
#         number2 = 170
#     else:
#         number = 75
#         number2 = 125
#         #im = Image.open("5v5galaxy.png")
#
#
#     draw = ImageDraw.Draw(im)
#     font = ImageFont.truetype("arial.ttf", 28)
#     counter = 0
#     names = ["Louisiana" , "madcatz"]
#     for i in names:
#         place = number + 52 * counter
#         if(counter == 4):
#             place -= 1.5
#         draw.text((45,place ), i[:13],(255,255,255), font=font)
#         counter += 1
#     counter = 0
#     for i in names:
#         place = number + 52 * counter
#         if(counter == 4):
#             place -= 1.5
#         draw.text((im.size[0] / 2 + 130 , place), i[:13],(255,255,255), font=font)
#         counter += 1
#     draw.text((im.size[0] / 2 - font.getsize(f"Hoster: louisiana")[0] / 2, number2), f"Hoster: louisiana",(255,255,255), font=font)
#     im.save("image.png")
#
#     await bot.send_message(ctx.message.channel , f"**Game #1! Good luck and have fun!**")
#     await bot.send_file(ctx.message.channel, 'image.png')



async def endgameimage(game):
    team1_role_lst = ["724754010573111296",  "729363219151454279", "724754010573111296", "724754010573111296"]
    team2_role_lst = ["724754011164639412",  "729363380170784789", "724754011164639412", "724754011164639412"]
    sv = bot.get_server("724753968508698674")

    im = Image.open("unknown.png")
    number = 0
    number2 = 0
    mult = 0
    number3 = 0
    number4 = 0
    counter_multiply = 70
    if game.is_2v2:
        number = 115
        number2 = 15
        number3 = 520
        counter_multiply = 311.5
    else:
        number = 40
        number2 = 15
        number3 = 520
        counter_multiply = 311.5
        im = Image.open("unknown.png")

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 50)

    ch = None
    queue = None

    results = discord.utils.get(sv.channels, id="725608518530367558")

    if game.match_channel_number == 1:
        ch = discord.utils.get(sv.channels, id="725499864854560818")
        queue = discord.utils.get(sv.channels, id="717473190359597066")

    if game.match_channel_number == 2:
        ch = discord.utils.get(sv.channels, name="hosting-server2")
        queue = discord.utils.get(sv.channels, id="688539174554697790")
    if game.match_channel_number == 3:
        ch = discord.utils.get(sv.channels, name="hosting-server3")
        queue = discord.utils.get(sv.channels, id="691145586799411211")
    if game.match_channel_number == 4:
        ch = discord.utils.get(sv.channels, name="hosting-server4")
        queue = discord.utils.get(sv.channels, id="691746601558867988")

    sv = bot.get_server("724753968508698674")

    print('almost')
    team1_role = discord.utils.get(sv.roles, id = team1_role_lst[game.match_channel_number - 1])
    
    team2_role = discord.utils.get(sv.roles, id = team2_role_lst[game.match_channel_number - 1])
    try:
        await results.send(f'{game.winning_team[0]} and {game.winning_team[1]} have beat {game.losing_team[0]} and {game.losing_team[1]}.')

    except:
        print('error')
    #await bot.send_message(ch , f"Game #{game.game_id} results.\nWinning Team:")
    counter = 0
    for i in game.winning_team:
        draw.text((number2,number + counter *  counter_multiply), i.name[:12] ,(255,0,0), font=font)
        draw.text((number3 ,number + counter * counter_multiply), f" +{int(game.winning_team_elo[counter])}" ,(255,0,0), font=font)
        shape = [(1, 311.5*counter), (622, 311.5*counter)] 
        draw.line(shape, fill ="red", width =4) 
        counter += 1



        #draw.text((15,40 + counter * 124.6), i ,(255,0,0), font=font)
        #draw.text((520 ,40 + counter * 124.6), f" -30" ,(255,0,0), font=font) # 260 with +


    shape2 = [(1, 623), (622, 622)] 
    draw.line(shape2, fill ="red", width =4) 

    shape3 = [(0, 1), (0, 622)] 
    draw.line(shape3, fill ="red", width =4) 
    shape4 = [(621, 1), (621, 622)] 
    draw.line(shape4, fill ="red", width =4) 

    shape5 = [(1, 621), (622, 621)] 
    draw.line(shape5, fill ="red", width =4) 

    shape6 = [(500, 1), (500, 622)] 
    draw.line(shape6, fill ="red", width =4) 

    im.save("image.png")


    embed = discord.Embed(colour=0xfc1016) #Red
    ch2 = discord.utils.get(sv.channels, name="gm")
    msg = await bot.send_file(ch2, 'image.png')
    embed.set_image(url=msg.attachments[0]['url'])
    print(msg.attachments[0]['url'])
    embed.set_author(name=f"Results of game #{game.game_id}", icon_url=csgo_logo)  

  #  await bot.send_file(ch, 'image.png')




    await asyncio.sleep(0.2)

    im = Image.open("unknown.png")
    if(not game.is_2v2):
        im = Image.open("unknown.png")

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 50)
    counter = 0

    for i in game.losing_team:
        draw.text((number2,number + counter * counter_multiply), i.name[:12] ,(255,0,0), font=font)
        draw.text((number3 + 15,number + counter * counter_multiply), f"-{int(game.losing_team_elo[counter])}" ,(255,0,0), font=font)

        shape = [(1, 311.5*counter), (622, 311.5*counter)] 
        draw.line(shape, fill ="red", width =4) 


        counter += 1
    shape2 = [(1, 623), (622, 622)] 
    draw.line(shape2, fill ="red", width =4) 

    shape3 = [(0, 1), (0, 622)] 
    draw.line(shape3, fill ="red", width =4) 
    shape4 = [(621, 1), (621, 622)] 
    draw.line(shape4, fill ="red", width =4) 

    shape5 = [(1, 621), (622, 621)] 
    draw.line(shape5, fill ="red", width =4) 

    shape6 = [(500, 1), (500, 622)] 
    draw.line(shape6, fill ="red", width =4) 

    im.save("image.png")
    embed2 = discord.Embed(colour=discord.Color.blue()) #Blue
    msg = await bot.send_file(ch2, 'image.png')
    embed2.set_image(url=msg.attachments[0]['url'])
    print(msg.attachments[0]['url'])
    embed2.set_author(name=f"Results of game #{game.game_id}", icon_url=csgo_logo)
    im.save("image.png")

  #  await bot.send_message(ch, embed=embed)
  #  await bot.send_message(ch, embed=embed2)
    await bot.delete_message(game.embed_msg)

    await removeroles(team1_role, team2_role)

    for x in game.team1:
        try:
           
            bot.remove_roles(x,team1_role)
            print('r t1')
        except:
            continue         
        try:

           await bot.move_member(x, queue)
        except:
           continue

    for y in game.team2:
        try:
            print('r t2')
            bot.remove_roles(y,team2_role)
        except:
            continue
            

        try:
 
           await bot.move_member(y, queue)
        except:
           continue
#
# @bot.command(pass_context = True)
# async def testendgameimage(ctx):
#     im = Image.open("2v2galaxyend.png")
#     number = 0
#     number2 = 0
#     number3 = 0
#     number4 = 0
#     if False:
#         team_y = 165
#         team1_x = 105
#         team2_x = 410
#         counter_multiply = 85
#
#
#     draw = ImageDraw.Draw(im)
#     font = ImageFont.truetype("arial.ttf", 36)
#     sv = bot.get_server("688538836908638382")
#     ch = discord.utils.get(sv.channels, name="bot-commands")
#     await bot.send_message(ch , f"Game #number results.\nTeam #1")
#     counter = 0
#     names = ["louisiana" , "madcatz" ]
#     for i in names:
#         draw.text((5,100 + counter * 85), i ,(255,255,255), font=font)
#         draw.text((380 ,100 + counter * 85), f" -30" ,(255,255,255), font=font) # 260 with +
#         counter += 1
#
#     im.save("image.png")
#     await bot.send_file(ch, 'image.png')
#     await bot.send_message(ch, "\nTeam #2")
#     im = Image.open("2v2galaxyend.png")
#     if False:
#         number = 75
#         number2 = 170
#     else:
#         number = 125
#         number2 = 400
#         im = Image.open("5v5galaxyend.png")
#     names = ["louisiana" , "madcatz" ,"troll1" , "agsaggsaashoaghsagiasghiaghasghag" , "ezasda"]
#     draw = ImageDraw.Draw(im)
#     font = ImageFont.truetype("arial.ttf", 36)
#     counter = 0
#     for i in names:
#         draw.text((5,95 + counter * 77), i[:13] ,(255,255,255), font=font)
#         draw.text((395 ,95 + counter * 77), f" +30" ,(255,255,255), font=font) # 260 with +
#         counter += 1
#
#     im.save("image.png")
#     await bot.send_file(ch, 'image.png')

# Function to calculate the Probability
def Probability(rating1, rating2):

    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B.

def EloRating(Ra, Rb, K, d):

    new_Ra = 0
    new_Rb = 0
    # To calculate the Winning
    # Probability of Player B
    Pb = Probability(Ra, Rb)

    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(Rb, Ra)

    # Case -1 When Player A wins
    # Updating the Elo Ratings
    if (d == 1) :
        new_Ra = Ra + K * (1 - Pa)
        new_Rb = Rb + K * (0 - Pb)


    # Case -2 When Player B wins
    # Updating the Elo Ratings
    else :
        new_Ra = Ra + K * (0 - Pa)
        new_Rb = Rb + K * (1 - Pb)


    #print("Updated Ratings:-")

    #print("Ra =", round(new_Ra, 0) - Ra," Rb =", round(new_Rb, 0) - Rb)
    return [round(new_Ra, 0) - Ra , round(new_Rb, 0) - Rb]


@bot.command(pass_context = True)
async def help(ctx, member:discord.User = None):
    if not await is_allowed(ctx.message.author , average_perms):
        return
    me = await bot.application_info()
    owner = ctx.message.server.get_member(me.owner.id)
    embed = discord.Embed(title="Help", description="The following available commands:", color=0xfe4040, timestamp=datetime.datetime.utcnow())
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_thumbnail(url=main_logo)

    #embed.add_field(name="restrict [@player] [time]", value="Restricts someone from playing for a certain amount of time.", inline=False)
    embed.add_field(name=f"{pref}leaderboard [page]", value="Shows the  players with the highest elo.", inline=False)
    embed.add_field(name=f"{pref}resetleaderboard", value="Will reset the leaderboard.", inline=False)
    embed.add_field(name=f"{pref}addwin [@player]", value="Adds win", inline=False)
    embed.add_field(name=f"{pref}addelo [@player] [amount]", value="Adds elo", inline=False)
    embed.add_field(name=f"{pref}setelo [@player] [amount]", value="Sets elo", inline=False)
    embed.add_field(name=f"{pref}removeelo [@player] [amount]", value="Removes elo", inline=False)
    embed.add_field(name=f"{pref}addlose [@player]", value="Will add a lose into our official leaderboard.", inline=False)
    embed.add_field(name=f"{pref}removewin [@player]", value="Will remove a win from our official leaderboard.", inline=False)
    embed.add_field(name=f"{pref}removelose [@player]", value="Will remove a lose from our official leaderboard.", inline=False)
    embed.add_field(name=f"{pref}changepassword", value="Will change the password on the server relative to the channel. (hosting-1 = 5v5 server 1, hosting 2 = 5v5 server 2, etc)", inline=False)
    embed.add_field(name=f"{pref}password", value="Will send you the password on the server relative to the channel. (hosting-1 = 5v5 server 1, hosting 2 = 5v5 server 2, etc)", inline=False)
    embed.add_field(name=f"{pref}resendpw", value="Will resend the password of the server relative to the channel to each player in the match.", inline=False)

    embed.add_field(name=f"{pref}stats [@player]", value="Shows the current statistics of the specified player", inline=False)
    embed.add_field(name=f"{pref}rank [number]", value="Shows the current statistics of player currently ranked at NUMBER", inline=False)
    embed.add_field(name=f"{pref}game [1 OR 2 OR TIE]", value="game 1 - sets win for team 1 AND game 2 - sets win for team 2 AND game tie - ties the game", inline=False)
    embed.add_field(name=f"{pref}host", value="Hosts a match", inline=False)
    embed.add_field(name=f"{pref}join", value="Joins the match hosted by @HOSTER", inline=False)
    embed.add_field(name=f"{pref}drop OR leave", value="Drops from the match", inline=False)
    embed.add_field(name=f"{pref}forcedrop NUMBER", value="Drops that person from the game if the game is in waiting queue stage", inline=False)
    embed.add_field(name=f"{pref}replace [@PLAYER1] [@PLAYER2]", value="Replaces PLAYER1 with PLAYER2", inline=False)
    embed.add_field(name=f"{pref}cancel", value="Cancels the match ", inline=False)
    embed.add_field(name=f"{pref}blacklist [@PLAYER] [TIME in hours]", value="Blacklist a player", inline=False)
    embed.add_field(name=f"{pref}whitelist [@PLAYER]", value="Removes the blacklist from a player", inline=False)
    embed.add_field(name=f"{pref}blackinfo", value="Will display the info of everyone blacklisted.", inline=False)

    embed.add_field(name=f"{pref}bltime or bltime [PLAYER]", value="See the time left on blacklist", inline=False)
    embed.add_field(name=f"{pref}forcecancel", value="Cancels someone else's match ", inline=False)
    await bot.say(embed=embed)
#token = "NjQ3NzkzNjc1NjkwMzExNjgx.XiXB7A.7KOKOOXMuA9sxeRLmUB6lwqoCqQ"
#token = "NjgzNzQyMjY4NTI3NzM5MDE2.Xlv-oA.YUOmFsg5ncexCvB_76gsYiRRuRY"
#token = "NDMzNjk0NjY5ODMxMTQzNDI1.XjnPhQ.Ml55k4NNt_UiYbMDU_UOGARPqCM"
token = "NzI1NDcxNTg0MDAwNjcxODU0.XvPPww.jIeCnCRlut5Nk4-PDPkb3Bpgdks"
bot.run(token)

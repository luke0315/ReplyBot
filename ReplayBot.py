import asyncio
from turtle import title
import discord
import requests
import os,time
import sys
import logging
from unittest import result
import pymongo
from pymongo.database import Database
import music
import db_controller as db
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
from dotenv import load_dotenv
from random import randint
from video import Video
#client是我們與Discord連結的橋樑
#client = discord.Client()
token = db.find_api_token()
load_dotenv()
prefix="[" 
bot = commands.Bot(command_prefix=prefix)
players = {}
urllist=[]
nowplay=''
@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.command()
async def ping(ctx):
    '''顯示PING'''
    await ctx.send(f'{round(bot.latency*1000)}ms')



@bot.event
#當有訊息時
async def on_message(message):
    lastmessage=''
    if message.author == bot.user:
            return
    #print( message.content[0])
    
    if message.content[0]!= '[':
        #拆分字串
        '''for i in range(0,len(message.content)-1):
            if db.find_keyword_reply(message.content[i]+message.content[i+1]):
                if lastmessage!= db.find_keyword_reply(message.content[i]+message.content[i+1]):
                    lastmessage=db.find_keyword_reply(message.content[i]+message.content[i+1])
                    await message.channel.send(db.find_keyword_reply(message.content[i]+message.content[i+1]))'''
        Replymessage = db.find_keyword(message.content)
        if Replymessage:
                print(Replymessage)
                await message.channel.send(Replymessage)
    await bot.process_commands(message)     
'''async def playlist(ctx, *, list):
        """Plays audio hosted at <url> (or performs a search for <url> and plays the first result)."""
        
         # get the guild's state
        if list=='韓':
            f = open("korean.txt", "r")
            for i in f:
                self.urllist.append(i)
        
        if ctx.author.voice is not None and ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel
            try:
                video = Video(url, ctx.author)
            except youtube_dl.DownloadError as e:
                await ctx.send(
                    "There was an error downloading your video, sorry.")
                return
            client = await channel.connect()
            self._play_song(client, state, video)
            message = await ctx.send("", embed=video.get_embed())
            await self._add_reaction_controls(message)
            logging.info(f"Now playing '{video.title}'")
        else:
            raise commands.CommandError(
                "You need to be in a voice channel to do that.")


        await message.channel.send('趕快下船啦幹')
    if  '完美' in message.content :
        await message.channel.send('Pofee啦')
    if  '遲到' in message.content :
        await message.channel.send('你他媽是黃正美喔')
    if  '你媽死' in message.content or message.content.lower() == 'nmsl':
        await message.channel.send('你的也是 HAHA')
    if  '電話' in message.content and '不接' in message.content :
        await message.channel.send('老子他媽在睡')
    if  '幹你娘' in message.content :
        await message.channel.send('叫爹地')
    if  '香蕉' in message.content :
        
        await message.channel.send('你個芭娜娜')
    if  '放生我' in message.content :
        await message.channel.send('傑鴿到此一遊')
    if  ('西瓜' and '白癡' ) in message.content:
        await message.channel.send('對')
    elif  '西瓜' in message.content :
        await message.channel.send('彥儒甜不甜')
    elif  '白癡' in message.content :
        await message.channel.send('你卡布奇諾嗎?')
    if  '賴俊' in message.content :
        await message.channel.send('馬子狗')
    if  '五月花' in message.content :
        await message.channel.send('衛生紙')
    if  '早上好' in message.content :
        await message.channel.send('我有冰激凌')
    if  '鴨子' in message.content :
        await message.channel.send('嘎嘎')
    if  '好暈' in message.content :
        await message.channel.send('確定是搭船在暈嗎?')
    if  '此船只應天上有' in message.content :
        await message.channel.send('apple暈船逃不走')
    if  '掰掰' in message.content :
        await message.channel.send('要滾快滾 :rage: ')
    if  '傑狗' in message.content :
        await message.channel.send('是隻鳥')
    if  '王八' in message.content :
        await message.channel.send('子傑他爹')
    if  '不要生氣' in message.content :
        await message.channel.send('假如你生氣 仰望耶穌')
    elif  '不要' in message.content :
        await message.channel.send('不要就是要')
    if  '怎麼贏' in message.content :
        await message.channel.send('我想不到怎麼輸')
    if  '派' in message.content :
        await message.channel.send('你想怎樣')
    if  '好菜' in message.content :
        await message.channel.send('子傑更菜')
    if  '綠' in message.content :
        await message.channel.send('你頭上的顏色')
    if  '@' in message.content :    
        
        if '@411812676784619520' in message.content :
            await message.channel.send('什麼時候要變學長')
        elif '@559726386005147668' in message.content :
             await message.channel.send('是可愛的狗狗')
        elif '@559580709992267786' in message.content :
             await message.channel.send('衛生紙')
        elif '@999282729646575637' in message.content :
             await message.channel.send('老子不在')
        else:
            await message.channel.send('那白癡不在')
        
    if  '臭' in message.content :
        await message.channel.send('真的臭死')
        #await message.channel.send(f"Hi, {message.author.mention}!")
    if  '輪迴' in message.content :
        myid = '<@559726386005147668>'
        await message.channel.send(' %s 在這 ' % myid)
        #await message.channel.send(f"Hi, {message.author.mention}!")
    if  '!p' in message.content :
        await message.channel.send('我看起來是點歌的?')
    if  '知道' in message.content :
        await message.channel.send('你又知道了')
    if  '禮貌' in message.content :
        await message.channel.send('人要常說請 謝謝 對不起')
        await message.channel.send(' 對不起我沒帶錢 請我吃飯 謝謝')
    if  '閉嘴' in message.content :
        await message.channel.send('不要')
    if  '你是誰' in message.content :
        await message.channel.send('你親爹')
    if  ('臻' or '真真' or'真牛皮') in message.content :
        await message.channel.send('去洗碗')
    if  message.content == 'eason'.lower() :
        await message.channel.send('sugar daddy')
    
    if  '學弟' in message.content :
        await message.channel.send('你到底什麼時候要買輪迴?')
    if  ('不' and '買') in message.content :
        await message.channel.send('我是你就買了')
    if  '嫩' in message.content :
        await message.channel.send('沒見過比你嫩的')
    if  '中國' in message.content :
        await message.channel.send('支持台獨')
    if  '盆栽要剪' in message.content :
        await message.channel.send('女人要扁')
    if  '笑話' in message.content :
        await message.channel.send('你也是笑話')
    if  '修理' in message.content :
        await message.channel.send('你怎麼不去把你人生修理好')
    if  '三點' in message.content :
        await message.channel.send('吃美味蟹堡囉')
    if  '垃圾' in message.content :
        await message.channel.send('這裡唯一的垃圾只有你')
    if  '楓之谷' in message.content :
        await message.channel.send('這什麼破Game')
    if  '外賣' in message.content :
        await message.channel.send('咖哩拌飯')
    if  '吃什麼' in message.content :
        await message.channel.send('吃自己')'''


         # Initialize the cog and add it to the bot
   
bot.add_cog(music.Music(bot, prefix))     
bot.run(token['token']) #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面 

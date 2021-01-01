# import discord
# import datetime

# #----------------------------------------------------------------------------------------

# token = 'NzMyMTI2ODI0NTM1OTQ5MzMy.XwwFdw.CQU10nHu593OYmj-weFW0YnzCQE'
# client = discord.Client()
# @client.event
# async def on_ready():
#     print('로그인되었습니다!')
#     print(client.user.name)
#     print(client.user.id)
#     print('====================================')
# @client.event
# async def on_message(message):
#     if message.content == '안녕 디봇':
#         embed=discord.Embed(color=0xff00, title=f"안녕하세요 {message.author} 님!  :grinning: ", description="반가워요! :D")
#         await message.channel.send(embed=embed)
    
#     if message.content == '규칙':
#         embed=discord.Embed(color=0xff00, title="규칙 설명 :scales: ", description="1.착한 말|2.성실한 활동|3.재미있는 말                                     이 세가지 규칙만 잘 지키시면 됩니다!", timestamp=message.created_at)
#         await message.channel.send(embed=embed)
#     if message.content == '명령어':
#         embed=discord.Embed(color=0xff00, title="명령어 모음 :tools: ", description="안녕 디봇/굿바이-디봇에게 인사하는 명령어입니다.                                    끝말잇기-당신이 디봇을 이길 수 있을까요?                                       규칙-기본적인 규칙을 서술하는 명령어입니다.                                      내정보-사용자의 닉네임과 ID를 보여줍니다.                                       ", timestamp=message.created_at)
#         await message.channel.send(embed=embed)
#     if message.content == '내정보':
#         user = message.author
#         date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22 ) + 1420070400000) / 1000)
#         await message.channel.send(f"{message.author}님입니다. ")
#     if message.content == '끝말잇기':
#         embed=discord.Embed(color=0xff00, title="흠... 절 이기실 수 있을거라고 생각하신건가요? :thinking: ", description="그럼 저 먼저 시작할게요. 음..... 비브라늄!! :stuck_out_tongue_closed_eyes: ")
#         await message.channel.send(embed=embed)
#     if message.content == '굿바이':
#         embed=discord.Embed(color=0xff00, title=f"바이바이! {message.author} 님!  :grinning: ", description="안녕히 가세요!! :D")
#         await message.channel.send(embed=embed)

# client.run(token)

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

#--------------------------------------------

@bot.event
async def on_ready():
    print(bot.user.name, '봇이 준비되었습니다!')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('ERROR CODE')

@bot.command()
async def test(ctx):
    await ctx.send('test')
@bot.command(aliases=['안녕'])
async def 안녕_디봇(ctx):
    await ctx.send('안녕하세요! ')
@bot.command()
async def 명령어(ctx):
    await ctx.send(embed=discord.Embed(
    title="DI-BOT 명령어 :tools:", 
    description="test, 안녕 디봇, 명령어, 규칙, 핑", 
    color=discord.Colour.green()))
@bot.command()
async def 규칙(ctx):
    await ctx.send(embed=discord.Embed(
    title="규칙 :scales:", 
    description="1. 욕설 금지. 2. 화목한 대화. 3.재미있는 채팅. ", 
    color=discord.Colour.greyple()))

@bot.command()
async def egg(ctx):
    await ctx.send('(대충 이스티에그) (로봇 기침).')

@bot.command()
async def 이뭐병(ctx):
    await ctx.send('이건 뭐 ㅄ도 아니고')

@bot.command()
async def info(ctx):
    await ctx.send('bot info : DI-BOT 2.0/bot accounts : DI-BOT 2.0#4062/ token : NzMyMTI2ODI0NTM1OTQ5MzMy.XwwFdw.CQU10nHu593OYmj-weFW0YnzCQE ')

@bot.command()
async def 핑(ctx):
    await ctx.send(f'퐁! / 현재 핑 : {round(bot.latency * 1000)}ms')

@bot.command(aliases=['ㅁㄴㅇㄹ', 'asdfasdf'])
async def asdf(ctx):
    await ctx.send('ㅁㄴㅇㄹ asdf asdfasdf')




#------------------------------------------------------------------------
bot.run('NzMyMTI2ODI0NTM1OTQ5MzMy.XwwEPQ.Udwua3YcXPYhrBMfiEg1kr5-_7w')
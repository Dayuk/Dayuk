import discord
import urllib.request
import requests
from bs4 import BeautifulSoup

if not discord.opus.is_loaded():
     discord.opus.load_opus('opus')
     
app = discord.Client()

token = 'NjAzNjQ5NTAxOTE5NzA3MTU2.XbkrXg.x_JBM_hWyHr-7qMq8rZOPMQxILc'

@app.event
async def on_ready():
    print(app.user.name)
    print(app.user.id)


@app.event
async def on_message(message):
    if message.author.bot:
        return None

        abc = 'abcdefg'
        test = str(abc)[1:5]
        print (test)
        

    if message.content.startswith('!롤'):
        #Name = message.content.split(" ")
        #Name1 = Name[1]
        #location = message.content[3:len(message.content)]

        Name = message.content[3:len(message.content)]

        req = requests.get('http://op.gg/summoner/userName='+Name)
        html = req.text
        soup = BeautifulSoup (html, 'html.parser')
        

        ####################### 닉네임 부분 ###################################

        Name1 = soup.find_all('span', {'class': 'Name'})
        Name2 = str(Name1[0])[str(Name1[0]).find('me">') +4:str(Name1[0]).find('</span>')]
        print(Name2)

        ####################### 프로필 인장 부분 ##############################

        Image1 = soup.find_all('div', {'class': 'borderImage'})
        Image2 = str(Image1[0])[str(Image1[0]).find('img">') +4:str(Image1[0]).find('</div>')]
        print(Image2)

        ####################### 모스트 부분 ###################################

        Most1 = soup.find_all('div', {'class': "ChampionInfo"})
        Most2 = str(Most1[0])[str(Most1[0]).find('nt">') +4:str(Most1[0]).find('</div>')] ##손질중##
        print(Most2)


        
        ######################### 랭크 부분 #########################
        
        Rank1 = soup.find_all('div', {'class': 'TierRank'})
        Rank2 = str(Rank1[0])[str(Rank1[0]).find('nk">') +4:str(Rank1[0]).find('</div>')]
        print(Rank2)

        ######################### 점수 부분 #########################
        
        LP1 = soup.find_all('span', {'class': 'LeaguePoints'})
        LP2 = str(LP1[0])[str(LP1[0]).find('">')+2 :str(LP1[0]).find('</sp')]
        LP3 = LP2.strip()
        print(LP3)
        
        ######################### 승리,패배,승률 부분#########################
        
        win1 = soup.find_all('span', {'class': 'WinLose'})
        win2 = str(win1[0])[str(win1[0]).find('ns">') + 4:str(win1[0]).find('</sp')]
        print(win2)
                              
        lose1 = soup.find_all('span', {'class': 'losses'})
        lose2 = str(lose1[0])[str(lose1[0]).find('es">') + 4:str(lose1[0]).find('</sp')]
        print(lose2)

        ratio1 = soup.find_all('span', {'class': 'winratio'})
        ratio2 = str(ratio1[0])[str(ratio1[0]).find('io">') + 4:str(ratio1[0]).find('</sp')]
        print(ratio2)

        ###########################가장 최근 전적##################################

        Game1 = soup.find_all('div', {'class': 'GameType'})
        Game2 = str(Game1[0])[str(Game1[0]).find('ga">') + 4:str(Game1[0]).find('</div')]
        print(Game2)

        Result1 = soup.find_all('div', {'class': 'GameResult'})
        Result2 = str(Result1[0])[str(Result1[0]).find('lt">') + 4:str(Result1[0]).find('</div')]
        print(Result2)

        ########################## 총 정리 ######################################

        
        Image3 = Image2.replace('  ','  ')
        Result3 = Result2.replace('GameResult',' ')
        Game3 = Game2.replace('GameType','게임종류')
        win3 = win2.replace('W','승')
        lose3 = lose2.replace('L','패')
        ratio3 = ratio2. replace('Win Ratio', '승률')
        Rank3 = Rank2. replace('TierRank', '티어')
        LP4 = LP3. replace('LeaguePoints', 'LP')
        Most3 = Most2. replace('ChampionInfo', 'Most')
        Name3 = Name2. replace('Name', '닉네임')
        print(win3+'/'+lose3+'/'+ratio3)

       ############################출력부분######################################
     
        embed = discord.Embed(title="LOL 전적검색", description=
                              '닉네임: '+Name3+'\n'
                              '\n'
                              '솔랭티어: '+Rank3+ ' /'+LP4+' \n'
                              '승,패:'+win3+' / '+lose3+' / '+ratio3, color=0x00ff00)
        embed.set_image(url="https://img1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/liveboard/mk/e36b876b022443239474b7e1675875cf.jpg")
        await message.channel.send(embed=embed)

        #############################디스코드 부분######################

    if message.content.startswith ("!스크림추가"):
        embed4 = discord.Embed(title="--------양식--------", description="팀명:\n날짜:\n시간(0~23시):\n팀 평균티어:\n팀장 롤닉네임:\n팀장 디스코드 닉네임:\n(*꼭 양식을 포함하여 적어주세요*)", color=0x00ff00)
        await app.send_message(message.channel, embed=embed4)
                               
    if message.content.startswith ("팀명:"):
       embed2 = discord.Embed(title="일정추가가 완료되었습니다.", description="본인의 팀과 경기를 희망하는 팀 혹은 관리자의 연락이 갈 수 있습니다.", color=0xFF0000)
       await message.channel.send(embed=embed2)
       await app.get_channel(int(689935648098091174)).send(message.content)


    if message.content.startswith ("!신고"):
       embed5 = discord.Embed(title="--------양식--------", description="!가해자 닉네임: \n 신고사유: \n 신고자 닉네임: \n (양식을 꼭 포함하여 적어주세요.)", color=0xFF0000)
       await message.channel.send(embed=embed5)
       await message.delete()
                               
    if message.content.startswith ("!가해자"):
       embed13 = discord.Embed(title="신고가 완료되었습니다.", description="관리자에게서 연락이 가실 수 있습니다.", color=0xFF0000)
       await message.channel.send(embed=embed13)
       await app.get_channel(int(689936339696877568)).send(message.content)
       await message.delete()


    if message.content.startswith ("!채널생성"):
        embed6 = discord.Embed(title="채널이 생성되었습니다.", description="채널명과 설정을 변경해주세요.", color=0xFF0000)
        await message.channel.send(embed=embed6)
        await guild_voice.add[
                              "id": "660213767820410908",
                              "guild_id": "660213767820410908",
                              "name": "ROCKET CHEESE",
                              "type": 2,
                              "nsfw": false,
                              "position": 5,
                              "permission_overwrites": [],
                              "bitrate": 64000,
                              "user_limit": 0,
                              "parent_id": null
                            ]


app.run('NjYwMjE0NjU2Njg1NTcyMTA2.XgZm4A.eABoudppFj-w31OsX34U6AmhZSw')



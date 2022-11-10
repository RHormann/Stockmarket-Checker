import requests
import champIds
import key

#Get the summoner name and using that to get the encrypted ID as we need that to do most things
summonerName = input("Enter your summoner name: ")
summonerInfo = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={key.key}"
SIresponse = requests.get(summonerInfo)
summonerInfoMap = SIresponse.json()
icon = summonerInfoMap["profileIconId"]
level = summonerInfoMap["summonerLevel"]
encryptedId = summonerInfoMap["id"]
puuId = summonerInfoMap["puuid"]

#Champion Mastery
masteryStats = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}/top?count=3&api_key={key.key}"
MSresponse = requests.get(masteryStats)
masteryStatsMap = MSresponse.json()

#Ranked stats of the player
rankedStats = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{encryptedId}?api_key={key.key}"
RSresponse = requests.get(rankedStats)
rankedStatsMap = RSresponse.json()
rankedStatsDic = rankedStatsMap[1]
queue = rankedStatsDic["queueType"]
tier = rankedStatsDic["tier"]
rank = rankedStatsDic["rank"]
lp = rankedStatsDic["leaguePoints"]
leagueId = rankedStatsDic["leagueId"]

#Ranked stats in more detail
rankedStatsMD = f"https://euw1.api.riotgames.com/lol/league/v4/leagues/{leagueId}?api_key={key.key}"


#Store all the above data in a class for easy access
class summonerData:
    def __init__(self, iconId, levelId, summonerName):
        self.iconID = iconId
        self.levelId = levelId
        self.summonerName = summonerName
    
    def getName(self):
        return self.summonerName

    def getIcon(self):
        return self.iconID

    def getLevel(self):
        return self.levelId
    
    def getRankedStats(self):
        print(f"    {queue}: {tier} {rank}")
        if lp == 100:
            pass
    
    #i cant figure out how to convert UNIX time to a readble time so have to come back to this, date time did not seem to work
    def getTopChamps(self, masteryStatsMap):
        for i in masteryStatsMap:
            champid = i["championId"]
            champ = champIds.getChampionId(champid)
            points = str(i["championPoints"])
            lastPlayed = i["lastPlayTime"]
            print(f"    {champ}: {points} Mastery Points")
            print(f"    Last played: {lastPlayed}\n")
    
    def getMatchHistory(self):
        pass

User = summonerData(icon, level, summonerName)
#the way the information will be displayed in the terminal, can choose to only display certain sections
class printFormat:
    def __init__(self) -> None:
        pass

    def getBasicInfo(self):
        print(f"\n{User.getName()}:")
        print(f"    Icon: {User.getIcon()}")
        print(f"    Summoner Level: {User.getLevel()}")
    
    def getChampionMasteryInfo(self):
        print(f"\nChampion Mastery:")
        print(f"{User.getTopChamps(masteryStatsMap)}")

    def getRankedInfo(self):
        print("\nRanked Stats:")
        User.getRankedStats()

    def getAll(self):
        self.getBasicInfo()
        self.getChampionMasteryInfo()
        self.getRankedInfo()

display = printFormat()

display.getAll()
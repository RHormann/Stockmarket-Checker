import requests
import champIds

#Get the summoner name and using that to get the encrypted ID as we need that to do most things
summonerName = input("Enter your summoner name: ")
api_key = "RGAPI-774b5cf4-4fea-44fd-b04f-08f30ede74d3"
summonerInfo = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={api_key}"
SIresponse = requests.get(summonerInfo)
summonerInfoMap = SIresponse.json()
icon = summonerInfoMap["profileIconId"]
level= summonerInfoMap["summonerLevel"]
encryptedId = summonerInfoMap["id"]
puuId = summonerInfoMap["puuid"]

#Champion Mastery
masteryStats = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}/top?count=3&api_key={api_key}"
MSresponse = requests.get(masteryStats)
masteryStatsMap = MSresponse.json()

#Ranked stats of the player
rankedStats = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{encryptedId}?api_key={api_key}"


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
        pass
    
    def getTopChamps(self, masteryStatsMap):
        for i in masteryStatsMap:
            champid = i["championId"]
            champ = champIds.getChampionId(champid)
            points = str(i["championPoints"])
            lastPlayed = str(i["lastPlayTime"])
            print(f"    {champ}: {points} Mastery Points")
            print(f"    Last played: {lastPlayed}\n")
    
    def getMatchHistory(self):
        pass

User = summonerData(icon, level, summonerName)
print("")
print(f"{User.getName()}:")
print(f"    Icon --> {User.getIcon()}")
print(f"    Summoner Level --> {User.getLevel()}")
print(f"\nChampion Mastery:")
print(f"{User.getTopChamps(masteryStatsMap)}")
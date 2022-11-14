import requests
import champIds
import key

class Global:

    #init all the api requests and the encrypted ID
    def __init__(self,summonerName):
        self.summonerName = summonerName
        self.summonerInfo = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={key.key}"
        SIresponse = requests.get(self.summonerInfo)
        self.summonerInfoMap = SIresponse.json()
        self.encryptedId = self.summonerInfoMap["id"]
        self.masteryStats = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{self.encryptedId}/top?count=3&api_key={key.key}"
        self.rankedStats = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.encryptedId}?api_key={key.key}"

    #returns info in a dictionary format 
    def getBasic(self):
        return {
            "username": self.summonerName,
            "icon":self.summonerInfoMap["profileIconId"],
            "level":self.summonerInfoMap["summonerLevel"]
        }

    #Returns top 3 champs as seperate dictionaries in a list 
    #removed some of the data from the original which is why i dont just return the original list
    def getMastery(self):
        MSresponse = requests.get(self.masteryStats)
        masteryStatsList = MSresponse.json()
        newMastery = []
        for i in masteryStatsList:
            champid = i["championId"]
            champ = champIds.getChampionId(champid)
            points = str(i["championPoints"])
            lastPlayed = i["lastPlayTime"]
            newDict = {
                "Champion Name": champ,
                "Mastery Points": points,
                "Last Played": lastPlayed
            }
            newMastery.append(newDict)
        return newMastery

    #returns ranked stats, could get more info on them but i cba and want to move on with the project so will come back to it
    def getRanked(self):
        RSresponse = requests.get(self.rankedStats)
        rankedStatsMap = RSresponse.json()
        rankedStatsDic = rankedStatsMap[0] #depending on the integer a different rank will come up, eg: flex, tft, solo/duo, should impliment a try method so if error comes UNRANKED should show
        queue = rankedStatsDic["queueType"]
        tier = rankedStatsDic["tier"]
        rank = rankedStatsDic["rank"]
        lp = rankedStatsDic["leaguePoints"]
        return {
            "Queue": queue,
            "Rank": tier,
            "Tier": rank,
            "lp": lp
        }


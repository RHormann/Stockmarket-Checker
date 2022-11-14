import Server
def main():
    summonerName = input("Enter Summoner Name: ").lower()
    user = Server.Global(summonerName)
    userdict = user.getRanked()
    print(userdict)


if __name__ == '__main__':
    main()
import mysql.connector 
import requests
import json
import re 


def jprint(obj):
    #creation of formatted string output 
    text = json.dumps(obj, sort_keys=True, indent = 3) 
    print(text)


createTable = """ 
                 CREATE TABLE IF NOT EXISTS `nhl_players` 
                (`key` INT NOT NULL AUTO_INCREMENT,
                    `activePlayer` BOOLEAN NULL, 
                    `assists` INT NULL, 
                    `firstName` VARCHAR(255) NULL, 
                    `franchiseId` INT NULL, 
                    `franchiseName` VARCHAR(255) NULL,
                    `gameTypeId` INT NULL, 
                    `gamesPlayed` INT NULL, 
                    `goals` INT NULL, 
                    `id` INT NULL, 
                    `lastName` VARCHAR(100) NULL, 
                    `mostAssistsGameDates` LONGTEXT NULL ,
                    `mostAssistsOneGame` INT NULL,
                    `mostAssistsOneSeason` INT NULL,
                    `mostAssistsSeasonIds` LONGTEXT NULL,
                    `mostGoalsGameDates` LONGTEXT NULL,
                    `mostGoalsOneGame` INT NULL,
                    `mostGoalsOneSeason` INT NULL,
                    `mostGoalsSeasonIds` LONGTEXT NULL,
                    `mostPenaltyMinutesOneSeason` INT NULL,
                    `mostPenaltyMinutesSeasonIds` LONGTEXT NULL,
                    `mostPointsGameDates` LONGTEXT NULL,
                    `mostPointsOneGame` INT NULL,
                    `mostPointsOneSeason` INT NULL,
                    `mostPointsSeasonIds` LONGTEXT NULL,
                    `penaltyMinutes` INT NULL,
                    `playerId` INT NULL,
                    `points` INT NULL,
                    `positionCode`  VARCHAR(100) NULL,
                    `rookiePoints` INT NULL,
                    `seasons` INT NULL, 
                    PRIMARY KEY (`key`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
                ;

              """

sqlInsert = """ INSERT INTO `nhl_players` (
                            `activePlayer`, 
                            `assists`, 
                            `firstName`, 
                            `franchiseId`, 
                            `franchiseName`,
                            `gameTypeId`, 
                            `gamesPlayed`, 
                            `goals`, 
                            `id`, 
                            `lastName`, 
                            `mostAssistsGameDates`,
                            `mostAssistsOneGame`,
                            `mostAssistsOneSeason`,
                            `mostAssistsSeasonIds`,
                            `mostGoalsGameDates`,
                            `mostGoalsOneGame`,
                            `mostGoalsOneSeason`,
                            `mostGoalsSeasonIds`,
                            `mostPenaltyMinutesOneSeason`,
                            `mostPenaltyMinutesSeasonIds`,
                            `mostPointsGameDates`,
                            `mostPointsOneGame`,
                            `mostPointsOneSeason`,
                            `mostPointsSeasonIds`,
                            `penaltyMinutes`,
                            `playerId`,
                            `points`,
                            `positionCode`,
                            `rookiePoints`,
                            `seasons`)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""


#######SETTING UP THE JSON data 
team = 38
PARAMS = {"franchiseId" : team}
URL = "https://records.nhl.com/site/api/franchise-skater-records"
print("Getting the data from the API")
response = requests.get(url=URL, params = PARAMS)
data = response.json()

####### DB CONNECTION
print("connecting to DB.....") 
mydb = mysql.connector.connect(
        host="localhost", 
        user='cklaroche',
        password="6166677525",
        database="cklaroche")

mycursor = mydb.cursor()
mycursor.execute(createTable) 
print("sent createTable statement")


print("Inserting Json Data") 

for item in data["data"]:
    val = (item.get("activePLayer"),item.get("assists"), item.get("firstName"), item.get("franchiseId"),item.get("franchiseName"),item.get("gameTypeId"),item.get("gamesPlayed"),item.get("goals"),item.get("id"),item.get("lastName"),item.get("mostAssistsGameDates"),item.get("mostAssistsOneGame"),item.get("mostAssistsOneSeason"),item.get("mostAssistsSeasonIds"),item.get("mostGoalsGameDates"),item.get("mostGoalsOneGame"), item.get("mostGolasOneSeason"),item.get("mostGoalsSeasonIds"),item.get("mostPenaltyMinutesOneSeason"), item.get("mostPenaltyMinutesSeasonIds"),item.get("mostGameDates"),item.get("mostPointsOneGame"),item.get("mostPointsOneSeason"),item.get("mostPointsSeasonIds"), item.get("penaltyMinutes"), item.get("playerId"), item.get("points"), item.get("positionCode"), item.get("rookiePoints"), item.get("seasons"))
    mycursor.execute(sqlInsert, val)
mydb.commit()

print("complete") 



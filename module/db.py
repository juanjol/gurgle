import mysql.connector
from config import Config
from cache import IsNotInCache, CacheUpdate

_LOGGER = Config.getLogger("db")


mydb = mysql.connector.connect(
  host=Config.getRequiredString('db', 'host'),
  user=Config.getRequiredString('db', 'user'),
  password=Config.getRequiredString('db', 'password'),
  database=Config.getRequiredString('db', 'database'),
)

def PostUpdate(update, factionList):
    """Responsible for sending the specified update to the Database."""
    starName = update["StarSystem"]
    eventDate = update["EventDate"]
    distance = update["Distance"]
    # Send the update, if Cache says we need to
    if IsNotInCache(eventDate, starName, factionList):
        if SendUpdate(update):
            _LOGGER.info("Processed (sent) update for %s (%.1fly)", starName, distance)
            # Update the Cache Entry (after send so we have definitely sent)
            CacheUpdate(eventDate, starName, factionList)
        else:
            _LOGGER.warning("Failed to send update for %s (%.1fly)", starName, distance)
    else:
        _LOGGER.debug("Processed (not sent) update for %s (%.1fly)", starName, distance)


def SendUpdate(dictionary):    
    dictionary['Timestamp'] = dictionary['Timestamp'][0:10] + ' ' + dictionary['Timestamp'][11:19]

    mycursor = mydb.cursor()
    columns = ['Timestamp', 'EventDate', 'EventTime', 'StarSystem', 'Distance', 'SystemSecurity', 'SystemAllegiance', 'SystemGovernment', 'SystemEconomy', 'Faction1Name', 'Faction1Influence', 'Faction1State', 'Faction1PendingState', 'Faction1RecoveringState', 'Faction2Name', 'Faction2Influence', 'Faction2State', 'Faction2PendingState', 'Faction2RecoveringState', 'Faction3Name', 'Faction3Influence', 'Faction3State', 'Faction3PendingState', 'Faction3RecoveringState', 'Faction4Name', 'Faction4Influence', 'Faction4State', 'Faction4PendingState', 'Faction4RecoveringState', 'Faction5Name', 'Faction5Influence', 'Faction5State', 'Faction5PendingState', 'Faction5RecoveringState', 'Faction6Name', 'Faction6Influence', 'Faction6State', 'Faction6PendingState', 'Faction6RecoveringState', 'Faction7Name', 'Faction7Influence', 'Faction7State', 'Faction7PendingState', 'Faction7RecoveringState', 'Faction8Name', 'Faction8Influence', 'Faction8State', 'Faction8PendingState', 'Faction8RecoveringState', 'Faction9Name', 'Faction9Influence', 'Faction9State', 'Faction9PendingState', 'Faction9RecoveringState', 'Faction10Name', 'Faction10Influence', 'Faction10State', 'Faction10PendingState', 'Faction10RecoveringState']
    sql = "INSERT INTO influence (`Timestamp`, `EventDate`, `EventTime`, `StarSystem`, `Distance`, `SystemSecurity`, `SystemAllegiance`, `SystemGovernment`, `SystemEconomy`, `Faction1Name`, `Faction1Influence`, `Faction1State`, `Faction1PendingState`, `Faction1RecoveringState`, `Faction2Name`, `Faction2Influence`, `Faction2State`, `Faction2PendingState`, `Faction2RecoveringState`, `Faction3Name`, `Faction3Influence`, `Faction3State`, `Faction3PendingState`, `Faction3RecoveringState`, `Faction4Name`, `Faction4Influence`, `Faction4State`, `Faction4PendingState`, `Faction4RecoveringState`, `Faction5Name`, `Faction5Influence`, `Faction5State`, `Faction5PendingState`, `Faction5RecoveringState`, `Faction6Name`, `Faction6Influence`, `Faction6State`, `Faction6PendingState`, `Faction6RecoveringState`, `Faction7Name`, `Faction7Influence`, `Faction7State`, `Faction7PendingState`, `Faction7RecoveringState`, `Faction8Name`, `Faction8Influence`, `Faction8State`, `Faction8PendingState`, `Faction8RecoveringState`, `Faction9Name`, `Faction9Influence`, `Faction9State`, `Faction9PendingState`, `Faction9RecoveringState`, `Faction10Name`, `Faction10Influence`, `Faction10State`, `Faction10PendingState`, `Faction10RecoveringState`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = [] 
    for v in columns:
        if v in dictionary and dictionary[v] != 'NULL':          
            values.append(dictionary[v])
        else:
            find = 0
            for i in range(1,11):
                # _LOGGER.info(v)
                # _LOGGER.info(['Faction' + str(i) + 'Influence'])
                if v== 'Faction' + str(i) + 'Influence':
                    values.append(.0)
                    find = 1                
            if find == 0:
                values.append('NULL')
    values = tuple(values)
    # _LOGGER.info(values)
    # _LOGGER.info(sql)
    try:
        mycursor.execute(sql, tuple(values))
        mydb.commit()
    except Exception, e:
        _LOGGER.info("(DB) Exception while attempting to INSERT data: %s", str(e))
    _LOGGER.info("%s Record Inserted", mycursor.rowcount)
    return True

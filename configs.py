# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "12658994"))
    API_HASH = getenv("API_HASH", "588df9088e18efcac76ba0d6e5769fd8")
    BOT_TOKEN = getenv("BOT_TOKEN", "6000438454:AAGGV5wcmmmZBnAY4cfNJWo-WjTr3DXrdmw")
    FSUB = getenv("FSUB", "Film_Nest")
    CHID = int(getenv("CHID", "-1001912762300"))
    SUDO = list(map(int, getenv("SUDO", "1663603208").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://anmol:anmol@cluster0.0efdinm.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

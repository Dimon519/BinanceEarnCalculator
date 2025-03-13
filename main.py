from binance.spot import Spot
from datetime import datetime, timezone
from decimal import Decimal
import pyperclip

def EarnCalculate(settings, params):
    if not settings.api_key or not settings.api_secret:
        return [False, "Not set keys or keys is bad"]
    summEarn = 0
    asset, type, typeRewards = params[0], params[3], params[4]
    startTime = (int(datetime.strptime(params[1], "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp()) * 1000)
    endTime = (int(datetime.strptime(params[2], "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp()) * 1000) + 86400000

    client = Spot(api_key= settings.api_key, api_secret= settings.api_secret)

    params = {
        'asset': asset,
        'size': 100,
        'startTime': startTime,
        'endTime' : endTime,
        'type': typeRewards
    }

    if type == 'Flexible':
        responce = client.get_flexible_rewards_history(**params)
        for rsp in responce['rows']:
            summEarn += Decimal(rsp['rewards'])
    
    if type == 'Locked':
        responce = client.get_locked_rewards_history(**params)
        for rsp in responce['rows']:
            summEarn += Decimal(rsp['amount'])

    settings.profit = summEarn
    return [True, str(summEarn)]

def CopyCalculateResult(settings):
    if settings.auto_convert:
        pyperclip.copy(str(settings.profit).replace(".",","))
    else:
        pyperclip.copy(settings.profit)
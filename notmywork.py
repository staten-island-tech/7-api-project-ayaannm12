import sys
from apex_legends_api import ApexLegendsAPI,\
    ALPlatform,\
    ALPlayer,\
    ALAction,\
    A​L​H​T​TPExcеptionFromResponse​
from​ apex_legends_api.al_base import print_description

api = ApexLegendsAPI(api_key='<api_key>')

player_name = str("PlayеrName")
player_uid = str("1234567890")
platform = ALPlatf​orm.PC
action = ALAction.GET

# Example 1:
# straight API calls
try:
    basic = api.basic_pl​ayer_stats(player_name=player_name, platform=platform)
    # or query by UID
    # basic = api.basic_player_stats_by_uid(uid=player_uid, platform=platform)
    history = api.events(player_name​=player_name, platform=platform, action=action)
    origin_player = api.get_playеr_ori​gin(player_name=player_name, show_all_hits=True)
except ALHTTPExceptionFromResponse as e​xcept​ion:
    print(exception)
    sys.exit()
KEEP USING AI MAN
print(basic)
print(his​tory)
print(origin_player)

# Example 2:
# retrieve an 'ALPlayer' object
player: ALPlayer = api.get_player(name=player_name, platform=platform)
print_description(player)


#none of this is mine im js reviewing it, IT IS NOT MY WORK.


import requests
import json
from datetime import datetime

from match import Match
from text_living import TextLiving


Living_Matches_Url = 'http://bifen4m.qiumibao.com/json/list.htm'

Match_Max_Sid_Url = 'http://dingshi4pc.qiumibao.com/livetext/data/cache/max_sid/%s/0.htm'
Match_Living_Text_Url = 'http://dingshi4pc.qiumibao.com/livetext/data/cache/livetext/%s/0/lit_page_2/%d.htm'
Match_Info_Url = 'http://bifen4pc2.qiumibao.com/json/%s/%s.htm'


def get_living_matches():
    response = requests.get(Living_Matches_Url)
    result = json.loads(response.text)
    matches = [Match(**match) for match in result['list'] if match['type'] == 'basketball' and match['period_cn'] != '完赛']
    # matches = [Match(**match) for match in result['list'] if match['period_cn'] != '完赛']
    return matches


def get_match_max_sid(match_id):
    response = requests.get(Match_Max_Sid_Url % match_id)
    if response.status_code == requests.codes.ok:
        return int(response.text)


def get_match_living(match_id, max_sid):
    match_info = get_match_info(match_id)

    response = requests.get(Match_Living_Text_Url % (match_id, max_sid))

    texts = []
    if response.status_code == requests.codes.ok:
        result = json.loads(response.text)
        texts = [TextLiving(match_info, **living) for living in result]
    return texts


def get_match_info(match_id):
    today = datetime.now().strftime('%Y-%m-%d')
    response = requests.get(Match_Info_Url % (today, match_id))
    match_info = json.loads(response.text)
    return match_info
        
        

import zhibo8_api


def get_living_matches():
    matches = zhibo8_api.get_living_matches()
    for match in matches:
        print(match)
    return matches


def get_watch_match(matches):
    match_id = input('请输入比赛ID：')
    for match in matches:
        if match.id == match_id:
            return match
    else:
        print('输入的ID不正确')
        return None


def main_loop():
    matches = get_living_matches()
    if len(matches) == 0:
        print('当前没有比赛！！！')
        return

    match = get_watch_match(matches)
    if not match:
        print('没去找到该比赛')
        return

    current_match_max_sid = -1
    while True:
        match_max_sid = zhibo8_api.get_match_max_sid(match.id)
        if not match_max_sid:
            print('没有直播数据')
            return
            
        if current_match_max_sid == match_max_sid:
            continue

        current_match_max_sid = match_max_sid
        text_livings = zhibo8_api.get_match_living(match.id, current_match_max_sid)
        for text in text_livings:
            print(text)


if __name__ == '__main__':
    main_loop()
    
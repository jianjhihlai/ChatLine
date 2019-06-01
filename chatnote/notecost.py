import re
from chatnote.account import *

class NoteCost:

    def __init__(self, text, userid):
        self.text = text
        self.userid = userid
        self.op = self.parse(text)

    # 買[東西] 花[數字]元 在[地點]
    # 在那裡買[東西]
    # 這個月花多少錢
    # 上個月花多少錢
    # 買[東西]花多少錢
    def parse(self, text):
        pattern = re.compile("(?<=買)(.+)花多少錢")
        found = pattern.search(text)
        if found is not None:
            return ItemCost(found.group(1))

        pattern = re.compile("(.+月)花多少錢")
        found = pattern.search(text)
        if found is not None:
            return TimeCost(found.group(1))

        pattern = re.compile("那裡買(.+)")
        found = pattern.search(text)
        if found is not None:
            return ItemWhere(found.group(1))

        pattern_cost = re.compile(r"花(\d+)")
        pattern_where = re.compile(r"在(\S+)")
        pattern_item = re.compile(r"買(\S+)")
        pattern_list = [pattern_where, pattern_item, pattern_cost]

        found = []
        for pattern in pattern_list:
            find = pattern.search(text)
            if find is None:
                found.append(None)
            else:
                found.append(find.group(1))

        if found[1] is not None and found[2] is not None:
            return CostNote(found)

        return AimlNote(text, self.userid)

    def response(self):
        return self.op.response()
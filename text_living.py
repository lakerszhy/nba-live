

class TextLiving:

    def __init__(self, match_info, **kwargs):
        self.home_team = match_info['home_team']
        self.visit_team = match_info['visit_team']
        self.period_cn = match_info['period_cn']

        self.live_text = kwargs['live_text']
        self.home_score = kwargs['home_score']
        self.visit_score = kwargs['visit_score']


    def __repr__(self):
        return '{self.home_team} {self.home_score} - {self.visit_score} {self.visit_team} {self.period_cn}\n{self.live_text}\n{sep}'\
            .format(self=self, sep='*'*60)


class Match:

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.home_team = kwargs['home_team']
        self.visit_team = kwargs['visit_team']
        self.home_score = kwargs['home_score']
        self.visit_score = kwargs['visit_score']
        self.period_cn = kwargs['period_cn'].replace('\n', ' ')


    def __repr__(self):
        return '{self.id} {self.home_team} {self.home_score} - {self.visit_score} {self.visit_team} {self.period_cn}'\
            .format(self=self)
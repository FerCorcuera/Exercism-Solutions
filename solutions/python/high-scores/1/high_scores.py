class HighScores:
    """
    This class recieves a list of scores and outputs three things:
    1. the full list of scores
    2. the latest score
    3. the top three scores
    """
    
    def __init__(self, scores):

        self.scores = scores


    def scores(self):

        return self.scores

    def latest(self):

        return self.scores[-1]

    def personal_best(self):

        return max(self.scores)

    def personal_top_three(self):

        srt = sorted(self.scores)
        
        return sorted(srt[-3:], reverse = True)

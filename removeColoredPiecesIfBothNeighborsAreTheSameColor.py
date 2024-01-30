class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        # count how many turns can come from each grouping of "A" or "B" with neighbors - person with least amount of removals win
        # account for case where pieces cannot be removed from edge 
        i = 0
        curr = 0
        match = 0
        n = len(colors)
        turn_dic = {"A": 0, "B" : 0}
        # iterate through colors and count times A or B is able to be removed
        while (i < n-1):
            # 1 turn = 1 piece b/t neighbors, ie. 3 matching pieces
            if (colors[i] == colors[i+1]):
                curr = i + 2
                while (curr < n) and (colors[i] == colors[curr]):
                    match += 1
                    curr += 1
                # match = num of turns for person, curr = index to continue iterating from
                turn_dic[colors[i]] += match
                i = curr - 1
                match = 0
            i += 1
        # lower turns is the loser
        if (turn_dic['A'] == turn_dic['B']):
            # Alice moves first - if alice has no moves, she looses
            return False
        elif (turn_dic['A'] > turn_dic['B']):
            return True
        elif (turn_dic['A'] < turn_dic['B']):
            return False
        

        

        

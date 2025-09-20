class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        # pre-process
        L = min(3, n)

        # helper function
        def flip(bit):
            if bit == "0":
                return "1"
            elif bit == "1":
                return "0"

        def switch(state):
            states = set()
            # button 1, 2, 3, 4
            new_state = ""
            new_state2 = ""
            new_state3 = ""
            new_state4 = ""

            for x in range(L):
                new_state += flip(state[x])
                if x == 0:
                    new_state4 += flip(state[x])
                else:
                    new_state4 += state[x]

                if x % 2 == 1:
                    new_state2 += flip(state[x])
                    new_state3 += state[x]
                else:
                    new_state2 += state[x]
                    new_state3 += flip(state[x])

            states.add(new_state)
            states.add(new_state2)
            states.add(new_state3)
            states.add(new_state4)
            return states

        # process
        states = set()
        state = "0" * L
        states.add(state)
        for _ in range(presses):
            new_states = set()
            for state in states:
                new_states.update(switch(state))
            states = new_states

        ans = len(states)
        return ans


n = 1
presses = 1

n = 2
presses = 1

n = 3
presses = 1

"""
n = 7
presses = 1000
"""

solution = Solution()
print(solution.flipLights(n, presses))

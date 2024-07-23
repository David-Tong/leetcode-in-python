import string


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def parseFormula(formula):
            # easy to process
            formula += "Z"
            # process
            from collections import defaultdict
            elements = defaultdict(int)
            start_element = -1
            start_digit = -1
            for idx, ch in enumerate(formula):
                if ch in string.ascii_uppercase:
                    if start_element != -1:
                        # no digits follow case
                        if start_digit == -1:
                            element = formula[start_element:idx]
                            count = 1
                        else:
                            element = formula[start_element:start_digit]
                            count = int(formula[start_digit:idx])
                        elements[element] += count
                    start_element = idx
                    start_digit = -1
                elif ch in string.digits:
                    if start_digit == -1:
                        start_digit = idx
            return elements

        def merge(elements, elements2):
            for element2 in elements2:
                elements[element2] += elements2[element2]
            return elements

        def doCount(formula):
            L = len(formula)
            from collections import defaultdict
            elements = defaultdict(int)
            idx = 0
            stacks = 0
            start = 0
            while idx < L:
                if formula[idx] == "(":
                    stacks += 1
                    if stacks == 1:
                        new_elements = parseFormula(formula[start:idx])
                        merge(elements, new_elements)
                        start = idx + 1
                elif formula[idx] == ")":
                    stacks -= 1
                    if stacks == 0:
                        new_elements = doCount(formula[start:idx])
                        idx2 = idx + 1
                        start = idx2
                        while idx2 < L:
                            if formula[idx2] not in string.digits:
                                break
                            idx2 += 1
                        if idx2 == idx + 1:
                            count = 1
                        else:
                            count = int(formula[idx+1:idx2])
                        idx = idx2 - 1

                        for key in new_elements:
                            new_elements[key] *= count
                        merge(elements, new_elements)
                idx += 1

            new_elements = parseFormula(formula[start:])
            merge(elements, new_elements)

            return elements

        elements = doCount(formula)

        # post-process
        ans = ""
        for element in sorted(elements.keys()):
            count = elements[element]
            if count > 1:
                ans += element + str(count)
            else:
                ans += element
        return ans


formula = "H2O"
formula = "HO2H3So3MgSo7"
formula = "Mg(OH)2"
formula = "K4(ON(SO3)2)2"
formula = "K4(OH(OH))2O2N(So4)"
formula = "(H20(H2O)2)"

solution = Solution()
print(solution.countOfAtoms(formula))

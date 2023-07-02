class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        from collections import defaultdict
        mask_dict = defaultdict(list)
        mask_dict[0].append(0)
        valid_dict = defaultdict(bool)

        for idx, rod in enumerate(rods):
            mask = 1 << idx
            keys = sorted(mask_dict.keys(), key=lambda x: -x)
            for key in keys:
                prev_masks = mask_dict[key]
                for prev_mask in prev_masks:
                    new_key = key + rod
                    new_mask = mask | prev_mask
                    if new_key not in valid_dict:
                        valid_dict[new_key] = False
                    else:
                        if not valid_dict[new_key]:
                            for _mask in mask_dict[new_key]:
                                if _mask & new_mask == 0:
                                    valid_dict[new_key] = True
                    mask_dict[new_key].append(new_mask)

        keys = sorted(mask_dict.keys(), key=lambda x: -x)
        for key in keys:
            if valid_dict[key]:
                return key
        return 0


rods = [1,2,3,6]
rods = [1,2,3,4,5,6]
rods = [1,2]
rods = [12,34,5,6,7,8,9,11,23,12,31,12,11,56,7,8,9]
#rods = [4,5,6,8,9,1,11,23,87,1,2,3,4,5,6,1,12,44,55,6]

solution = Solution()
print(solution.tallestBillboard(rods))

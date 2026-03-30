class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # If num-1 is not in the set, it means 'num' is the start of a potential sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Count how long the sequence goes upwards
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:] + [0]):
            medians.append((window[k/2] + window[~(k/2)]) / 2.)
            window.remove(a)
            bisect.insort(window, b)
        return medians
                
                
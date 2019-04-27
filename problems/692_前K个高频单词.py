import collections
import heapq


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # Python中对于元组的排序
        return [x[1] for x in heapq.nsmallest(k, [(v, k) for k, v in collections.Counter(words).items()],
                                              key=lambda a: (-a[0], a[1]))]

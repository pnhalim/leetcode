class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0 for _ in range(len(citations) + 1)]
        for count in citations:
            if count > len(citations):
                counts[-1] += 1
            else:
                counts[count] += 1
        running_count = 0
        index = len(citations)
        for papers in counts[::-1]:
            running_count += papers
            if running_count >= index:
                return index
            index -= 1
        return 0
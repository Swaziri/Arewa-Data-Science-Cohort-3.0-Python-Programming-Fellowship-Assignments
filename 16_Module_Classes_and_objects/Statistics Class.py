import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        mid = len(sorted_data) // 2
        return (sorted_data[mid] if len(sorted_data) % 2 != 0
                else (sorted_data[mid - 1] + sorted_data[mid]) / 2)

    def mode(self):
        freq = Counter(self.data)
        max_count = max(freq.values())
        mode = [key for key, value in freq.items() if value == max_count]
        return {"mode": mode, "count": max_count}

    def std(self):
        mean = self.mean()
        return math.sqrt(sum((x - mean) ** 2 for x in self.data) / self.count())

    def var(self):
        return self.std() ** 2

    def freq_dist(self):
        freq = Counter(self.data)
        return sorted([(value / self.count() * 100, key) for key, value in freq.items()], reverse=True)

    def describe(self):
        return {
            "Count": self.count(),
            "Sum": self.sum(),
            "Min": self.min(),
            "Max": self.max(),
            "Range": self.range(),
            "Mean": self.mean(),
            "Median": self.median(),
            "Mode": self.mode(),
            "Variance": self.var(),
            "Standard Deviation": self.std(),
            "Frequency Distribution": self.freq_dist()
        }

# Example usage
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print("Count:", data.count())
print("Sum:", data.sum())
print("Min:", data.min())
print("Max:", data.max())
print("Range:", data.range())
print("Mean:", data.mean())
print("Median:", data.median())
print("Mode:", data.mode())
print("Standard Deviation:", data.std())
print("Variance:", data.var())
print("Frequency Distribution:", data.freq_dist())
print(data.describe())

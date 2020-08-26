class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def parse_number(i):
            results = []
            if i % 3 == 0: results.append("Fizz")
            if i % 5 == 0: results.append("Buzz")
            if (i % 3 != 0) and (i % 5 != 0): results.append(str(i))
            return ''.join(results)
        return list(map(parse_number, range(1, n + 1)))


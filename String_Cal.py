class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        normalized = numbers.replace('\n', ',')
        parts = normalized.split(",")
        total = sum(int(num) for num in parts)
        return total

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        parts = numbers.split(",")
        total = sum(int(num) for num in parts)
        return total

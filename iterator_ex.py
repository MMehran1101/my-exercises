import time

file = open("text.txt")

for line in file:
    print(line.rstrip())
    time.sleep(.5)

print("\n      *****    End Program    ****\n")


class ErrorLogIterator:
    def __init__(self, file_path):
        self.file = open(file_path)

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.file:
            if "ERROR" in line:
                return line.strip()
        self.file.close()
        raise StopIteration

errors = ErrorLogIterator("text.txt")

for err in errors:
    print("🚨", err)



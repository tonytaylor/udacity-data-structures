from time import time


class Prof:
    record_timings = []
    record_names = []

    @classmethod
    def record(cls, name):
        cls.record_timings.append(time())
        cls.record_names.append(name)

    @classmethod
    def print(cls):
        size = len(cls.record_timings)

        print("Simple Performance Analysis:\n")

        for i in range(0, size - 1):
            start = cls.record_timings[i]
            end = cls.record_timings[i + 1]

            print("{0}".format(cls.record_names[i]))
            print("\t{:2.4}".format(end - start))

        print("{0}\n".format(cls.record_names[size - 1]))

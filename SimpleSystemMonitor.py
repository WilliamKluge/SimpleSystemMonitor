import time

import psutil as psutil


def main():
    psutil.cpu_percent(interval=None)  # Meaningless value, supposed to ignore

    print("\'CPU %\' \'Available Memory (Bytes)\'")

    while True:
        cpu_percent = psutil.cpu_percent(interval=None)
        memory_available = psutil.virtual_memory().available
        print(cpu_percent, memory_available)
        time.sleep(1)


if __name__ == "__main__":
    main()

import time


def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Time remaining: {remaining_time} seconds", end="\r")
    print("Time's up!")


# 示例使用：计时10秒钟
timer(10)

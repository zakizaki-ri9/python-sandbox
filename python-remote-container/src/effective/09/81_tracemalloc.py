import tracemalloc

# 比較前
tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()

# 色々、メモリを使う処理をする
data = [_ for _ in range(10000)]

# スナップショット
time2 = tracemalloc.take_snapshot()

# 比較
stats = time2.compare_to(time1, "lineno")
for stat in stats[:3]:
    print(stat)

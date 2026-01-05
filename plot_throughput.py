import matplotlib.pyplot as plt
import csv
from collections import defaultdict

"""
Expected CSV format (example: throughput_log.csv)

time,queue,throughput
1,q0,5.2
1,q1,8.1
1,q2,12.4
2,q0,5.0
2,q1,8.3
2,q2,12.1
...

Throughput is assumed to be in Mbps.
"""

LOG_FILE = "throughput_log.csv"

# Data structure: {queue: [(time, throughput), ...]}
data = defaultdict(list)

# Read CSV
with open(LOG_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        time = float(row["time"])
        queue = row["queue"]
        throughput = float(row["throughput"])
        data[queue].append((time, throughput))

# Plot
plt.figure(figsize=(10, 6))

for queue, values in data.items():
    values.sort(key=lambda x: x[0])
    times = [v[0] for v in values]
    throughputs = [v[1] for v in values]
    plt.plot(times, throughputs, label=queue)

plt.xlabel("Time (seconds)")
plt.ylabel("Throughput (Mbps)")
plt.title("Queue-wise Throughput Over Time")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

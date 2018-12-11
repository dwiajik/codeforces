n, m = [int(i) for i in input().split()]
tasks = [int(i) for i in input().split()]

time = 0
prev = 0
for task in tasks:
  if task < prev:
    time += n
  prev = task

print(time + tasks[len(tasks) - 1] - 1)
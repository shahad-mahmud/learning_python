time = int(input())  # input in seconds

# convert into hours
hours = int(time / 3600)
time = time % 3600

# convert into minutes
minutes = int(time / 60)
time = time % 60

print(f"{hours}:{minutes}:{time}")
import random 
sample_space = [1, 2, 3, 4, 5, 6]
roll = random.choice(sample_space)


print("I Rolled:", roll)


sample_space = [1, 2, 3, 4, 5, 6]
Rolls = 1000000
Count = 0

for i in range(Rolls):
    roll = random.choice(sample_space)
    if roll == 6:
        Count += 1

print("Times Rolled Greater Than 4:",Count)
print("Estimated probability:", Count / Rolls)

sample_space = [1, 2, 3, 4, 5, 6]
event = []

for outcome in sample_space:
    if outcome % 2 == 0:
     event.append(outcome)

print("Outcomes in the Event:", event)
print("Exact Probability:", len(event) / len(sample_space))

not_event = []

for outcome in sample_space:
    if outcome <= 4:
       not_event.append(outcome)

print("Outcomes NOT in the event:", not_event)
print("Probablity of NOT :", len(not_event) / len(sample_space))
print("using The Complete Rule:", 1 - len(event) / len(sample_space))
def velocity (vi, a, t):
    return vi + a * t

def distance (vi, a, t):
    return vi*t + 1/2 * a * t**2


vi = 0
ct = 0
t = int(input("Please insert the time spent driving in seconds "))
a = int(input("Please insert the desired acceleration in m/s^2 "))
d = int(input("Please insert the desired distance in meters "))
dur = 0
dist = 0
lim = 60
sym = "*"
count = 0
vel = velocity (vi, a, t)

print ("Each '*' indicates every 10m")

while dur <= t:
    dist = distance (vi, a, dur)
    count = int(dist / 10)
    print ("Duration: " + str(dur) + " / Distance: " + sym*count)
    dur += 1

if vel > lim:
    print ("The person went over the speed limit. (Max speed was " + str(vel) + "m/s)")
else:
    print ("The person did not go over the speed limit. (Max speed was " + str(vel) + "m/s)")

if dist >= d:
    print ("The person reached the destination. (Reached " + str(dist) + "m)")
else:
    print ("The person did not reach the destination. (Reached " + str(dist) + "m)")

"""Lecture_ThermoDynamics"""
def thermo(energy):
    """Return Time until HeatDeath"""
    energy.sort(reverse=True)
    time = 0
    while (max(energy) - min(energy) >= 2):
        for i in xrange(1, len(energy)):
            attempt = 0
            for j in xrange(len(energy) - i):
                if energy[j] - energy[j+i] >= 2:
                    attempt = 1
                    energy[j] = energy[j] - 1
                    energy[j+i] = energy[j+i] + 1
                    time = time + 1
                    break
            if attempt == 1:
                break
    return time
print thermo(input())

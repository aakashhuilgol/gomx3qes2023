import pickle
import matplotlib.pyplot as plt


# possible jobs
plband2 = [6172, 11742, 11914, 17484, 17750, 23320, 23776, 29346, 29859, 35429, 35769, 41339, 41549, 47119, 47276, 52846];
plband3 = [3491, 9061, 9245, 14815, 15112, 20682, 21165, 26735, 27217, 32787, 33096, 38666, 38862, 44432, 44587, 50157];
psun = [0, 2088, 4097, 7594, 9601, 13101, 15105, 18608, 20609, 24115, 26113, 29622, 31618, 35129, 37122, 40636, 42626, 46144, 48130, 51651, 53634, 54000];
puhf = [3318, 3542, 8830, 9348, 14488, 15067, 20188, 20767, 25907, 26424, 31718, 31931];
pxband = [2993, 3426, 7741, 8152, 8603, 9203, 13374, 13949, 14355, 14933, 20138, 20692, 25884, 26476, 31616, 32201, 37454, 37723, 48773, 49242];


# combine consecutive values e.g. [4,5,6,7, 10,11,12] -> [4,7,11,12]
def shorten(lista):
    if len(lista) == 0:
        return lista
    listb = [lista[0]-1]
    for i in range(1,len(lista)):
        if lista[i] - lista[i-1] != 1:
            listb.append(lista[i-1])
            listb.append(lista[i]-1)

    listb.append(lista[-1])
    return listb

f = open('schedule.pkl', 'rb')

# helper function to plot jobs with correct color
def plot(times, name, plot, color, preheat, cooldown):
    for i in range(0, len(times), 2):
        plot.barh(name, times[i+1]-times[i], left=times[i], color=color, align='center')
        plot.barh(name, preheat, left=times[i]-preheat, color='#ff6600', align='center') 
        plot.barh(name, cooldown, left=times[i+1], color='#ff6600', align='center') 
    



# load pickled times
sun = pickle.load(f) 
uhf = pickle.load(f) 
lband2 = pickle.load(f) 
lband3 = pickle.load(f) 
xband = pickle.load(f) 
charge = pickle.load(f)
charge = [c/1497600. for c in charge]
gc = [i for i in range(len(charge))]


f.close()

# preprocess list
sun = shorten(sun)
uhf = shorten(uhf)
lband2 = shorten(lband2)
lband3 = shorten(lband3)
xband = shorten(xband)

# plot possible jobs
fig, ax = plt.subplots(1, 1)
plot(psun, 'Sun', ax, '#aaaaaa', 0, 0)
plot(puhf, 'UHF', ax, '#aaaaaa', 0, 0)
plot(plband2, 'L2', ax, '#aaaaaa', 0, 0)
plot(plband3, 'L3', ax, '#aaaaaa', 0, 0)
plot(pxband, 'X', ax, '#aaaaaa', 0, 0)

# plot scheduled jobs
plot(sun, 'Sun', ax, '#ffff00', 0, 0)
plot(uhf, 'UHF', ax, '#000080', 20*60, 0)
plot(lband2, 'L2', ax, '#000080', 30*60, 10*60)
plot(lband3, 'L3', ax, '#000080', 30*60, 10*60)
plot(xband, 'X', ax, '#000080', 30*60, 10*60)

ax.set_xlim(0, 54000)
# save
fig.savefig('jobs_picked.png')

ax.cla()
ax.plot(gc, charge)
fig.savefig('charge.png')

# print chosen schedule. used in kinetic battery schedule.modest
if len(uhf) == 0:
    uhf = [0,0]
if len(lband2) == 0:
    lband2 = [0,0]
if len(lband3) == 0:
    lband3 = [0,0]
if len(xband) == 0:
    xband = [0,0]
print('const int xband_len = '+str(len(xband))+';')
print('int(0..gmax)[] xband = ['+','.join(str(t) for t in xband)+'];\n')
print('const int lband3_len = '+str(len(lband3))+';')
print('int(0..gmax)[] lband3 = ['+','.join(str(t) for t in lband3)+'];\n')
print('const int lband2_len = '+str(len(lband2))+';')
print('int(0..gmax)[] lband2 = ['+','.join(str(t) for t in lband2)+'];\n')
print('const int uhf_len = '+str(len(uhf))+';')
print('int(0..gmax)[] uhf = ['+','.join(str(t) for t in uhf)+'];\n')
print('const int sun_len = '+str(len(sun))+';')
print('int(0..gmax)[] sun = ['+','.join(str(t) for t in sun)+'];\n')

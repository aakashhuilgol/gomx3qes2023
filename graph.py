import csv 
import matplotlib.pyplot as plt


# open csv file containing modest modes trace
with open('schedule.csv', 'r') as cf:
    reader = csv.reader(cf)

    fields = next(reader)
    # look for fields we are interested in
    gc_index = fields.index('gc')
    a_index = fields.index('a')
    b_index = fields.index('b')
    # init arrays
    gc = []
    a = []
    b = []

    # populate arrays with trace values
    for row in reader:
        try:
            gc.append(float(row[gc_index])/(60*60))
            a.append(float(row[a_index])/1497600)
            b.append(float(row[b_index])/1497600)
        except:
            print('finished')

    # plot a, b and SoC (a+b) over gc (global clock)
    print('plotting...')
    plt.plot(gc, a, label='a')
    plt.plot(gc, b, label='b')
    plt.plot(gc, [sum(x) for x in zip(a,b)], label='SoC')
    plt.hlines(y = 40, xmin=0, xmax=54000, linestyle='dotted', color='r')
    plt.hlines(y = 20, xmin=0, xmax=54000, linestyle='dotted', color='r')
    plt.legend(loc='upper right')
    plt.xlim(0,15)
    plt.savefig('schedule.png')
print('schedule.png created successfully')
if min(a) < 20:
    print('schedule produced is unsafe')
else:
    print('schedule produced is safe')


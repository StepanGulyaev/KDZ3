import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

def draw_D(D):
    D = plt.gca()
    major_ticks = np.arange(-4, 36, 4)
    minor_ticks = np.arange(-4, 36, 2)

    D.set_xticks(major_ticks)
    D.set_xticks(minor_ticks, minor=True)
    D.set_yticks(major_ticks)
    D.set_yticks(minor_ticks, minor=True)
    D.tick_params(axis='both', which='major', labelsize=10)
    D.tick_params(axis='both', which='minor', labelsize=10)
    # And a corresponding grid
    D.grid(which='both')

    D.set_title('D',)
    D.set_aspect(1)
    D.set_xlim((-4, 36))
    D.set_ylim((-4, 36))
    plt.axhline(0, color='orange')
    plt.axvline(0, color='orange')
    plt.xlabel(r'$x1$')
    plt.ylabel(r'$x2$')

    x = np.linspace(-4, 36, 40)
    y = -x + 16
    D.plot(x, y, linestyle='-', linewidth=2, color='black')

    x = np.linspace(-4, 36, 40)
    y = (8-x)/-2
    D.plot(x, y, linestyle='-', linewidth=2, color='black')

    x = np.linspace(-4, 36, 40)
    y = (16+3*x)/2
    D.plot(x, y, linestyle='-', linewidth=2, color='black')

    x = np.linspace(32,32,20)
    y = np.linspace(0,36,20)
    D.plot(x, y,linestyle='-',linewidth=2,color='black')

    x = np.linspace(0,36,20)
    y = np.linspace(24,24,20)
    D.plot(x, y,linestyle='-',linewidth=2,color='black')

    D.annotate("l1", xy=(5.7, 7.5), fontsize=22)
    D.annotate("l2", xy=(22.7, 5.9), fontsize=22)
    D.annotate("l3", xy=(12, 28.6), fontsize=22)
    D.annotate("l4", xy=(32.4, 20), fontsize=22)
    D.annotate("l5", xy=(17.7, 24.7), fontsize=22)

def draw_Dmod(Dmod,opt):
    Dmod = plt.gca()
    major_ticks = np.arange(-4, 36, 4)
    minor_ticks = np.arange(-4, 36, 2)

    Dmod.set_xticks(major_ticks)
    Dmod.set_xticks(minor_ticks, minor=True)
    Dmod.set_yticks(major_ticks)
    Dmod.set_yticks(minor_ticks, minor=True)
    Dmod.tick_params(axis='both', which='major', labelsize=10)
    Dmod.tick_params(axis='both', which='minor', labelsize=10)
    # And a corresponding grid
    Dmod.grid(which='both')

    Dmod.set_title('D~',)
    Dmod.set_aspect(1)
    Dmod.set_xlim((-4, 36))
    Dmod.set_ylim((-4, 36))
    plt.axhline(0, color='orange')
    plt.axvline(0, color='orange')
    plt.xlabel(r'$x1$')
    plt.ylabel(r'$x2$')

    x = np.linspace(-4, 36, 40)
    y = -x + 16
    Dmod.plot(x, y, linestyle='-', linewidth=2, color='black')

    x = np.linspace(-4, 36, 40)
    y = (8-x)/-2
    Dmod.plot(x, y, linestyle='-', linewidth=2, color='black')

    x = np.linspace(-4, 36, 40)
    y = (16+3*x)/2
    Dmod.plot(x, y, linestyle='-', linewidth=2, color='black')

    x = np.linspace(32,32,20)
    y = np.linspace(0,36,20)
    Dmod.plot(x, y,linestyle='-',linewidth=2,color='black')

    x = np.linspace(0,36,20)
    y = np.linspace(24,24,20)
    Dmod.plot(x, y,linestyle='-',linewidth=2,color='black')

    x = np.linspace(-4, 36, 40)
    y = (-16+3*x)
    Dmod.plot(x, y, linestyle='-', linewidth=2, color='black')

    x = np.linspace(-4, 36, 40)
    y = (-48-x)/-3
    Dmod.plot(x, y, linestyle='-', linewidth=2, color='black')

    plt.quiver(0, 0, 4,4, color='b', units='xy',scale=1)
    plt.quiver(0, 0, -4, 4, color='r', units='xy', scale=1)

    Dmod.annotate("a", xy=(2 - 0.6 ,2 + 0.6),fontsize = 22)
    Dmod.annotate("b", xy=(-2 + 0.6,2 + 0.6),fontsize = 22)

    Dmod.annotate("A", xy=(2.5, 10.5), fontsize=22)
    Dmod.annotate("B", xy=(6, 18.7), fontsize=22)
    Dmod.annotate("C", xy=(13.3, 21.3), fontsize=22)
    Dmod.annotate("D", xy=(9.15, 8.15), fontsize=22)

    Dmod.plot(opt.x[0], opt.x[1], 'r.', markersize=8)

    x = np.linspace(-4, 36, 40)
    y = 32-x
    Dmod.plot(x, y, linestyle='-', linewidth=2, color='red')

    Dmod.annotate("l1", xy=(5.7, 7.5), fontsize=22)
    Dmod.annotate("l2", xy=(22.7, 5.9), fontsize=22)
    Dmod.annotate("l3", xy=(12, 28.6), fontsize=22)
    Dmod.annotate("l4", xy=(32.4, 20), fontsize=22)
    Dmod.annotate("l5", xy=(17.7, 24.7), fontsize=22)
    Dmod.annotate("l6", xy=(10.7, 13.5), fontsize=22)
    Dmod.annotate("l7", xy=(2, 18), fontsize=22)




def draw_graphs(opt):
    windows_size = (9,9)
    plt.figure(figsize=windows_size)
    D = plt.gca()
    draw_D(D)
    plt.figure(figsize=windows_size)
    Dmod = plt.gca()
    draw_Dmod(Dmod,opt)
    plt.show()
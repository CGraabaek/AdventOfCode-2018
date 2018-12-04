import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_claims(claims):
    cm = plt.get_cmap('gist_rainbow')
    NUM_COLORS = 10
    colors = [cm(i/NUM_COLORS) for i in range(NUM_COLORS)]

    i=1

    plt.figure(figsize=(10,10))
    ax = plt.gca()

    for claim in claims:
        rect = patches.Rectangle((claim[1], claim[2]), claim[3], claim[4], color=colors[i%NUM_COLORS], alpha=0.5)
        ax.add_patch(rect)
        
    plt.xlim(0,1000)
    plt.ylim(0,1000)
    ax.set_aspect("equal")
    plt.tight_layout()

    #plt.savefig("day3.png")
    plt.show()
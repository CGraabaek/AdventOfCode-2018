import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_claims(claims,special):
    cm = plt.get_cmap('gist_rainbow')

    plt.figure(figsize=(10,10))
    ax = plt.gca()

    for claim in claims:
        rect = patches.Rectangle((claim[1], claim[2]), claim[3], claim[4], color='red', alpha=0.5)
        ax.add_patch(rect)
        
    rect_special = patches.Rectangle((special[1], special[2]), special[3], special[4], color='green', alpha=0.5)
    ax.add_patch(rect_special)


    plt.xlim(0,1000)
    plt.ylim(0,1000)
    ax.set_aspect("equal")
    plt.tight_layout()

    #plt.savefig("day3.png")
    plt.show()
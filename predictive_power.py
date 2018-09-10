import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('rossidata')


def sampler(min_prob,size):
    return  np.mean(np.random.choice([0,1], size, p=[min_prob, 1-min_prob]))

def total_prob(n):
    return 1-((1-(1/n))**n)
if __name__ == "__main__":
    x_range=np.arange(1,300)
    data_size=np.zeros((1000,len(x_range)))
    for j in range(np.shape(data_size)[0]):
        for k in range(np.shape(data_size)[1]):
            data_size[j,k]=sampler(0.5,x_range[k])

    fig,ax = plt.subplots()
    y=np.mean(data_size,0)
    error=np.std(data_size,0)
    ax.set_ylim([0,1])
    ax.plot(x_range,error,color='black')
    # ax.fill_between(x_range, y - error, y + error,color='#e684ae')

    fig.savefig('errors.png',transparent=True,dpi=300)
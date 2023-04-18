import pandas as pd
from matplotlib import pyplot as plt

def bar(label,data,title,path,fileName,barColor="yellow",yLabel=""):

    plt.clf()
    plt.style.use('ggplot')
    plt.bar(label, data,color=barColor)

    plt.ylabel(yLabel)


    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.title=title
    plt.savefig(path+fileName)


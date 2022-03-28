import matplotlib.pyplot as plt


def plot_first_25_images(data):
    plt.figure(figsize=(50, 50))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(data[i])
        plt.xlabel(data[i])
    plt.show()

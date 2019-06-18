import matplotlib.pyplot as plt
import numpy as np

def plotImageWithNoPaddingAndSave(image, filename, axes='off', grid=False, pad_inches=0, figsize=(15,15)):
    """
    image = image_variable
    filename = name of the file to save image (example: "./foldername/image.png")
    :This function saves the plot as an image without padding
    """
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.imshow(image)
    ax.grid(False)
    ax.axis('off')
    ax.margins(0,0)
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    plt.savefig(filename, bbox_inches='tight', transparent=True, pad_inches=pad_inches)
    
    
 def plot_3d(data, save_path=None, display_plot=False grid=True, figsize=None):
    """
    :param data: Data to plot should be of size (nx3)
                n - number of rows or data samples
    :param save_path: path to save the plotted data
    :paran display_plot: bol (if True) will display the plot
    """
    pass


if __name__=="__main__":
    import matplotlib.image as mpimg
    image=mpimg.imread('./data/test_image.png')
    plotImageWithNoPaddingAndSave(image, "./data/test_image_out.png", axes='off', grid=False, pad_inches=0)

from PIL import Image
import scipy.io


class Utils:

    def __init__(self, imageset):
        self.mat = scipy.io.loadmat(imageset)

    def create_images(self):
        im = Image.open(self.imageset)



def main():
    utils = Utils('data/DIP_sim500.mat')


if __name__ == "__main__":
    main()
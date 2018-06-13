from PIL import Image
from numpy import *
import numpy as np


class OVMoments:

    def __init__(self, filename):
        self.filename = filename
        im = Image.open(self.filename)
        #im.show()
        self.image = im

    def convert_image_to_matrix(self):
        width, height = self.image.size
        image_matrix = np.zeros((width, height))
        #data = np.zeros((height, width, 3), dtype=np.uint8)
        for i in range(width):  # total row
            for j in range(height):  # total column
                cpixel = self.image.getpixel((i, j))
                bw_value = int(round(sum(cpixel) / float(len(cpixel))))
                image_matrix[i][j] = bw_value
                #data[j][i] = cpixel



        #img = Image.fromarray(data, 'RGB')
        #img.show()
        return image_matrix



    def calculate_ovmoments(self):
        moments = []
        area = 1.0
        image_matrix = self.convert_image_to_matrix()
        area = sum(sum(image_matrix))
        dx = diff(image_matrix, 1, 1)
        dy = diff(image_matrix, 1, 0)
        mdx = sum(sum(abs(dx)))
        mdy = sum(sum(abs(dy)))
        x = image_matrix.shape[1] + 0.0
        y = image_matrix.shape[0] + 0.0

        # Longitudes de superficie
        lx = (1 + sum(1 + sum(sqrt(1 + (dx ** 2))))) / (image_matrix.shape[0] * image_matrix.shape[1])
        ly = (1 + sum(1 + sum(sqrt(1 + (dy ** 2))))) / (image_matrix.shape[0] * image_matrix.shape[1])

        # estaciones transversales
        px = (1.0 + sum(1.0 + sum(abs(dx) * (fromfunction(lambda i, j: j, dx.shape) + 1.0)))) / (0.1 + (mdx / (4.5)))
        py = (1.0 + sum(1.0 + sum(abs(dy) * (fromfunction(lambda i, j: i, dy.shape) + 1.0)))) / (0.1 + (mdy / (8.0)))

        # Frecuencias Espaciales Transversales
        fx = (1 + sum(1 + sum(abs(dx), 1) / x))
        fy = (1 + sum(1 + sum(abs(dy), 0) / y))

        moments.append(area)
        moments.append(lx)
        moments.append(ly)
        moments.append(px)
        moments.append(py)
        moments.append(fx)
        moments.append(fy)

        return moments

def main():
    moments = []

    for x in range(1, 501):
       ovmoment = OVMoments('../../sequenced_data/01_Dados_Matlab_v2/DSw_sim500_T4018/%d.tiff'% (x))
       moment = ovmoment.calculate_ovmoments()
       moments.append(moment)
       #print(moment)

    ovmoment = OVMoments('../../sequenced_data/01_Dados_Matlab_v2/DIP_seis_obs_58x81/DIP_seis_obs_58x81_T4018.tiff')
    moment = ovmoment.calculate_ovmoments()
    moments.append(moment)

    # ovmoment = OVMoments('../../sequenced_data/01_Dados_Matlab_v2/D(16) 9910-97088IP_seis_true_234x326/DIP_seis_true_234x326_T2618.tiff')
    # moment = ovmoment.calculate_ovmoments()
    # moments.append(moment)

    #ovmoment = OVMoments('../../sequenced_data/01_Dados_Matlab_v2/DIP_seis_true_234x326/DIP_seis_true_234x326_T3287.tiff')
    #moment = ovmoment.calculate_ovmoments()
    #moments.append(moment)

    #ovmoment = OVMoments('../../sequenced_data/01_Dados_Matlab_v2/DIP_seis_true_234x326/DIP_seis_true_234x326_T3652.tiff')
    #moment = ovmoment.calculate_ovmoments()
    #moments.append(moment)

    #ovmoment = OVMoments('../../sequenced_data/01_Dados_Matlab_v2/DIP_seis_true_234x326/DIP_seis_true_234x326_T4018.tiff')
    #moment = ovmoment.calculate_ovmoments()
    #moments.append(moment)


    file = open("../../sequenced_data/DSw_sim500_58x81__T4018.data", "w+")
    file.write("DN\n")
    file.write("%d\n"% (len(moments)))
    file.write("%d\n" % (7))

    for i in range(7):
        file.write("attr%d" % (i+1))
        if i != 6:
            file.write(";")
    file.write("\n")

    for m in range(len(moments)):
        file.write("%d;" % (m+1))
        ovm = moments[m]
        for n in range(len(ovm)):
            file.write("%f" % (ovm[n]))
            if n != 6:
                file.write(";")
        file.write("\n")
        #print(moments[m])


if __name__ == "__main__":
    main()

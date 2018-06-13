from PIL import Image
import math


class AboZaidMoments:

    def __init__(self, filename):
        self.filename = filename
        im = Image.open(self.filename)
        self.image = im

    """raw moment"""
    def raw_moment(self, p, q):
        """print("raw moment ", p, "-", q)"""
        m = 0
        width, height = self.image.size
        """for loop from 0 to width"""
        for i in range(0, width):
            for j in range(0, height):
                cpixel = self.image.getpixel((i, j))
                bw_value = int(round(sum(cpixel) / float(len(cpixel))))
                m += math.pow(i, p) * math.pow(j, q) * bw_value
        return m

    """centroid"""
    def centroid(self):
        """print("centroid")"""
        m00 = self.raw_moment(0, 0)
        m10 = self.raw_moment(1, 0)
        m01 = self.raw_moment(0, 1)
        x0 = m10 / m00
        y0 = m01 / m00
        arr = []
        arr.append(x0)
        arr.append(y0)
        return arr

    """Central moment"""
    def central_moment(self, p, q):
        """print("central moment ",p,"-",q)"""
        centroid = self.centroid()
        mc = 0
        width, height = self.image.size
        for i in range(0, width):
            for j in range(0, height):
                cpixel = self.image.getpixel((i, j))
                bw_value = int(round(sum(cpixel) / float(len(cpixel))))
                mc += math.pow((i - centroid[0]), p) * math.pow((j - centroid[1]), q) * bw_value
        return mc

    """Abo Zaid Normalized central moment"""
    def abozaid_moment(self, p, q):
        """print("abo zaid ",p,"-",q)"""
        mpq = self.central_moment(p, q)
        m00 = self.central_moment(0, 0)
        m20 = self.central_moment(2, 0)
        m02 = self.central_moment(0, 2)

        return mpq * (1 / m00)*math.pow(m00 / (m20 + m02), (p + q) / 2)

    def calculate_abozaid_moment(self):
        moments = []

        for n in range(0, 4):
            for m in range(0, 4):
                moment = self.abozaid_moment(n, m)
                moments.append(moment)

        return moments


def main():
    moments = AboZaidMoments('DIP_seis_obs_58x81.tiff')
    print("1;", moments.calculate_abozaid_moment())
    moments2 = AboZaidMoments('DIP_seis_obs_234x326.tiff')
    print("2;", moments2.calculate_abozaid_moment())
    moments3 = AboZaidMoments('DIP_seis_true_58x81.tiff')
    print("3;", moments3.calculate_abozaid_moment())
    moments4 = AboZaidMoments('DIP_seis_true_234x326.tiff')
    print("4;", moments4.calculate_abozaid_moment())
    moments5 = AboZaidMoments('DIP_sim500.tiff')
    print("5;", moments5.calculate_abozaid_moment())
    moments6 = AboZaidMoments('DSw_sim500.tiff')
    print("6;", moments6.calculate_abozaid_moment())


if __name__ == "__main__":
    main()

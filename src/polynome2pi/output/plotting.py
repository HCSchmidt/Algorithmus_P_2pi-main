import cmath
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from ..cli import ScanSector
from ..constants import get_colors
  

def draw_points(xs_by_j, ys_by_j, grey_segments, Obj, Charge, Ch, show_H, show_N):      # Charge[0][Ch]                   #    um Charge ergänzt

    colors = get_colors()
    for j in range(1, 29):
        if Obj[j][6] == Charge[0][Ch] or " " == Charge[0][Ch] and not j == show_H and not j == show_N:  
            print(Obj[j][6])
            if xs_by_j[j]:    
               plt.scatter(xs_by_j[j], ys_by_j[j], s=40, c=colors[j], marker=".", linewidths=0)

    if grey_segments:
        lc = LineCollection(grey_segments, colors="#6F6E6E", linewidths=2)
        plt.gca().add_collection(lc)
    
def add_reference_lines(sector: ScanSector, i_T: int):
    x_a = 0
    x_m = i_T * 1 / 5

    plt.ylabel("Energy in $m_e$")
    plt.xlabel("N")

    TWO_PI = float(2 * cmath.pi)
    i2_ = TWO_PI ** 2
    i1_ = TWO_PI 
    i3_ = TWO_PI ** 3
    i4_ = TWO_PI ** 4
    i5_ = 0.5 * (i4_ + i3_ + i2_)
    i6_ = i4_ + i3_ + i2_
    i7_= 2.5* i4_ - 1.5 * i3_ - 0.5 * i2_;
    i9_ = 2 * i4_ + 2 * i3_ + 1.5 * i2_;
    i10_ = 1.5 * i4_ + 0.5 * i3_ + 0.5 * i2_;
    i11_ = 2 * i4_ - 2 * i3_  - 2 * i2_ - 2 * i1_ 
    i12_ = 1 * i4_ - 2 * i3_  - 2 * i2_ - 2 * i1_ 
    i13_ = 3/2 * i4_ - 2 * i3_  - 2 * i2_ - 2 * i1_   
    i14_ = 1/2 * i4_ - 2 * i3_  - 2 * i2_ - 2 * i1_ 

    if sector is ScanSector.broad:
        plt.plot([x_a, x_m], [i4_, i4_], "k", linewidth=1)
        plt.text(x_a, i4_ + 15, r"$(2\pi)^4$", fontsize=12, color="blue")
        plt.plot([x_a, x_m], [i3_, i3_], "k", linewidth=1)
        plt.text(x_a, i3_ + 15, r"$(2\pi)^3$", fontsize=12, color="blue")
        plt.plot([x_a, x_m], [i5_, i5_], "k", linewidth=1)
        plt.text(x_a, i5_ + 15, r"$1/2((2\pi)^4+(2\pi)^3+(2\pi)^2)$", fontsize=12, color="blue")
        plt.plot([x_a, x_m], [i6_, i6_], "k", linewidth=1)
        plt.text(x_a, i6_ + 15, r"$(2\pi)^4+(2\pi)^3+(2\pi)^2$", fontsize=12, color="blue")

    if sector is ScanSector.E112P:
        plt.plot([x_a, x_m], [i6_, i6_], "k", linewidth=1)
        plt.text(x_a, i6_ + 15, r"$(2\pi)^4+(2\pi)^3+(2\pi)^2$", fontsize=12, color="blue")

    if sector is ScanSector.heavy:
        plt.plot([x_a, 4.5 * x_m], [i7_, i7_], "k",linewidth=1); 
        plt.text(x_a, i7_ + 15, r"$5/2(2\pi)^4-2(2\pi)^3-2(2\pi)^2-2(2\pi)$", fontsize=12, color='blue')
        plt.plot([x_a, 3.8 * x_m], [i11_, i11_], "k", linewidth=1); 
        plt.text(x_a, i11_ + 15, r"$2(2\pi)^4-2(2\pi)^3-2(2\pi)^2-2(2\pi)$", fontsize=12, color='blue')
        plt.plot([1.8 * x_m, 5 * x_m], [i12_, i12_], "k", linewidth=1); 
        plt.text(3 * x_m, i12_ + 15, r"$(2\pi)^4-2(2\pi)^3-2(2\pi)^2-2(2\pi)$", fontsize=12, color='blue')
        plt.plot([2.8 * x_m, 5 * x_m], [i13_, i13_], "k", linewidth=1); 
        plt.text(3.3 * x_m, i13_ - 150, r"$3/2(2\pi)^4-2(2\pi)^3-2(2\pi)^2-2(2\pi)$", fontsize=12, color='blue')
        plt.plot([0.8 * x_m, 5 * x_m], [i14_, i14_], "k", linewidth=1); 
        plt.text(3 * x_m, i14_ + 15, r"$1/2(2\pi)^4-2(2\pi)^3-2(2\pi)^2-2(2\pi)$", fontsize=12, color='blue')

    if sector is ScanSector.E222:
        plt.plot([x_a, 4.5 * x_m], [i11_, i11_], "k", linewidth=1); 
        plt.text(x_a, i11_ + 15, r"$2(2\pi)^4-2(2\pi)^3-2(2\pi)^2-2(2\pi)$", fontsize=12, color='blue')
        plt.plot([x_a, 2.0 * x_m], [i13_, i13_], "k", linewidth=1); 
        plt.text(x_a, i13_ + 15, r"$3/2(2\pi)^4-2(2\pi)^3-2(2\pi)^2-2(2\pi)$", fontsize=12, color='blue')
        plt.plot([2.5 * x_m, 5 * x_m], [i12_, i12_], "k", linewidth=1); 
        plt.text(3 * x_m, i12_ + 15, r"$(2\pi)^4-2(2\pi)^3-2(2\pi)^2-2(2\pi)$", fontsize=12, color='blue')
        plt.plot([1.5 * x_m, 5 * x_m], [i14_, i14_], "k", linewidth=1); 
        plt.text(3 * x_m, i14_ + 15, r"$1/2(2\pi)^4-2(2\pi)^3-2(2\pi)^2-2(2\pi)$", fontsize=12, color='blue')

    if sector is ScanSector.E333D:
        plt.plot([x_a, x_m], [i6_, i6_], "k", linewidth=1)
        plt.text(x_a, i6_ + 15, r"$(2\pi)^4+(2\pi)^3+(2\pi)^2$", fontsize=12, color="blue")      
    
    if sector in (ScanSector.light):
        plt.plot([x_a, x_m], [i3_, i3_], "k", linewidth=1)
        plt.text(x_a, i3_ + 15, r"$(2\pi)^3$", fontsize=12, color="blue")
        plt.plot([x_a, x_m], [i2_, i2_], "k", linewidth=1)
        plt.text(x_a, i2_ + 15, r"$(2\pi)^2$", fontsize=12, color="blue")

    if sector in (ScanSector.minimal):
        plt.plot([x_a, x_m], [i1_, i1_], "k", linewidth=1)
        plt.text(x_a, i1_ +1 , r"$(2\pi)$", fontsize=12, color="blue")

    # x-limits similar to your previous plots
    if sector is ScanSector.minimal:
        plt.xlim(-1000, i_T + 10000)
    elif sector is ScanSector.nucleon:
        plt.xlim(0, i_T)
    else:
        plt.xlim(-10000, i_T + 30000)

def label_offsets_for_sector(sector: ScanSector, j: int):
    """Return (X, Y, fs) where X is a whole list so we can use X[j]."""
    if sector is ScanSector.broad:
        X = [0, 4, 7, 9,8 , 9, 5, 13, -21, -12, 7, -19, 8, -28, -17, -21, -13, -20, -12, -10, -37, -9, -5.5, -22, -11, 0, 0, 0]
        return X, -20, 12

    if sector is ScanSector.E112P:                                          #H   
        X = [0, 4, 7, 9, 8, 9, 5, 13, -21, -12, 7, -19, 8, -28, -17, -4, 6, 1, -4, -4, -5, 0, 0, 0, 0, 0, 0, 0]
        return X, 0, 16
  
#    if sector is ScanSector.E122:       # test  schräg                                  #H   
#        X = [0, 4, 7, 9, 8, 9, 5, 13, -21, -12, 7, -19, 8, -28, -17, -4, 6, 1, -4, -4, -5, 0, 0, 0, 0, 0, 0, 0]
#        return X, 0, 16

    if sector is ScanSector.light:
        X = [0, 1.2, 2.5, 3,-3, 1, -4, 1]
        return X, -4, 16

    if sector is ScanSector.minimal:
        X = [0, 0.1, 0.3, 0.1]
        return X, -1, 16

    if sector is ScanSector.nucleon:
        X = [0, 2, 4, 5, 3, 4, 4, 8, -13, -7, 2, -11, 2, -14, -7, 1, 1, 1, 1, 1, 1, -0, -0, -22, -11, 0, 0, 0]
        return X, -0, 16

    if sector is ScanSector.heavy:                                                  #H
        X = [0, 5, 10, 15, 20, 24, 20, 38, -35, -20, 18, -38, -15, 5, 22, 25, -20, -30, -19, -14, 20, 20, 10, -10, -30, -15, -5, 0, 0]
        X[j] *= 2
        return X, -30, 12
    
    if sector is ScanSector.E222:                                                  #H
        X = [0, 5, 10, 15, 20, 24, 20, 38, -35, -20, 18, -38, -15, 5, 22, 25, -20, -30, -19, -14, 20, 20, 10, -10, -30, -15, -5, 0, 0]
        X[j] *= 2
        return X, -30, 12
    
    if sector is ScanSector.E333U:                                          #P                       #tau
        X = [0, 5, 10, 15, 20, 5, 9, 30, -35, -20, 7, -40, 25, 0, 0, 60, 40, 3 ,12, 25, 35, 50, 10, -10, -40, -25, -9, -15, -15, 0, 0]
        X[j] *= 4
        return X, -50, 12
    
    if sector is ScanSector.E333D:                                          #P                       #tau
        X = [0, 4, 6, 8, -3, 4, 4, 20, -10, 4, 23, -19, -10, 4, 16, -18, -9, -24, -18, -15, -8, -15, -0, -22, -11, 0, 0, 0]
        X[j] *= 5
        return X, -0, 16  

    raise ValueError(f"Unhandled sector: {sector}")

def add_particle_labels(labels):
    """Draw all particle labels returned by report.write_report().

    Expected `labels` format: iterable of dicts with keys:
      - sector, j, x_base, y, text, color
    """
    if not labels:
        return

    for item in labels:
        sector, j, x_base, y, text, color = item[:6]
        X, Y, fs = label_offsets_for_sector(sector, j)
        plt.text(
            x_base + 10000 * X[j],
            y + Y,
            text,
            fontsize=fs,
            color=color,
        )
        

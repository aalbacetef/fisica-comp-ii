from matplotlib import pyplot as plt

from code.methods.trapezium import trapezium
from code.util import write_csv
from code.pecs.pec5.data import antideriv_C, antideriv_S

if __name__ == "__main__":
    w = 5.0
    interval = (0.0, w)

    # generate subdivisions
    max_pow = 9
    subdivisions = [6] + [1 << k for k in range(max_pow)]
    subdivisions.sort()

    # initiate integrating functions of C(w) and S(w)
    integrate_c = trapezium(antideriv_C, interval)
    integrate_s = trapezium(antideriv_S, interval)

    C = [integrate_c(n) for n in subdivisions]
    S = [integrate_s(n) for n in subdivisions]

    # plot results
    plt.figure(1)
    (c_line,) = plt.plot(subdivisions, C, color="red")
    (s_line,) = plt.plot(subdivisions, S, color="blue")
    plt.legend([c_line, s_line], ["C(w)", "S(w)"])

    plt.savefig("pecs/pec5/figures/ex1.png")
    plt.close()

    # prepare table
    hdr = ["n", "C(w)", "S(w)"]
    rows = [[subdivisions[k], C[k], S[k]] for k in range(len(subdivisions))]
    write_csv(hdr, rows, "pecs/pec5/data/c_s_subdivs.csv")

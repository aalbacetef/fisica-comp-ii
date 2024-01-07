from code.util import load_data, mk_plot
from matplotlib import pyplot as plt


if __name__ == "__main__":
    t, r = load_data("pecs/pec6/data/simul_no_rel_r.csv")
    t, v = load_data("pecs/pec6/data/simul_no_rel_v.csv")

    png_paths = [
        "pecs/pec6/figures/no_rel_rx_ry_rz.png",
        "pecs/pec6/figures/no_rel_vx_vy_vz.png",
        "pecs/pec6/figures/no_rel_y_x.png",
    ]

    mk_plot(
        t,
        r,
        ["r_x(t)", "r_y(t)", "r_z(t)"],
        png_paths[0],
    )

    mk_plot(
        t,
        v,
        ["v_x(t)", "v_y(t)", "v_z(t)"],
        png_paths[1],
    )

    plt.figure(1)
    x = [r_k[0] for r_k in r]
    y = [r_k[1] for r_k in r]
    plt.xlabel("r_y(t)")
    plt.ylabel("r_x(t)")
    plt.plot(y, x)
    plt.savefig(png_paths[2])
    plt.close()

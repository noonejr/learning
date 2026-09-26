"""Recreation of DeepLearning.AI's lab_utils_uni.py plots (C1 W1 Lab03 - cost function).

Plain inline matplotlib + core ipywidgets sliders (no ipympl), so it renders in Colab,
VS Code (incl. the Colab extension) and Jupyter. The course's click-to-pick and drag-to-rotate
are sliders here.
"""

import io
import textwrap

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
from ipywidgets import Image, IntSlider, VBox
from matplotlib.colors import LinearSegmentedColormap

dlblue, dlorange, dldarkred, dlmagenta, dlpurple = "#0096ff", "#FF9300", "#C00000", "#FF40FF", "#7030A0"
dlcolors = [dlblue, dlorange, dldarkred, dlmagenta, dlpurple]
dlcm = LinearSegmentedColormap.from_list("dl_map", dlcolors, N=5)

# approximation of the course's deeplearning.mplstyle
plt.style.use({
    "axes.prop_cycle": plt.cycler(color=[dlblue, dlorange, dlmagenta, dlpurple, dldarkred]),
    "axes.edgecolor": "#f0f0f0",
    "axes.linewidth": 3.0,
    "axes.labelsize": "large",
    "axes.titlesize": "x-large",
    "lines.linewidth": 4,
    "lines.solid_capstyle": "butt",
    "xtick.major.size": 0,
    "ytick.major.size": 0,
    "font.size": 8,
    "font.sans-serif": ["Verdana", "DejaVu Sans", "Arial", "sans-serif"],
    "figure.facecolor": "white",
})


def _show(draw, **sliders):
    """Sliders + a PNG Image widget re-rendered from draw(**values) -> fig on slider release.

    Not `interact`: its Output-widget capture shows each plot twice in VS Code / Colab.
    sliders: name=(value, min, max, step)
    """
    sliders = {k: IntSlider(value=v, min=lo, max=hi, step=st, description=k, continuous_update=False)
               for k, (v, lo, hi, st) in sliders.items()}
    img = Image(format="png")

    def update(_=None):
        fig = draw(**{k: s.value for k, s in sliders.items()})
        buf = io.BytesIO()
        fig.savefig(buf, format="png", bbox_inches="tight")
        plt.close(fig)  # else the inline backend displays it again at cell end
        img.value = buf.getvalue()

    for s in sliders.values():
        s.observe(update, "value")
    update()
    display(VBox([*sliders.values(), img]))


def compute_cost(x, y, w, b):
    """J(w,b) = 1/(2m) * sum((w*x + b - y)^2)"""
    return np.mean((w * x + b - y) ** 2) / 2


def plt_fit(x, y, w, b, ax):
    """Housing data, model line, and a dotted cost line + label per example with the cost sum."""
    f_wb = w * x + b
    costs = (f_wb - y) ** 2 / 2
    ax.plot(x, f_wb, c=dlblue, label="Our Prediction")
    ax.vlines(x, y, f_wb, lw=3, color=dlpurple, ls="dotted", label="cost for point")
    ax.scatter(x, y, marker="x", c="r", label="Actual Value")
    for xi, mid, c in zip(x, (y + f_wb) / 2, costs):
        ax.annotate(f"{c:0.0f}", xy=(xi, mid), color=dlpurple, xytext=(5, 0), textcoords="offset points")
    text = f"cost = (1/m)*({' +'.join(f'{c:0.0f}' for c in costs)}) = {costs.mean():0.0f}"
    ax.text(0.15, 0.02, textwrap.fill(text, 45), transform=ax.transAxes, color=dlpurple)
    ax.set(title="Housing Prices", ylabel="Price (in 1000s of dollars)", xlabel="Size (1000 sqft)")
    ax.legend()


def _plot_bowl(ax, W, B, Z, cmap, alpha, zlabel):
    ax.plot_surface(W, B, Z, cmap=cmap, alpha=alpha)
    ax.plot_wireframe(W, B, Z, color="k", alpha=0.1)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1, 1, 1, 0))
    ax.zaxis.set_rotate_label(False)
    ax.set(xlabel="$w$", ylabel="$b$")
    ax.set_zlabel(zlabel, rotation=90)


def plt_intuition(x_train, y_train, b=100):
    """Slider over w (b fixed): model fit on the left, cost vs. w on the right."""
    w_array = np.arange(0, 400, 5)
    cost = [compute_cost(x_train, y_train, w, b) for w in w_array]

    def draw(w):
        fig, ax = plt.subplots(1, 2, constrained_layout=True, figsize=(8, 4))
        plt_fit(x_train, y_train, w, b, ax[0])
        cur = compute_cost(x_train, y_train, w, b)
        ax[1].plot(w_array, cost)
        ax[1].scatter(w, cur, s=100, color=dldarkred, zorder=10, label=f"cost at w={w}")
        ax[1].hlines(cur, ax[1].get_xlim()[0], w, lw=4, color=dlpurple, ls="dotted")
        ax[1].vlines(w, ax[1].get_ylim()[0], cur, lw=4, color=dlpurple, ls="dotted")
        ax[1].set(title=f"Cost vs. w, (b fixed at {b})", ylabel="Cost", xlabel="w")
        ax[1].legend(loc="upper center")
        fig.suptitle(f"Minimize Cost: Current Cost = {cur:0.0f}", fontsize=12)
        return fig

    _show(draw, w=(150, 0, 400, 10))


def plt_stationary(x_train, y_train):
    """Model fit + cost contour + 3D cost surface. Sliders choose w, b and rotate the surface."""
    W, B = np.meshgrid(np.linspace(-100, 500, 100), np.linspace(-250, 350, 100))
    Z = np.vectorize(lambda w, b: compute_cost(x_train, y_train, w, b))(W, B)
    log_Z = np.log(np.maximum(Z, 1e-6))

    def draw(w, b, rotate):
        cost = compute_cost(x_train, y_train, w, b)
        fig = plt.figure(figsize=(9, 8))
        ax0, ax1 = fig.add_subplot(2, 2, 1), fig.add_subplot(2, 2, 2)
        ax2 = fig.add_subplot(2, 1, 2, projection="3d")
        fig.subplots_adjust(hspace=0.35)

        plt_fit(x_train, y_train, w, b, ax0)

        ax1.contour(W, B, log_Z, levels=12, linewidths=2, alpha=0.7, colors=dlcolors)
        ax1.scatter(w, b, s=100, color=dlblue, zorder=10)
        ax1.hlines(b, -100, w, lw=4, color=dlpurple, ls="dotted")
        ax1.vlines(w, -250, b, lw=4, color=dlpurple, ls="dotted")
        ax1.annotate(f"Cost: {cost:.0f}", xy=(w, b), xytext=(4, 4), textcoords="offset points",
                     bbox=dict(facecolor="white"), size=10)
        ax1.set(title="Cost(w,b)", xlabel="w", ylabel="b", xlim=(-100, 500), ylim=(-250, 350))

        _plot_bowl(ax2, W, B, Z, dlcm, 0.3, "J(w, b)\n\n")
        ax2.scatter3D(w, b, cost, marker="X", s=100)
        ax2.set_title("Cost(w,b)", size=12)
        ax2.view_init(30, rotate)
        ax2.set_box_aspect((2.2, 1.6, 0.7), zoom=1.25)  # wide & flat like the course figure
        return fig

    _show(draw, w=(200, -100, 500, 1), b=(-100, -250, 350, 1), rotate=(-120, -180, 180, 10))


def soup_bowl():
    """Symmetric convex bowl J(w,b) = w^2 + b^2."""
    W, B = np.meshgrid(np.linspace(-20, 20, 100), np.linspace(-20, 20, 100))

    def draw(rotate):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(projection="3d")
        _plot_bowl(ax, W, B, W**2 + B**2, "Spectral_r", 0.7, "$J(w,b)$")
        ax.set_title("$J(w,b)$", size=15)
        ax.view_init(45, rotate)
        return fig

    _show(draw, rotate=(-120, -180, 180, 10))


if __name__ == "__main__":
    # numbers from the course screenshots
    x, y = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2]), np.array([250, 300, 480, 430, 630, 730])
    assert round(compute_cost(x, y, 150, 100)) == 3362
    assert round(compute_cost(x, y, 200, -100)) == 9367
    assert compute_cost(np.array([1.0, 2.0]), np.array([300.0, 500.0]), 200, 100) == 0
    print("ok")

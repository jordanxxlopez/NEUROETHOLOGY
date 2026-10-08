#!/usr/bin/env python3
"""Figures for Lecture 12. Charts plot only values reported in the cited papers;
schematics are labeled as schematics in their slide captions.

    python lectures/L12/make_figures.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle, Wedge

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)

COBALT, LIGHT, PALE, SLATE, INK = "#1F3FA0", "#7F96D6", "#DCE4F7", "#5A6378", "#1E2330"
UV, GREEN, RED = "#5B3FA8", "#2E8B57", "#B22222"
plt.rcParams.update({
    "font.family": "Liberation Sans", "font.size": 13, "axes.edgecolor": SLATE,
    "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 200,
})


def save(fig, name):
    fig.savefig(OUT / name, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def box(ax, x, y, w, h, text, fc=PALE, ec=COBALT, size=12, color=INK, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03",
                                fc=fc, ec=ec, lw=1.5))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size, color=color,
            fontweight="bold" if bold else "normal", wrap=True)


def arrow(ax, x1, y1, x2, y2, color=SLATE, lw=1.8, style="-|>"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=16,
                                 color=color, lw=lw))


SCALE = 0.72  # draw small so lettering stays legible when placed on a slide


def canvas(w=8, h=5):
    fig, ax = plt.subplots(figsize=(w * SCALE, h * SCALE))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def nomogram(lmax, wl):
    """Govardovskii et al. (2000) A1 alpha-band template, normalized to 1."""
    x = lmax / wl
    a, b, c = 0.8795 + 0.0459 * np.exp(-((lmax - 300) ** 2) / 11940), 0.922, 1.104
    A = 69.7
    return 1 / (np.exp(A * (a - x)) + np.exp(28 * (b - x)) + np.exp(-14.9 * (c - x)) + 0.674)


# 1 hunting sequence (Forster 1977)
def f_hunt():
    fig, ax = canvas(9, 4.2)
    groups = [("Orientation", ["Alert", "Swivel", "Alignment"]),
              ("Pursuit", ["Follow", "Run", "Stalk"]),
              ("Capture", ["Pre-crouch", "Crouch", "Jump"])]
    for i, (g, els) in enumerate(groups):
        x = 0.02 + i * 0.34
        box(ax, x, 0.72, 0.28, 0.18, g, fc=COBALT, color="white", size=15, bold=True)
        for j, e in enumerate(els):
            box(ax, x + 0.03, 0.48 - j * 0.17, 0.22, 0.13, e, size=13)
        if i < 2:
            arrow(ax, x + 0.285, 0.81, x + 0.335, 0.81, COBALT, 2.2)
    ax.text(0.5, 0.0, "Response patterns (bold) and their motor elements, after Forster (1977)",
            ha="center", fontsize=11, color=SLATE)
    save(fig, "f01_hunt_sequence.png")


# 2 fields of view (Land 1985; Zurek & Nelson 2012)
def f_fov():
    fig, ax = plt.subplots(figsize=(6.4 * SCALE, 6.4 * SCALE))
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Wedge((0, 0), 1.0, 40, 140, fc=LIGHT, alpha=0.55, ec=COBALT, lw=1.2))
    ax.add_patch(Wedge((0, 0), 1.0, -90, 270, fc=PALE, alpha=0.35, ec="none"))
    ax.add_patch(Wedge((0, 0), 1.12, 60, 120, width=0.08, fc=COBALT, ec="none"))
    ax.add_patch(Wedge((0, 0), 0.6, 88.5, 91.5, fc=INK, ec="none"))
    ax.add_patch(Ellipse((0, -0.05), 0.18, 0.32, fc=SLATE))
    ax.text(0, 1.18, "Principal-eye scan span ≈ 60°", ha="center", color=COBALT, fontsize=12, fontweight="bold")
    ax.text(0, 0.67, "retina at any instant:\n~1° wide (centre)", ha="center", fontsize=10, color=INK)
    ax.text(1.0, 0.85, "ALE field\n≈ ±50°", ha="center", fontsize=12, color=COBALT)
    ax.text(0, -0.8, "Secondary eyes together:\nnearly 360°", ha="center", fontsize=12, color=SLATE)
    save(fig, "f02_fields_of_view.png")


# 3 receptor spacing / acuity (Land 1985; Land 1969a; Cerveira et al. 2021)
def f_spacing():
    labels = ["Principal eye,\nbest case", "Land 1969a\nmin. spacing", "Cyrba principal\n(dim-light species)",
              "ALE (Portia)", "PME (Portia)", "PLE (Portia)"]
    lo = np.array([0.04, 11 / 60, 12.4 / 60, 0.55, 1.0, 1.49])
    hi = np.array([0.10, 11 / 60, 12.4 / 60, 0.97, 1.0, 1.49])
    fig, ax = plt.subplots(figsize=(9 * SCALE, 4.6 * SCALE))
    y = np.arange(len(labels))[::-1]
    colors = [COBALT, COBALT, COBALT, SLATE, SLATE, SLATE]
    for yi, l, h, c in zip(y, lo, hi, colors):
        if h > l:
            ax.plot([l, h], [yi, yi], color=c, lw=9, solid_capstyle="round")
        else:
            ax.plot(l, yi, "o", color=c, ms=11)
        txt = f"{l:.2f}–{h:.2f}°" if h > l else f"{l:.2f}°"
        ax.text(h * 1.12, yi, txt, va="center", fontsize=12)
    ax.set_xscale("log")
    ax.set_xlim(0.03, 3)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Angular spacing or resolvable angle (degrees, log scale)")
    ax.axvspan(0.03, 0.3, color=PALE, alpha=0.5, lw=0)
    ax.text(0.032, 5.45, "principal eyes", color=COBALT, fontsize=11)
    ax.text(0.5, 5.45, "secondary eyes", color=SLATE, fontsize=11)
    ax.set_ylim(-0.6, 5.8)
    save(fig, "f03_receptor_spacing.png")


# 4 principal eye schematic (Land 1969a; Williams & McIntyre 1980)
def f_eye():
    fig, ax = canvas(9, 4.2)
    ax.add_patch(Ellipse((0.08, 0.5), 0.09, 0.42, fc=LIGHT, ec=COBALT, lw=2))
    ax.add_patch(Polygon([[0.1, 0.72], [0.75, 0.6], [0.75, 0.4], [0.1, 0.28]], fc="#F4F6FB", ec=SLATE, lw=1.5))
    ax.add_patch(Ellipse((0.74, 0.5), 0.05, 0.18, fc="white", ec=COBALT, lw=2))
    for i, c in enumerate([PALE, "#B9C7EC", LIGHT, COBALT]):
        ax.add_patch(Rectangle((0.78 + i * 0.035, 0.38), 0.03, 0.24, fc=c, ec=INK, lw=0.6))
    ax.text(0.08, 0.2, "corneal lens", ha="center", fontsize=12)
    ax.text(0.42, 0.75, "long eye tube (movable)", ha="center", fontsize=12)
    ax.text(0.62, 0.22, "pit: diverging\nsecond lens", ha="center", fontsize=11, color=COBALT)
    ax.text(0.85, 0.7, "4 receptor tiers", ha="center", fontsize=12)
    ax.text(0.88, 0.32, "4      3     2     1", ha="center", fontsize=10)
    ax.text(0.85, 0.13, "light →  layer 4 first, layer 1 deepest", ha="center", fontsize=10, color=SLATE)
    for yy in (0.62, 0.38):
        arrow(ax, 0.0, yy, 0.05, yy, COBALT, 1.4)
    ax.text(0.5, 0.0, "Schematic, not to scale", ha="center", fontsize=10, color=SLATE)
    save(fig, "f04_principal_eye.png")


# 5 telephoto (thin-lens geometry, illustrative)
def f_tele():
    fig, ax = canvas(9, 3.8)
    ax.plot([0.02, 0.98], [0.5, 0.5], color=SLATE, lw=0.8, ls="--")
    ax.add_patch(Ellipse((0.15, 0.5), 0.03, 0.6, fc=LIGHT, ec=COBALT, lw=2))
    ax.add_patch(Ellipse((0.66, 0.5), 0.025, 0.25, fc="white", ec=COBALT, lw=2))
    for y0 in (0.75, 0.25):
        ax.plot([0.02, 0.15], [y0, y0], color=GREEN, lw=1.6)
        y1 = 0.5 + (y0 - 0.5) * (1 - (0.66 - 0.15) / 0.65)
        ax.plot([0.15, 0.66], [y0, y1], color=GREEN, lw=1.6)
        ax.plot([0.66, 0.92], [y1, 0.5], color=GREEN, lw=1.6)
        ax.plot([0.66, 0.80], [y1, 0.5 + (y1 - 0.5) * 0.0], color=GREEN, lw=0.8, ls=":")
    ax.plot([0.92, 0.92], [0.38, 0.62], color=INK, lw=3)
    ax.text(0.15, 0.1, "corneal lens\n(converging)", ha="center", fontsize=11)
    ax.text(0.66, 0.15, "pit\n(diverging)", ha="center", fontsize=11, color=COBALT)
    ax.text(0.92, 0.7, "retina", ha="center", fontsize=11)
    ax.text(0.5, 0.92, "A diverging element behind the lens lengthens the effective focal length → larger image per receptor",
            ha="center", fontsize=11, color=INK)
    save(fig, "f05_telephoto.png")


# 6 retina tiers: Land's 1969 predictions vs later measurements
def f_tiers():
    fig, ax = canvas(9, 4.4)
    rows = [("Layer 4 (most distal)", "not assigned", "UV"),
            ("Layer 3", "violet–UV", "UV"),
            ("Layer 2", "blue-green", "green"),
            ("Layer 1 (deepest)", "red", "green")]
    ax.text(0.2, 0.92, "Tier", ha="center", fontsize=12, fontweight="bold")
    ax.text(0.535, 0.92, "Land (1969a)\npredicted pigment", ha="center", fontsize=12, fontweight="bold")
    ax.text(0.85, 0.92, "Later evidence,\nHasarius adansoni", ha="center", fontsize=12, fontweight="bold")
    col = {"UV": UV, "green": GREEN}
    for i, (t, p, m) in enumerate(rows):
        y = 0.72 - i * 0.18
        box(ax, 0.03, y, 0.34, 0.13, t, size=12)
        box(ax, 0.39, y, 0.29, 0.13, p, fc="white", ec=SLATE, size=12)
        box(ax, 0.71, y, 0.27, 0.13, m, fc=col[m], ec=col[m], color="white", size=12, bold=True)
    save(fig, "f06_retina_tiers.png")


# 7 Land 1969a conjugate planes
def f_conj():
    fig, ax = canvas(9, 3.6)
    ax.plot([0.03, 0.97], [0.45, 0.45], color=SLATE, lw=0.8)
    pts = [(0.12, "≈ 2 cm in front\n(blue-green on layer 1)", GREEN), (0.55, "distant objects\n(blue-green on layer 2)", GREEN),
           (0.9, "infinity\n(red on layer 1)", RED)]
    for x, t, c in pts:
        ax.plot(x, 0.45, "o", color=c, ms=13)
        ax.text(x, 0.6, t, ha="center", fontsize=12, color=INK)
    ax.text(0.5, 0.15, "Object planes that Land calculated to be in focus on each layer (chromatic aberration).\n"
            "Distances from Land (1969a) abstract; axis not to scale.", ha="center", fontsize=10.5, color=SLATE)
    save(fig, "f07_conjugate_planes.png")


# 8 DeVoe 1975 spectral classes (template curves at reported peaks)
def f_devoe():
    wl = np.linspace(300, 700, 400)
    fig, ax = plt.subplots(figsize=(8.5 * SCALE, 4.4 * SCALE))
    ax.plot(wl, nomogram(370, wl), color=UV, lw=2.5, label="UV cells, λmax 370 nm")
    ax.plot(wl, nomogram(532, wl), color=GREEN, lw=2.5, label="green cells, λmax 532 nm")
    dual = np.maximum(nomogram(370, wl), nomogram(525, wl))
    ax.plot(wl, dual, color=SLATE, lw=1.6, ls="--", label="UV-green cells, peaks ≈370 and 525 nm")
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Relative sensitivity")
    ax.set_ylim(0, 1.08)
    ax.legend(frameon=False, fontsize=10, loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=1)
    save(fig, "f08_devoe_spectral.png")


# 9 Nagata defocus geometry (thin-lens illustration)
def f_defocus():
    fig, ax = canvas(9, 4.2)
    ax.add_patch(Ellipse((0.12, 0.5), 0.03, 0.62, fc=LIGHT, ec=COBALT, lw=2))
    for y0 in (0.8, 0.2):
        ax.plot([0.12, 0.8], [y0, 0.5], color=GREEN, lw=2)
        ax.plot([0.8, 0.9], [0.5, 0.5 - (y0 - 0.5) * 0.15], color=GREEN, lw=2)
    ax.add_patch(Rectangle((0.78, 0.25), 0.04, 0.5, fc=GREEN, alpha=0.25, ec=INK))
    ax.add_patch(Rectangle((0.72, 0.25), 0.04, 0.5, fc=GREEN, alpha=0.12, ec=INK))
    ax.text(0.8, 0.15, "layer 1\nsharp", ha="center", fontsize=11)
    ax.text(0.73, 0.82, "layer 2\nblurred", ha="center", fontsize=11)
    ax.annotate("", xy=(0.74, 0.55), xytext=(0.74, 0.45), arrowprops=dict(arrowstyle="<->", color=RED, lw=2))
    ax.text(0.6, 0.5, "blur width\nvaries with\nobject distance", ha="center", va="center", fontsize=11, color=RED)
    ax.text(0.12, 0.08, "lens", ha="center", fontsize=11)
    ax.text(0.5, 0.95, "Both layers carry green-sensitive pigment; green light is focused on layer 1 only",
            ha="center", fontsize=11.5, color=INK)
    save(fig, "f09_defocus.png")


# 10 green vs red prediction (qualitative, from Nagata et al. 2012 logic)
def f_redgreen():
    fig, ax = canvas(9, 3.8)
    for i, (lab, c, txt) in enumerate([("Green light", GREEN, "blur on layer 2 matches the\ncalibrated green relation\n→ accurate jump"),
                                       ("Red light", RED, "longer focal length: blur equals that\nof a closer object in green\n→ jump falls short")]):
        y = 0.55 - i * 0.45
        box(ax, 0.02, y, 0.2, 0.32, lab, fc=c, ec=c, color="white", size=14, bold=True)
        box(ax, 0.27, y, 0.42, 0.32, txt, fc="white", ec=SLATE, size=9.5)
        ax.plot([0.75, 0.97], [y + 0.08] * 2, color=SLATE, lw=1)
        ax.plot(0.95, y + 0.08, "s", color=INK, ms=10)
        land = 0.95 if i == 0 else 0.86
        ax.add_patch(FancyArrowPatch((0.76, y + 0.1), (land, y + 0.12), connectionstyle="arc3,rad=-0.5",
                                     arrowstyle="-|>", mutation_scale=15, color=c, lw=2))
    ax.text(0.86, 0.96, "target ■", ha="center", fontsize=10, color=SLATE)
    save(fig, "f10_red_green.png")


# 11 Habronattus red filter (Zurek et al. 2015)
def f_filter():
    wl = np.linspace(300, 720, 400)
    fig, ax = plt.subplots(figsize=(8.5 * SCALE, 4.4 * SCALE))
    ax.plot(wl, nomogram(360, wl), color=UV, lw=2.5, label="UV receptors")
    ax.plot(wl, nomogram(530, wl), color=GREEN, lw=2.5, label="green receptors, λmax ≈ 530 nm")
    ax.axvline(626, color=RED, lw=2.5, ls="--", label="filtered receptors, reported λmax 626 nm")
    ax.annotate("", xy=(620, 0.55), xytext=(536, 0.55), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))
    ax.text(578, 0.6, "red filter", ha="center", color=RED, fontsize=12)
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Relative sensitivity")
    ax.set_ylim(0, 1.08)
    ax.legend(frameon=False, fontsize=10, loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=1)
    save(fig, "f11_red_filter.png")


# 12 six muscles / six axons (Land 1969b)
def f_muscles():
    fig, ax = canvas(9, 4.2)
    box(ax, 0.36, 0.38, 0.28, 0.24, "principal-eye\ntube + retina", fc=LIGHT, size=13, bold=True)
    for (x, y, t) in [(0.03, 0.75, "dorsal"), (0.03, 0.08, "ventral"), (0.73, 0.75, "medial"), (0.73, 0.08, "lateral")]:
        box(ax, x, y, 0.24, 0.15, t + " muscle\n(translation)", fc="white", ec=SLATE, size=11)
        arrow(ax, x + (0.24 if x < 0.5 else 0), y + 0.075, 0.36 if x < 0.5 else 0.64, 0.5, SLATE, 1.4)
    box(ax, 0.38, 0.8, 0.24, 0.13, "2 band muscles\n(torsion)", fc=COBALT, ec=COBALT, color="white", size=11)
    arrow(ax, 0.5, 0.8, 0.5, 0.62, COBALT, 2)
    ax.text(0.5, 0.0, "6 muscles · 6 axons, one per muscle", ha="center", fontsize=10.5, color=INK)
    save(fig, "f12_muscles.png")


# 13 scanning frequencies (Land 1969b; Land 1972 chapter)
def f_scan():
    fig, ax = plt.subplots(figsize=(8.5 * SCALE, 3.6 * SCALE))
    items = [("Lateral oscillation\nacross target", 0.5, 1.0, COBALT), ("Slow conjugate shift\n(with torsion)", 0.1, 0.2, LIGHT)]
    for i, (lab, lo, hi, c) in enumerate(items):
        ax.plot([lo, hi], [i, i], lw=14, color=c, solid_capstyle="butt")
        ax.text(hi + 0.03, i, f"{lo}–{hi} Hz  (period {1/hi:.0f}–{1/lo:.0f} s)", va="center", fontsize=12)
    ax.set_yticks([0, 1])
    ax.set_yticklabels([x[0] for x in items])
    ax.set_xlim(0, 1.6)
    ax.set_ylim(-0.6, 1.6)
    ax.set_xlabel("Frequency (Hz)")
    save(fig, "f13_scan_frequencies.png")


# 14 eyetracker (Canavesi et al. 2011; Jakob et al. 2018)
def f_tracker():
    fig, ax = canvas(9, 3.8)
    box(ax, 0.02, 0.35, 0.18, 0.3, "stimulus\nmonitor", fc="white", ec=SLATE)
    box(ax, 0.32, 0.35, 0.16, 0.3, "beam\nsplitter", fc=PALE)
    box(ax, 0.6, 0.35, 0.16, 0.3, "tethered\nspider", fc=LIGHT, bold=True)
    box(ax, 0.32, 0.8, 0.16, 0.17, "IR camera", fc=COBALT, color="white", bold=True)
    arrow(ax, 0.2, 0.5, 0.32, 0.5, SLATE)
    arrow(ax, 0.48, 0.5, 0.6, 0.5, SLATE)
    arrow(ax, 0.6, 0.6, 0.48, 0.85, COBALT)
    ax.text(0.9, 0.5, "IR passes the\ncuticle; retina\nreflects to camera", ha="center", va="center", fontsize=9)
    ax.text(0.4, 0.12, "visible stimulus and infrared retinal image share one optical axis", ha="center", fontsize=11, color=SLATE)
    save(fig, "f14_eyetracker.png")


# 15 Jakob et al. 2018 design and outcome
def f_jakob():
    fig, ax = canvas(9.5, 4.4)
    ax.text(0.22, 0.93, "Stimulus set", ha="center", fontsize=14, fontweight="bold")
    box(ax, 0.02, 0.55, 0.4, 0.3, "Moving disks\nsize 3, 4, 5°\nspeed 2.77, 7.60, 15.13 °/s", fc=PALE, size=10.5)
    box(ax, 0.02, 0.15, 0.4, 0.3, "Stationary objects", fc=PALE, size=12)
    ax.text(0.62, 0.93, "ALEs open", ha="center", fontsize=13, fontweight="bold")
    ax.text(0.86, 0.93, "ALEs masked", ha="center", fontsize=13, fontweight="bold")
    cells = [(0.62, 0.7, "smooth\ntracking", COBALT), (0.86, 0.7, "no smooth\ntracking", RED),
             (0.62, 0.3, "scanning", COBALT), (0.86, 0.3, "scanning", COBALT)]
    for x, y, t, c in cells:
        box(ax, x - 0.105, y - 0.12, 0.21, 0.24, t, fc=c, ec=c, color="white", size=11, bold=True)
    save(fig, "f15_jakob_matrix.png")


# 16 Bruce et al. 2021 distractor paradigm
def f_bruce():
    fig, ax = canvas(9, 3.8)
    ax.add_patch(Rectangle((0.35, 0.3), 0.3, 0.45, fc="white", ec=SLATE, lw=1.5))
    ax.add_patch(Ellipse((0.5, 0.62), 0.06, 0.1, fc=INK))
    ax.text(0.5, 0.4, "primary stimulus\n(cricket or other)", ha="center", fontsize=10)
    ax.add_patch(Ellipse((0.86, 0.6), 0.07, 0.12, fc=SLATE))
    ax.text(0.86, 0.32, "distractor oval\n(ALE field)", ha="center", fontsize=10)
    ax.add_patch(Wedge((0.5, 0.05), 0.2, 80, 100, fc=LIGHT, alpha=0.7))
    ax.text(0.5, 0.0, "principal eyes", ha="center", fontsize=10, color=COBALT)
    arrow(ax, 0.6, 0.12, 0.83, 0.52, COBALT, 1.6)
    ax.text(0.78, 0.15, "gaze shift?", fontsize=11, color=COBALT)
    ax.text(0.5, 0.92, "Gaze shifts to the distractor were less frequent when the primary stimulus was a cricket",
            ha="center", fontsize=11)
    save(fig, "f16_bruce.png")


# 17 Loconsole et al. 2024 cue-target design
def f_loco():
    fig, ax = canvas(9, 3.6)
    box(ax, 0.02, 0.4, 0.24, 0.3, "1  spatial cue\nleft or right", fc=PALE)
    box(ax, 0.38, 0.4, 0.24, 0.3, "2  target dot\nmoving vertically", fc=PALE)
    box(ax, 0.74, 0.4, 0.24, 0.3, "3  detection\nspeed & accuracy", fc=PALE)
    arrow(ax, 0.26, 0.55, 0.38, 0.55)
    arrow(ax, 0.62, 0.55, 0.74, 0.55)
    ax.text(0.5, 0.13, "Result: faster and more accurate when the target appeared opposite the cue", ha="center",
            fontsize=12, color=COBALT, fontweight="bold")
    save(fig, "f17_loconsole.png")


# 18 brain pathways (Strausfeld & Barth 1993; Steinhoff et al. 2020)
def f_brain():
    fig, ax = canvas(9.5, 4.6)
    box(ax, 0.02, 0.72, 0.2, 0.18, "Principal eyes\n(AME)", fc=COBALT, color="white", bold=True)
    box(ax, 0.3, 0.72, 0.17, 0.18, "1st-order\nneuropil", fc=PALE)
    box(ax, 0.55, 0.72, 0.17, 0.18, "2nd-order\nneuropil", fc=PALE)
    box(ax, 0.8, 0.55, 0.18, 0.2, "Arcuate\nbody", fc=LIGHT, bold=True)
    for a, b in ((0.22, 0.3), (0.47, 0.55)):
        arrow(ax, a, 0.81, b, 0.81)
    arrow(ax, 0.72, 0.8, 0.8, 0.68)
    box(ax, 0.02, 0.1, 0.2, 0.18, "ALE + PLE", fc=SLATE, color="white", bold=True)
    box(ax, 0.3, 0.1, 0.17, 0.18, "own 1st-order\nneuropils", fc=PALE)
    box(ax, 0.55, 0.1, 0.17, 0.18, "2nd-order +\nshared L2", fc=PALE)
    box(ax, 0.8, 0.1, 0.18, 0.2, "Mushroom\nbody", fc=LIGHT, bold=True)
    for a, b in ((0.22, 0.3), (0.47, 0.55), (0.72, 0.8)):
        arrow(ax, a, 0.19, b, 0.19)
    box(ax, 0.02, 0.41, 0.2, 0.16, "PME", fc="white", ec=SLATE)
    box(ax, 0.3, 0.41, 0.17, 0.16, "1st-order\nneuropil", fc=PALE)
    arrow(ax, 0.22, 0.49, 0.3, 0.49)
    arrow(ax, 0.47, 0.5, 0.8, 0.62, SLATE, 1.4)
    save(fig, "f18_brain_pathways.png")


# 19 Menda et al. 2014 latency window
def f_menda():
    fig, ax = plt.subplots(figsize=(8.5 * SCALE, 3.0 * SCALE))
    ax.axvspan(80, 160, color=LIGHT, alpha=0.7)
    ax.axvline(0, color=INK, lw=2)
    ax.text(2, 0.85, "stimulus onset", fontsize=11)
    ax.text(120, 0.5, "window in which spiking\nbecame linked to the\nprey-like stimulus\n(≈80–160 ms)", ha="center",
            va="center", fontsize=11, color=COBALT)
    ax.set_xlim(-20, 300)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Time after stimulus onset (ms)")
    save(fig, "f19_menda_latency.png")


# 20 De Agrò et al. 2021 outcomes
def f_biomotion():
    fig, ax = canvas(9, 3.8)
    rows = [("Biological\nvs random", "discriminated; turned\npreferentially toward random"),
            ("Biological\nvs scrambled", "no preference")]
    for i, (a, b) in enumerate(rows):
        y = 0.55 - i * 0.42
        box(ax, 0.02, y, 0.33, 0.28, a, fc=PALE, size=11, bold=True)
        box(ax, 0.4, y, 0.58, 0.28, b, fc="white", ec=SLATE, size=11)
    ax.text(0.5, 0.95, "Point-light displays shown to the secondary eyes; response = turning on a sphere",
            ha="center", fontsize=11, color=SLATE)
    save(fig, "f20_biomotion.png")


# 21 jump mechanics (Parry & Brown 1959; Nabawy et al. 2018)
def f_jump():
    fig, axs = plt.subplots(3, 1, figsize=(7.5 * SCALE, 6.4 * SCALE), gridspec_kw={"height_ratios": [2, 1, 1]})
    panels = [
        (axs[0], [("femur–patella", 65.3, 144.0), ("tibia–metatarsus", 17.3, 46.7)], "Joint pressure, leg IV (kPa)", 190,
         "Parry & Brown (1959), Sitticus"),
        (axs[1], [("take-off velocity", 0.52, 0.97)], "m/s", 1.4, "Nabawy et al. (2018)"),
        (axs[2], [("time to take-off", 18.1, 31.6)], "ms", 45, "Nabawy et al. (2018)"),
    ]
    for ax, rows, xl, xmax, title in panels:
        for i, (lab, lo, hi) in enumerate(rows):
            ax.plot([lo, hi], [i, i], lw=14, color=COBALT if i == 0 else LIGHT, solid_capstyle="butt")
            ax.text(hi + xmax * 0.03, i, f"{lo}–{hi}", va="center", fontsize=11)
        ax.set_yticks(range(len(rows)))
        ax.set_yticklabels([r[0] for r in rows])
        ax.set_xlim(0, xmax)
        ax.set_ylim(-0.7, len(rows) - 0.3)
        ax.set_xlabel(xl)
        ax.set_title(title, fontsize=11)
    fig.tight_layout()
    save(fig, "f21_jump.png")


# 22 dim light (Cerveira et al. 2019)
def f_dim():
    fig, ax = plt.subplots(figsize=(8.5 * SCALE, 3.8 * SCALE))
    vals = [(234, "proficient", COBALT), (1.35, "proficient", COBALT), (0.54, "minority succeeded", LIGHT),
            (0.24, "none succeeded", RED)]
    for k, (v, t, c) in enumerate(vals):
        ax.plot(v, 0, "o", ms=16, color=c)
        ax.text(v, 0.2 + 0.25 * (k % 2), f"{v} cd/m²\n{t}", ha="center", fontsize=11)
    ax.set_xscale("log")
    ax.set_xlim(0.12, 800)
    ax.set_ylim(-0.3, 0.85)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Luminance (cd/m², log scale)")
    save(fig, "f22_dim_light.png")


# 23 Land 1971 ring experiment
def f_ring():
    fig, ax = canvas(9, 4)
    ax.add_patch(Circle((0.3, 0.5), 0.3 * 0.45, fc="none", ec=SLATE, lw=6))
    ax.add_patch(Ellipse((0.3, 0.5), 0.08, 0.14, fc=INK))
    ax.plot([0.3, 0.3], [0.57, 0.95], color=SLATE, lw=2)
    ax.text(0.04, 0.97, "carapace fixed to holder", fontsize=10)
    ax.text(0.3, 0.1, "legs turn a light ring", ha="center", fontsize=11)
    ax.plot(0.8, 0.75, "o", color=COBALT, ms=14)
    ax.text(0.8, 0.88, "stimulus seen\nby a lateral eye", ha="center", fontsize=10)
    arrow(ax, 0.42, 0.55, 0.75, 0.73, COBALT, 1.5)
    ax.text(0.72, 0.33, "ring rotation ≈ the turn the spider\nwould have made; the eyes never\nmove, so no visual feedback",
            ha="center", fontsize=9.5, color=INK)
    save(fig, "f23_ring.png")


# 24 hyperacuity illustration (Zurek & Nelson 2012a; Land 1985)
def f_hyper():
    fig, ax = plt.subplots(figsize=(8.5 * SCALE, 3.6 * SCALE))
    for i, x in enumerate(np.arange(0, 5, 1)):
        ax.add_patch(Circle((x, 0), 0.42, fc=PALE, ec=COBALT, lw=1.5))
    ax.annotate("", xy=(1, -0.75), xytext=(2, -0.75), arrowprops=dict(arrowstyle="<->", color=SLATE))
    ax.text(1.5, -1.0, "receptor spacing ≈ 0.55–0.97° (ALE)", ha="center", fontsize=11)
    ax.plot([2.2, 2.3], [0.75, 0.75], color=RED, lw=6)
    ax.text(2.25, 1.0, "detectable displacement:\nroughly one-tenth of the spacing", ha="center", fontsize=11, color=RED)
    ax.set_xlim(-0.8, 4.8)
    ax.set_ylim(-1.3, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "f24_hyperacuity.png")


# 25 Zurek et al. 2010 optimum
def f_zurek():
    fig, ax = canvas(9, 3.4)
    for i, (k, v) in enumerate([("dot diameter", "4°"), ("contrast", "40%"), ("speed", "9°/s")]):
        x = 0.04 + i * 0.33
        box(ax, x, 0.35, 0.26, 0.4, f"{v}\n{k}", fc=COBALT, ec=COBALT, color="white", size=16, bold=True)
    ax.text(0.5, 0.12, "Most effective dot for orienting turns, all eyes except the ALEs covered",
            ha="center", fontsize=11, color=SLATE)
    save(fig, "f25_zurek_optimum.png")


# 26 opsins (Koyanagi et al. 2008; Nagata et al. 2012)
def f_opsins():
    fig, ax = canvas(9, 3.6)
    items = [("Rh1", "green-sensitive", GREEN, "most eyes;\nprincipal-eye layers 1–2"),
             ("Rh2", "blue-sensitive", COBALT, "distribution debated"),
             ("Rh3 / Rh4", "UV-sensitive", UV, "principal-eye layers 3–4")]
    for i, (n, s, c, w) in enumerate(items):
        y = 0.68 - i * 0.3
        box(ax, 0.02, y, 0.18, 0.22, n, fc=c, ec=c, color="white", size=14, bold=True)
        box(ax, 0.23, y, 0.27, 0.22, s, fc="white", ec=SLATE, size=10.5)
        box(ax, 0.53, y, 0.45, 0.22, w, fc=PALE, size=10.5)
    save(fig, "f26_opsins.png")


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("f_") and callable(fn):
            fn()
    print(sorted(p.name for p in OUT.glob("*.png")))

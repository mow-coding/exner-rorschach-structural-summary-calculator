"""Render public synthetic benchmark figures from reviewed aggregate data.

The figures deliberately keep the fixed-excerpt comparison separate from the
retrieval experiment, where Luna used Fast rather than the released tier.
"""

from pathlib import Path
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
INITIAL = ROOT / "v3-web" / "benchmarks" / "2026-09-23"
FOLLOWUP = ROOT / "v3-web" / "benchmarks" / "2026-09-24"
raw = json.loads((INITIAL / "results.json").read_text(encoding="utf-8"))
rescored = json.loads((INITIAL / "results-rescored.json").read_text(encoding="utf-8"))

INK = "#23333d"
MUTED = "#596c76"
GRID = "#dce3e5"
PAPER = "#f9faf8"
TERRA = "#405f7b"
SOL = "#78a7c5"
LUNA = "#dc9a45"


def style(fig, axes, title, note):
    fig.patch.set_facecolor(PAPER)
    for ax in axes:
        ax.set_facecolor(PAPER)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.spines["bottom"].set_color(GRID)
        ax.xaxis.grid(True, color=GRID, linewidth=0.8)
        ax.set_axisbelow(True)
        ax.tick_params(axis="both", colors=MUTED, length=0)
    fig.suptitle(title, x=0.055, y=0.96, ha="left", fontsize=17, color=INK, weight="bold")
    fig.text(0.055, 0.035, note, ha="left", va="bottom", fontsize=8.7, color=MUTED)


labels = ["GPT-5.6 Terra", "GPT-6 Sol", "GPT-6 Luna"]
keys = ["gpt-5.6-terra", "gpt-6-sol", "gpt-6-luna"]
colors = [TERRA, SOL, LUNA]
costs = [raw["models"][key]["costUsd"] for key in keys]
passes = [rescored["models"][key]["rescoredPassed"] for key in keys]
assert passes == [257, 254, 255]
assert all(rescored["models"][key]["total"] == 280 for key in keys)

fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.2), dpi=180)
style(fig, axes, "Same-input model comparison", "260 synthetic cases | 290 calls/model | fixed reference excerpts | list-price calculation, not an invoice")
for ax, values, heading, maximum, fmt in [
    (axes[0], costs, "Generation cost (US$)  ↓", 4.0, "${:.3f}"),
    (axes[1], passes, "Wording checks passed (/280)  ↑", 280, "{:.0f}/280"),
]:
    y = range(3)
    ax.barh(y, values, color=colors, height=0.55, edgecolor="none")
    ax.set_yticks(list(y), labels, fontsize=10, color=INK)
    ax.invert_yaxis()
    ax.set_xlim(0, maximum)
    ax.set_title(heading, loc="left", pad=12, fontsize=11, weight="bold", color=INK)
    for idx, value in enumerate(values):
        ax.text(min(value + maximum * 0.018, maximum * 0.92), idx, fmt.format(value),
                va="center", fontsize=10, color=INK, weight="bold")
fig.text(0.055, 0.095, "Automatic wording checks are not clinical accuracy.", fontsize=9, color=INK, weight="bold")
fig.subplots_adjust(left=0.16, right=0.97, bottom=0.23, top=0.74, wspace=0.35)
for ext in ("svg", "png"):
    fig.savefig(INITIAL / f"model-comparison.{ext}", dpi=180, facecolor=PAPER)
plt.close(fig)


def normalize_svg(path):
    """Remove Matplotlib's trailing path whitespace for clean Git diffs."""
    lines = path.read_text(encoding="utf-8").splitlines()
    path.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf-8")


normalize_svg(INITIAL / "model-comparison.svg")

fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.2), dpi=180)
style(fig, axes, "Actual-retrieval trial", "30 synthetic source cases x 3 repeats/model | Terra standard vs Luna Fast (not the released standard tier)")
comparison_labels = ["GPT-5.6 Terra\nstandard", "GPT-6 Luna\nFast"]
for ax, values, heading, maximum, fmt in [
    (axes[0], [1.372149, 0.064049], "Retrieval + generation cost (US$)  ↓", 1.55, "${:.3f}"),
    (axes[1], [2.024, 2.652], "Median first token (seconds)  ↓", 3.2, "{:.3f}s"),
]:
    ax.barh(range(2), values, color=[TERRA, LUNA], height=0.5, edgecolor="none")
    ax.set_yticks([0, 1], comparison_labels, fontsize=10, color=INK)
    ax.invert_yaxis()
    ax.set_xlim(0, maximum)
    ax.set_title(heading, loc="left", pad=12, fontsize=11, weight="bold", color=INK)
    for idx, value in enumerate(values):
        ax.text(min(value + maximum * 0.018, maximum * 0.90), idx, fmt.format(value),
                va="center", fontsize=10, color=INK, weight="bold")
fig.text(0.055, 0.095, "Fast results cannot be used as timing or cost estimates for the standard-tier release.", fontsize=9, color=INK, weight="bold")
fig.subplots_adjust(left=0.19, right=0.97, bottom=0.23, top=0.74, wspace=0.38)
for ext in ("svg", "png"):
    fig.savefig(FOLLOWUP / f"retrieval-trial.{ext}", dpi=180, facecolor=PAPER)
plt.close(fig)
normalize_svg(FOLLOWUP / "retrieval-trial.svg")

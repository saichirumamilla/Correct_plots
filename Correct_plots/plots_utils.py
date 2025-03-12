import seaborn as sns
import matplotlib.pyplot as plt

def standardize_style(ax, font_size=12, line_width=2, color_scheme='seaborn-muted'):
    """
    Standardizes the style of the plot with customizable parameters.
    """
    sns.set_style(color_scheme)
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(font_size)
    for line in ax.get_lines():
        line.set_linewidth(line_width)

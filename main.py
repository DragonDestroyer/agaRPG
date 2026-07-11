from pyscript import display, document, when
import matplotlib.pyplot as plt
import numpy as np
import js

# Hide loading message once Python is ready
loading = document.getElementById("loading-msg")
if loading:
    loading.style.display = "none"

# Clear previous plots
def clear_plot():
    target = document.getElementById("plot-target")
    target.innerHTML = ""

def make_plot(func_name="sin", n_points=200):
    clear_plot()
    
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=100)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f8f9fa')
    
    x = np.linspace(-2 * np.pi, 2 * np.pi, n_points)
    
    if func_name == "sin":
        y = np.sin(x)
        title = "Sine Wave"
        color = "#00d4ff"
    elif func_name == "cos":
        y = np.cos(x)
        title = "Cosine Wave"
        color = "#7b2cbf"
    elif func_name == "sinc":
        y = np.sinc(x / np.pi)
        title = "Sinc Function"
        color = "#ff6b6b"
    elif func_name == "exp":
        y = np.exp(-0.2 * np.abs(x)) * np.sin(3 * x)
        title = "Damped Sine Wave"
        color = "#51cf66"
    else:  # random walk
        y = np.cumsum(np.random.randn(n_points))
        x = np.arange(n_points)
        title = "Random Walk"
        color = "#fcc419"
    
    ax.plot(x, y, color=color, linewidth=2.5, alpha=0.9)
    ax.fill_between(x, y, alpha=0.15, color=color)
    ax.set_title(title, fontsize=14, fontweight='bold', color='#212529')
    ax.set_xlabel("x", fontsize=11)
    ax.set_ylabel("y", fontsize=11)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Display the figure into the target div
    display(fig, target="plot-target", append=False)
    plt.close(fig)

# Initial plot
make_plot()

# Button handler
@when("click", "#plot-btn")
def update_plot(event):
    func = document.getElementById("func-select").value
    points = int(document.getElementById("points-slider").value)
    make_plot(func, points)

# Live update points label
@when("input", "#points-slider")
def update_label(event):
    val = document.getElementById("points-slider").value
    document.getElementById("points-val").innerText = val

import tkinter as tk
import math

# ------------------ Configurable Colors ------------------
BG_COLOR = "#2c3f70"          # Background color
ENTRY_COLOR = "#c63030"       # Entry box color
RESULT_COLOR = "#cc11bf"      # Result text color
TEXT_COLOR = "#000000"        # Labels text color
BUTTON_COLOR = "#1a73e8"      # Button background color
BUTTON_TEXT_COLOR = "#b15176" # Button text color

# ------------------ Create main window ------------------
window = tk.Tk()
window.title("Comprehensive Facial Analysis")
window.geometry("600x700")
window.config(bg=BG_COLOR)

# ----- Title -----
title_label = tk.Label(
    window,
    text="Enter All Facial Measurements",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 16, "bold")
)
title_label.pack(pady=15)

# ------------------ Facial Third Measurements ------------------
tk.Label(window, text="Facial Third Measurements", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(window, text="1. Upper Third (units):", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).pack()
upper_entry = tk.Entry(window, bg=ENTRY_COLOR, fg=TEXT_COLOR, font=("Arial", 12))
upper_entry.pack(pady=5)

tk.Label(window, text="2. Middle Third (units):", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).pack()
middle_entry = tk.Entry(window, bg=ENTRY_COLOR, fg=TEXT_COLOR, font=("Arial", 12))
middle_entry.pack(pady=5)

tk.Label(window, text="3. Lower Third (units):", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).pack()
lower_entry = tk.Entry(window, bg=ENTRY_COLOR, fg=TEXT_COLOR, font=("Arial", 12))
lower_entry.pack(pady=5)

# ------------------ Lip / Alar Base Measurements ------------------
tk.Label(window, text="Lip & Alar Base Measurements", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(window, text="4. Lip Width (units):", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).pack()
lip_entry = tk.Entry(window, bg=ENTRY_COLOR, fg=TEXT_COLOR, font=("Arial", 12))
lip_entry.pack(pady=5)

tk.Label(window, text="5. Alar Base Width (units):", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).pack()
alar_entry = tk.Entry(window, bg=ENTRY_COLOR, fg=TEXT_COLOR, font=("Arial", 12))
alar_entry.pack(pady=5)

# ------------------ Canthal Tilt Measurements ------------------
tk.Label(window, text="Canthal Tilt Measurements", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(window, text="6. Eye Width (units):", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).pack()
width_entry = tk.Entry(window, bg=ENTRY_COLOR, fg=TEXT_COLOR, font=("Arial", 12))
width_entry.pack(pady=5)

tk.Label(window, text="7. Vertical difference (outer-inner canthus, units):", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).pack()
height_entry = tk.Entry(window, bg=ENTRY_COLOR, fg=TEXT_COLOR, font=("Arial", 12))
height_entry.pack(pady=5)

# ------------------ Result Label ------------------
response_label = tk.Label(window, text="", bg=BG_COLOR, fg=RESULT_COLOR, font=("Arial", 12), justify="left")
response_label.pack(pady=20)

# ------------------ Calculation Function ------------------
def calculate_all():
    try:
        # --- Facial Third ---
        upper = float(upper_entry.get())
        middle = float(middle_entry.get())
        lower = float(lower_entry.get())
        avg = (upper + middle + lower) / 3
        var_upper = abs(upper - avg) / avg * 100
        var_middle = abs(middle - avg) / avg * 100
        var_lower = abs(lower - avg) / avg * 100
        mean_deviation = (var_upper + var_middle + var_lower) / 3
        harmony_score = max(0, 100 - mean_deviation*2)

        facial_third_result = (f"Facial Third Harmony:\n"
                               f"  Upper Variance: {var_upper:.2f}%\n"
                               f"  Middle Variance: {var_middle:.2f}%\n"
                               f"  Lower Variance: {var_lower:.2f}%\n"
                               f"  Overall Harmony Score: {harmony_score:.2f}%\n\n")

        # --- Lip / Alar Base Ratio ---
        try:
            lip_width = float(lip_entry.get())
            alar_base = float(alar_entry.get())

            if alar_base == 0:
                lip_result = "Alar base cannot be zero.\n\n"
            else:
                ratio = lip_width / alar_base
                if abs(ratio - 1.6) < 1e-6:
                    lip_result = "Lip/Alar Base Ratio: Perfect (1.6)\n\n"
                elif ratio > 1.6:
                    lip_result = f"Lip/Alar Base Ratio:\n  Ratio: {ratio:.2f}\n  Lips too wide\n\n"
                else:  # ratio < 1.6
                    lip_result = f"Lip/Alar Base Ratio:\n  Ratio: {ratio:.2f}\n  Lips too narrow\n\n"
        except ValueError:
            lip_result = "Please enter valid numbers for lip and alar base.\n\n"

        # --- Canthal Tilt ---
        eye_width = float(width_entry.get())
        vertical_diff = float(height_entry.get())
        angle_rad = math.atan(vertical_diff / eye_width)
        angle_deg = math.degrees(angle_rad)

        if 5 <= angle_deg <= 8:
            tilt_desc = "Ideal canthal tilt"
            off_text = ""
        elif angle_deg > 8:
            tilt_desc = "Canthal tilt too high"
            off_text = f" ({angle_deg - 8:.2f}° above 8°)"
        elif 0 <= angle_deg < 5:
            tilt_desc = "Neutral tilt"
            off_text = f" ({5 - angle_deg:.2f}° below ideal start 5°)"
        else:
            tilt_desc = "Negative tilt"
            off_text = f" ({abs(angle_deg):.2f}° below 0°)"

        canthal_result = f"Canthal Tilt:\n  Angle: {angle_deg:.2f}°\n  {tilt_desc}{off_text}"

        # --- Display All ---
        response_label.config(text=facial_third_result + lip_result + canthal_result)

    except ValueError:
        response_label.config(text="Please enter valid numbers for all measurements.")
    except ZeroDivisionError:
        response_label.config(text="Eye width and Alar base cannot be zero.")

# ------------------ Calculate Button ------------------
submit_button = tk.Button(window, text="Calculate All", command=calculate_all,
                          bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=("Arial", 12))
submit_button.pack(pady=10)

# Run window
window.mainloop()

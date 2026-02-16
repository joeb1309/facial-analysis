import streamlit as st
import math

# ------------------ Title ------------------
st.title("Comprehensive Facial Analysis")
st.markdown("Enter all facial measurements below:")

# ------------------ Facial Third Measurements ------------------
st.subheader("Facial Third Measurements")
upper = st.number_input("1. Upper Third (units):", value=0.0, step=0.1)
middle = st.number_input("2. Middle Third (units):", value=0.0, step=0.1)
lower = st.number_input("3. Lower Third (units):", value=0.0, step=0.1)

# ------------------ Lip / Alar Base Measurements ------------------
st.subheader("Lip & Alar Base Measurements")
lip_width = st.number_input("4. Lip Width (units):", value=0.0, step=0.1)
alar_base = st.number_input("5. Alar Base Width (units):", value=0.0, step=0.1)

# ------------------ Canthal Tilt Measurements ------------------
st.subheader("Canthal Tilt Measurements")
eye_width = st.number_input("6. Eye Width (units):", value=0.0, step=0.1)
vertical_diff = st.number_input("7. Vertical difference (outer-inner canthus, units):", value=0.0, step=0.1)

# ------------------ Calculate Button ------------------
if st.button("Calculate All"):
    try:
        # --- Facial Third ---
        avg = (upper + middle + lower) / 3
        var_upper = abs(upper - avg) / avg * 100 if avg != 0 else 0
        var_middle = abs(middle - avg) / avg * 100 if avg != 0 else 0
        var_lower = abs(lower - avg) / avg * 100 if avg != 0 else 0
        mean_deviation = (var_upper + var_middle + var_lower) / 3
        harmony_score = max(0, 100 - mean_deviation * 2)

        facial_third_result = (
            f"**Facial Third Harmony:**\n"
            f"- Upper Variance: {var_upper:.2f}%\n"
            f"- Middle Variance: {var_middle:.2f}%\n"
            f"- Lower Variance: {var_lower:.2f}%\n"
            f"- Overall Harmony Score: {harmony_score:.2f}%\n"
        )

        # --- Lip / Alar Base Ratio ---
        if alar_base == 0:
            lip_result = "Alar base cannot be zero.\n"
        else:
            ratio = lip_width / alar_base
            if abs(ratio - 1.6) < 1e-6:
                lip_result = "Lip/Alar Base Ratio: Perfect (1.6)\n"
            elif ratio > 1.6:
                lip_result = f"Lip/Alar Base Ratio: {ratio:.2f} → Lips too wide\n"
            else:
                lip_result = f"Lip/Alar Base Ratio: {ratio:.2f} → Lips too narrow\n"

        # --- Canthal Tilt ---
        if eye_width == 0:
            canthal_result = "Eye width cannot be zero."
        else:
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

            canthal_result = f"**Canthal Tilt:**\n- Angle: {angle_deg:.2f}°\n- {tilt_desc}{off_text}"

        # --- Display All Results ---
        st.markdown("---")
        st.markdown(facial_third_result)
        st.markdown(lip_result)
        st.markdown(canthal_result)

    except Exception as e:
        st.error(f"Error in calculation: {e}")

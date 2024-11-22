import streamlit as st
import math

# Define the function Tran_Eff
def Tran_Eff(V0, I0, W0):
    """
    Calculate R0 (resistance) and X0 (reactance) from given parameters.
    Parameters:
        V0 (float): Voltage in volts.
        I0 (float): Current in amperes.
        W0 (float): Power in watts.
    Returns:
        R0 (float): Resistance in ohms.
        X0 (float): Reactance in ohms.
    """
    # Calculate NPF (Power Factor)
    NPF = W0 / (V0 * I0)
    
    # Calculate Magnetizing Current (Im) and Working Current (Iw)
    Im = I0 * math.sqrt(1 - NPF**2)
    Iw = I0 * NPF
    
    # Calculate R0 and X0
    R0 = V0 / Iw if Iw != 0 else float('inf')  # Avoid division by zero
    X0 = V0 / Im if Im != 0 else float('inf')  # Avoid division by zero
    
    return R0, X0

# Build Streamlit Web Application
st.title("Transformer Open Circuit Test Calculator")
st.write("This application calculates the Resistance (R0) and Reactance (X0) of a transformer.")

# User Input Fields
V0 = st.number_input("Enter Voltage (V0) in volts:", min_value=0.0, format="%.2f")
I0 = st.number_input("Enter Current (I0) in amperes:", min_value=0.0, format="%.2f")
W0 = st.number_input("Enter Power (W0) in watts:", min_value=0.0, format="%.2f")

# Calculate and Display Results
if st.button("Calculate"):
    if V0 > 0 and I0 > 0 and W0 > 0:
        R0, X0 = Tran_Eff(V0, I0, W0)
        st.success(f"Results:\nResistance (R0): {R0:.2f} ohms\nReactance (X0): {X0:.2f} ohms")
    else:
        st.error("Please provide valid non-zero inputs for V0, I0, and W0.")
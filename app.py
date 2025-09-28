import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.fftpack import fft, fftfreq
import streamlit as st

# ==========================================================
# 1. Pemodelan Osilator Teredam
# ==========================================================
def sdof(t, y, m, c, k, F0, omega):
    x, v = y
    dxdt = v
    dvdt = (F0*np.sin(omega*t) - c*v - k*x) / m
    return [dxdt, dvdt]

def simulate(m, c, k, F0=1000, omega=2*np.pi*5, tmax=20):
    y0 = [0, 0]
    t_eval = np.linspace(0, tmax, 5000)
    sol = solve_ivp(sdof, [0, tmax], y0, t_eval=t_eval, args=(m, c, k, F0, omega))
    return sol.t, sol.y[0]

def frequency_spectrum(t, x):
    N = len(t)
    dt = t[1] - t[0]
    xf = fftfreq(N, dt)[:N//2]
    yf = np.abs(fft(x))[:N//2]
    return xf, yf

def resonance_curve(m, c, k, F0=1000, freq_range=(1, 20)):
    freqs = np.linspace(freq_range[0], freq_range[1], 200)
    amplitudes = []
    for f in freqs:
        omega = 2*np.pi*f
        X = F0 / np.sqrt((k - m*omega**2)**2 + (c*omega)**2)
        amplitudes.append(X)
    return freqs, amplitudes

# ==========================================================
# 2. Streamlit Web Interface
# ==========================================================
st.title("Simulasi Dinamika Rumah Adat Indonesia 🏠🌏")
st.markdown("Aplikasi ini memodelkan **rumah adat** sebagai sistem osilator teredam satu derajat kebebasan (SDOF) terhadap input gempa sederhana.")

# Pilih material
material = st.selectbox("Pilih Material Rumah Adat", ["Kayu", "Bambu"])

if material == "Kayu":
    m, k, c = 1000, 50000, 1000
else:
    m, k, c = 800, 30000, 800

# Input parameter
F0 = st.slider("Gaya Gempa (N)", 500, 2000, 1000)
f_input = st.slider("Frekuensi Input Gempa (Hz)", 1, 20, 5)
tmax = st.slider("Durasi Simulasi (detik)", 5, 60, 20)

# Simulasi
t, x = simulate(m, c, k, F0, 2*np.pi*f_input, tmax)

# Plot respons waktu
st.subheader("Respons Waktu")
fig1, ax1 = plt.subplots()
ax1.plot(t, x)
ax1.set_xlabel("Waktu (s)")
ax1.set_ylabel("Perpindahan (m)")
ax1.set_title(f"Respons Waktu - Rumah {material}")
st.pyplot(fig1)

# Plot spektrum frekuensi
st.subheader("Spektrum Frekuensi")
xf, yf = frequency_spectrum(t, x)
fig2, ax2 = plt.subplots()
ax2.plot(xf, yf)
ax2.set_xlabel("Frekuensi (Hz)")
ax2.set_ylabel("Amplitudo")
ax2.set_title(f"Spektrum Frekuensi - Rumah {material}")
st.pyplot(fig2)

# Plot kurva resonansi
st.subheader("Kurva Resonansi")
freqs, amps = resonance_curve(m, c, k, F0)
fig3, ax3 = plt.subplots()
ax3.plot(freqs, amps)
ax3.set_xlabel("Frekuensi Input (Hz)")
ax3.set_ylabel("Amplitudo Maksimum (m)")
ax3.set_title(f"Kurva Resonansi - Rumah {material}")
st.pyplot(fig3)

# Info resonansi
f_res = freqs[np.argmax(amps)]
A_max = max(amps)
st.success(f"**Frekuensi Resonansi Rumah {material}: {f_res:.2f} Hz dengan Amplitudo Maksimum {A_max:.4f} m**")

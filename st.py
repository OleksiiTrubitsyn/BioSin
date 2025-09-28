import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Заголовок приложения
st.title("МІЦНІ НЕРВИ 1.0")

# Пользовательские параметры
k = st.slider("Коефіцієнт k", min_value=0.0, max_value=2.0, value=1.0, step=0.1)
phi = st.slider("Фаза φ (у радіанах)", min_value=0.0, max_value=2*np.pi, value=0.0, step=0.1)

# Временные переменные
t = np.linspace(0, 100, 1000)
h = t  # Предположим, что h зависит от времени так же, как и t

# Уравнения
S1 = np.sin(2 * np.pi * t / 23) + k * np.sin(2 * np.pi * h / 24 + phi)
S2 = np.sin(2 * np.pi * t / 28) + k * np.sin(2 * np.pi * h / 24 + phi)
S3 = np.sin(2 * np.pi * t / 33) + k * np.sin(2 * np.pi * h / 24 + phi)

# Визуализация
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, S1, label="S1: T=23")
ax.plot(t, S2, label="S2: T=28")
ax.plot(t, S3, label="S3: T=33")
ax.set_title("Порівняння синусоїдальных сигналів")
ax.set_xlabel("Час (t)")
ax.set_ylabel("Амплітуда (S)")
ax.legend()
ax.grid(True)

st.pyplot(fig)
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

# Danh sách các mục trên vòng quay
segments = ["Giải Nhất", "Giải Nhì", "Giải Ba", "Giải Khuyến Khích"]

# Trọng số (xác suất quay)
weights = [10, 30, 50, 10]  # Tổng 100%

def draw_wheel():
    num_segments = len(segments)
    angles = np.linspace(0, 360, num_segments + 1)

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
    for i in range(num_segments):
        ax.barh(1, width=np.deg2rad(angles[i+1] - angles[i]), left=np.deg2rad(angles[i]), color=colors[i], edgecolor='black', alpha=0.7)

    for i in range(num_segments):
        angle = (angles[i] + angles[i+1]) / 2
        ax.text(np.deg2rad(angle), 0.5, segments[i], ha='center', va='center', fontsize=12, fontweight='bold')

    plt.title("Vòng Quay May Mắn (Hiển thị đều nhưng trọng số ngầm)", fontsize=14, fontweight='bold')
    return fig

def spin_wheel():
    result = random.choices(segments, weights=weights, k=1)[0]
    return result

# Giao diện Streamlit
st.title("🎡 Vòng Quay May Mắn")
st.write("Vòng quay hiển thị các phần bằng nhau nhưng kết quả dựa trên trọng số.")

# Hiển thị vòng quay
st.pyplot(draw_wheel())

# Nút quay vòng
if st.button("🎯 Quay Ngay!"):
    result = spin_wheel()
    st.success(f"Kết quả quay: **{result}** 🎉")

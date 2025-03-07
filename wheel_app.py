import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import time

# Danh sách các phần trên vòng quay
segments = ["10k", "50k", "Chúc bạn may mắn lần sau", "20k", "Nước", "Chúc bạn may mắn lần sau"]
colors = ["#E74C3C", "#EC69C5", "#4B2C83", "#F4C542", "#4CAF50", "#5DADE2"]
weights = [10, 15, 30, 20, 15, 30]  # Xác suất xuất hiện

# Hàm vẽ vòng quay
def draw_wheel(rotation=0):
    num_segments = len(segments)
    angles = np.linspace(0, 360, num_segments + 1)

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    for i in range(num_segments):
        ax.barh(1, width=np.deg2rad(angles[i+1] - angles[i]), 
                left=np.deg2rad(angles[i] + rotation), color=colors[i], edgecolor='black', alpha=0.8)

        angle = (angles[i] + angles[i+1]) / 2 + rotation
        ax.text(np.deg2rad(angle), 0.6, segments[i], ha='center', va='center', fontsize=12, fontweight='bold', color="white")

    plt.title("🎡 Vòng Quay May Mắn", fontsize=14, fontweight='bold')
    return fig

# Hàm tạo hiệu ứng quay vòng
def spin_effect():
    rotations = np.linspace(0, 360 * random.randint(3, 5), 50)  # Quay nhiều vòng rồi chậm dần
    for rot in rotations:
        st.pyplot(draw_wheel(rot))
        time.sleep(0.05)  # Tạo hiệu ứng quay
    return rot

# Hàm chọn kết quả theo trọng số
def spin_wheel():
    return random.choices(segments, weights=weights, k=1)[0]

# Giao diện Streamlit
st.title("🎡 Vòng Quay May Mắn")
st.write("Nhấn nút quay để thử vận may của bạn!")

# Hiển thị vòng quay ban đầu
st.pyplot(draw_wheel())

# Nút quay vòng
if st.button("🎯 Quay Ngay!"):
    final_rotation = spin_effect()  # Hiệu ứng quay
    result = spin_wheel()
    st.success(f"Kết quả quay: **{result}** 🎉")

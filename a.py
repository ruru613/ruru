import streamlit as st
import pickle
from pathlib import Path

# 加载模型
model_path = Path(__file__).parent / "catscats.pkl"
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    st.success("模型加载成功！")
except Exception as e:
    st.error(f"加载模型失败: {e}")

# 测试预测
if st.button("测试模型"):
    st.write(model.predict([[1, 2, 3]]))  # 示例输入
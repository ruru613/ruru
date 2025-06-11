import streamlit as st
import pathlib
from fastai.learner import load_learner
import sys

# Python 版本检查
if sys.version_info >= (3, 13):
    st.error("⚠️ 当前 Python 版本为 3.13+，可能与 fastai 不兼容。建议使用 Python 3.11。")
    st.stop()

@st.cache_resource
def load_model():
    """加载并缓存模型"""
    # Windows 路径兼容性处理
    temp = None
    if sys.platform == "win32":
        temp = pathlib.PosixPath
        pathlib.PosixPath = pathlib.WindowsPath
    
    try:
        model_path = pathlib.Path(__file__).parent / "catscats.pkl"
        model = load_learner(model_path)
    finally:
        # 恢复原始设置
        if sys.platform == "win32" and temp is not None:
            pathlib.PosixPath = temp
    
    return model

# 主应用
st.title("图像分类应用")
st.write("上传一张图片，应用将预测对应的标签。")

model = load_model()

def main():
    st.title("Desert cat, Mainecoon, Siberian Cats分类器")
    st.write("上传一张图片，看看它是 Desert cat, Mainecoon还是 Siberian Cats!")
    
    # 调用加载模型函数，名称要和定义的一致
    model = safe_load_model()
    if model:
        # 这里可添加上传图片、模型推理等后续逻辑
        uploaded_file = st.file_uploader("上传图片", type=["jpg", "png"])
        if uploaded_file:
            # 示例：假设有推理逻辑，这里简单打印
            st.success("模型加载成功，可上传图片进行分类啦")

if __name__ == "__main__":
    main()




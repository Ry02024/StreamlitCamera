import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("画像認識アプリ")
st.write("オリジナルの画像認識モデルを使って何の画像かを判定します。")

st.write("")

def capture_image():
    img_file = st.camera_input("カメラで撮影")
    if img_file is not None:
        img = Image.open(img_file)
        st.image(img, caption="撮影された画像", use_column_width=True)
        return img
    return None

def upload_image():
    img_file = st.file_uploader("画像を選択してください。", type=["png", "jpg"])
    if img_file is not None:
        img = Image.open(img_file)
        st.image(img, caption="アップロードされた画像", use_column_width=True)
        return img
    return None

img_source = st.radio("画像のソースを選択してください。",
                      ("画像をアップロード", "カメラで撮影"))

if img_source == "画像をアップロード":
    img = upload_image()
elif img_source == "カメラで撮影":
    img = capture_image()

if img is not None:
    # ここに画像の予測処理を追加する
    st.write("画像がアップロードされました。")

import streamlit as st
from  PIL import Image

with st.expander("Camera"):
    camera_image=st.camera_input("Camera")

if camera_image:
    st.image(camera_image)
    img = Image.open(camera_image)
    grey_img = img.convert("L")
    st.image(grey_img)


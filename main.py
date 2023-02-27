import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def image_making():
    for i in range(7):
        image = Image.open(f'{i+1}.png')
        st.image(image)

def process_image():
    image = Image.open("process.png")
    st.image(image, caption="2/27일자 에상 프로세스")   
    
    
def main():
    st.title("AI 서비스 개발 프로젝트 기획안")
    st.subheader("시각 장애인을 위한 고지서 해석 서비스:scroll:")
    st.markdown("- 2조 : 김의석(조장) 김수윤 고준성 박진호 이한재 최성주")
    st.markdown("------")
    st.subheader("Concept")
    image_making()
    st.markdown("----")
    st.markdown('''2022년 4월 20일 장애인의 날 뉴스입니다.
                \n시각장애인을 대상으로 바코드를 이용해 고지서의 내용을 음성
                전환해주는 서비스가 있습니다.
                \n하지만 뉴스의 내용과 같이 무용지물이라고 합니다.
                ''')
    st.markdown("-----")
    st.subheader("process")
    process_image()
    
    
if __name__ == "__main__":
    main()
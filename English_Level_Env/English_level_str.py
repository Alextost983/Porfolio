import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px
from urllib.request import urlopen
import json

st.title('Английский по фильмам для всех уровней')
st.markdown('### Выбери подходящий иди загрузи свой')

st.text('Выбери подходящий иди загрузи свой')

# Ползун для определения уровня
x = st.slider('x')
st.write(x/2, 'squared is', x * x)
#таблица
df = pd.DataFrame({
  'Название фильма': ['Охота', 'Рыбалка', 'Музыка', 'Игры'],
  'Уровень языка': ['B1','B2','C1','C2']
})
st.write(df)
#График
st.markdown('### Наслаждайся любимым фильмом с пользой')
st.markdown('#### Популярность жанров')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a2', 'b2', 'c1'])

st.line_chart(chart_data)  

with open("file.srt", "r") as file: text = file.read()
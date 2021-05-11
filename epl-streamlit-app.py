import streamlit as st
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import RendererAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")


_lock = RendererAgg.lock
plt.style.use('default')

# SETUP ------------------------------------------------------------------------

st.set_page_config(page_title='Premier League Dashboard',
                   page_icon='https://sortitoutsi.net/uploads/megapacks/cutoutfaces/originals/12.00/85128159.png',
                   layout="wide")

st.title('Premier League Dashboard')

#write in data


# ------------------------------------------------------------------------------

add_selectbox = st.sidebar.multiselect(
    'Which years would you like to explore?',
    [15, 16, 17, 18, 19, 20]
)

if 15 in add_selectbox:
    st.write('15!')


df = pd.DataFrame({'col1': [1, 2, 3]})
df

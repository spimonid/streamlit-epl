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
                   page_icon='https://sortitoutsi.net/uploads/megapacks/cutoutfaces/originals/13.00/92020288.png',
                   layout="wide")


# write in data


def get_data():
    data_ = pd.read_csv(
        "https://github.com/spimonid/streamlit-epl/blob/main/20_21_master.csv?raw=True").drop(columns='Unnamed: 0')
    return data_


data = get_data()
# ------------------------------------------------------------------------------
row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.beta_columns(
    (.1, 1.5, 1.5, 1, .1)
)

row1_1.title('Premier League Dashboard')

with row1_2:
    st.write('')
    row1_2.subheader(
        'A Web App by [daniel spimoni](https://twitter.com/mr5phere)')

with row1_1:
    choice = st.radio('choose a module',
                      ('Player',
                       'Team',
                       'Week'))
    if choice == 'By_Team':
        st.write('by team')

    players = st.multiselect('Select player(s): ', data.Player_FBR.unique())
    stats = st.multiselect('Select stats: ', data.columns)
    # stats.unshift()
    st.dataframe(data[data.Player_FBR.isin(players)]
                 [['Player_FBR'] + [stat for stat in stats] + ["Fantrax_Date"]])
    # ax = sns.swarmplot(x='Player_FBR', y='Goals', data=data)


# @st.cache(allow_output_mutation=True)
# add_selectbox = st.sidebar.multiselect(
#     'Which years would you like to explore?',
#     [15, 16, 17, 18, 19, 20]
# )

# if 15 in add_selectbox:
#     st.write('15!')

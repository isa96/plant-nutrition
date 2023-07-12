import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


# Load data dengan pandas dan assign ke variabel df
df = pd.read_excel('aria_data.xlsx')

def run() :
    # Membuat Title 
    st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
    st.write('Berikut adalah EDA dari setiap feature')

    # Membuat Sub Header
    st.subheader('**Distribution Plot**')
    pilihan = st.selectbox('**Silahkan pilih column :** ',('v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'target'))
    fig = plt.figure(figsize=(20,10))
    sns.histplot(df[pilihan],bins=30,kde=True)
    title = 'Distribution Plot ' + pilihan
    plt.title(title, fontsize=20)
    plt.xlabel(pilihan, fontsize=14)
    plt.ylabel('Counts', fontsize=14)
    st.pyplot(fig)

    # Membuat Sub Header
    st.subheader('**Heatmap Correlation**')
    st.write('Berikut Heatmap Correlation antar feature')
    fig = plt.figure(figsize=(15,10))
    sns.heatmap(df.corr(), annot = True, color = 'blue', cmap = 'YlGn')
    st.pyplot(fig)

    # Membuat Sub Header
    st.subheader('**Distribusi Sample Type**')
    st.write('Berikut visualisasi distribusi sample type dengan barchart dan piechart (persentase)')
    # Visualisasi
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='sample_type', data=df, palette="winter", ax=ax[0])
    ax[0].set_xlabel("Lab", fontsize= 12)
    ax[0].set_ylabel("# of Tested Plant", fontsize= 12)
    fig.suptitle('Count of Tested Plant in each Lab', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,110)

    ax[0].set_xticks([0,1], ['Lab 1', 'Lab 2'], fontsize = 11)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+2), ha='center', va='center',fontsize = 11) 
    df['sample_type'].value_counts().plot(kind='pie', labels = ['Lab 1','Lab 2'],autopct='%1.1f%%',explode = [0,0.05] ,colors = ['indigo','salmon'],textprops = {"fontsize":12})
    ax[1].set_ylabel("% of Tested Plant", fontsize= 12)
    st.pyplot(fig)

    # Membuat Sub Header
    st.subheader('**Distribusi Sample Type berdasarkan target**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- Lab 1 sering menguji tanaman dengan tingkat nutrisi 4.6 - 4.85')
    st.markdown('- Lab 2 sering menguji tanaman dengan tingkat nutrisi 4.5 - 5')
    # Visualisasi
    fig = plt.figure(figsize=(15,8))
    sns.boxenplot(y=df['target'], x= df['sample_type'], palette = 'Blues')
    plt.title('Sample Type vs Target', fontsize = 15)
    st.pyplot(fig)

if __name__ == '__main__':
    run()
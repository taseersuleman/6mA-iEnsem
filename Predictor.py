import numpy as np
import pandas as pd
import streamlit as st
from Bio import SeqIO
import math
import csv
import pickle
from PIL import Image
from sklearn.preprocessing import StandardScaler

st.title(
    """
               6mA-iEnsem: Predictor for 6-Methyladenosine Sites
"""
)
st.subheader("""N6-methyladenosine (6mA) is the most common internal modification in eukaryotic mRNA. Mass spectrometry and site-directed mutagenesis, two of the most common conventional approaches, have been shown to be laborious and challenging. In recent years, there has been a rising interest in analyzing RNA sequences to systematically investigate mutated locations. Using novel methods for feature development, the current work aimed to identify 6mA locations in RNA sequences. Following the generation of these novel features, they were used to train an ensemble of models using methods such as blending, boosting, and bagging. The trained ensemble models were assessed using an independent test set and k-fold cross validation. When compared to baseline predictors, the suggested model performed better and showed improved ratings across the board for key measures of accuracy.
""")

#---------------------------------#
image = Image.open('flow.png')
st.image(image)

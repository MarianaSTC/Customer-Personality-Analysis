from django.shortcuts import render
import matplotlib.pyplot as plt
from .forms import UploadFileForm
from io import BytesIO
import base64
import numpy as np
import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from yellowbrick.cluster import KElbowVisualizer
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import AgglomerativeClustering
from matplotlib.colors import ListedColormap
from sklearn import metrics
import warnings
import sys

def my_view(request):
    # Specify the path to your CSV file
    file_path = r'C:\Users\maria\projet_clustering\data.csv'
    
    # Read the CSV file into a DataFrame
    data = pd.read_csv(file_path, sep=';')

    # Perform your data analysis here
    # Create a plot
    # Perform your data analysis here
    corr_matrix = data.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    # Set up the matplotlib figure
    plt.figure(figsize=(18, 18))

    # Draw the heatmap with the mask
    sns.heatmap(corr_matrix, mask=mask, cmap='coolwarm', vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt=".1f")

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()  # Close the figure to prevent it from being displayed in the notebook or script
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

 # Encode the image in base64 and remove the b'' part
    graphic = base64.b64encode(image_png).decode('utf-8')


    # Prepare and pass results or necessary data to your template
    context = {
        # Include any context variables here, for example:
        # 'data_summary': df.describe(),
    }
    return render(request, 'your_template.html', context)
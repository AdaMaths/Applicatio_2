import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def analyse_csv(fichier_path):
    df = pd.read_csv(fichier_path)
    stats = df.describe().round(2).to_html(classes="table table-bordered")

    # Générer un histogramme de la 1re colonne numérique
    col = df.select_dtypes(include='number').columns[0]
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True)
    image_path = "media/hist.png"
    plt.title(f"Distribution de {col}")
    plt.tight_layout()
    plt.savefig(image_path)
    plt.close()

    return stats, image_path
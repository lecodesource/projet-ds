import pandas as pd

def suppprimer_lignes_vides(df):
    """
    Supprime les lignes imcomplètes.

    """
    return df.dropna().reset_index(drop=True)
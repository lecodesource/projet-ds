import pandas as pd


def suppprimer_lignes_vides(df):
    """
    Supprime les lignes imcomplètes.

    """
    return df.dropna().reset_index(drop=True)


def ajouter_ligne_vides(df):
    """
    Ajoute des lignes vides.

    """
    return df.append(pd.Series(), ignore_index=True)

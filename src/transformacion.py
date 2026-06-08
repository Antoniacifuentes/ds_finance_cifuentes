from matplotlib import pyplot as plt
from scipy.stats import f_oneway, mannwhitneyu, kruskal, levene, bartlett
from scipy.optimize import minimize
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import seaborn as sns
import yfinance as yf
import pandas as pd
import numpy as np

sns.set_style("dark")
np.random.seed(20260607)


def calcular_retornos_simples(precios):
    """
    Calcula retornos simples diarios.
    """
    return precios.pct_change().dropna()

def calcular_retornos_log(precios):
    """
    Calcula retornos logarítmicos diarios.
    """
    return np.log(precios / precios.shift(1)).dropna()

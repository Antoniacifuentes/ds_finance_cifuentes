import yfinance as yf
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize
from scipy.stats import f_oneway, mannwhitneyu, kruskal, levene, bartlett
from scipy.optimize import minimize
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def descargar_datos_mercado(start="2014-01-01", end="2024-12-31"):

    datos = yf.download(
        ["^GSPC", "^VIX"],
        start=start,
        end=end,
        interval="1mo",
        auto_adjust=True,
        progress=False
    )["Close"]

    datos.columns = ["SP500", "VIX"]

    return datos.dropna()


def preparar_datos_regresion(datos):

    datos = datos.copy()

    datos["ret_sp500"] = datos["SP500"].pct_change()
    datos["delta_vix"] = datos["VIX"].diff()

    return datos.dropna()


def estimar_regresion_simple(datos):

    y = datos["delta_vix"]

    X = sm.add_constant(datos["ret_sp500"])

    modelo = sm.OLS(y, X).fit()

    return modelo
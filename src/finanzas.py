import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def descargar_datos_yf(tickers, start, end):

    datos = yf.download(
        tickers,
        start=start,
        end=end
    )["Close"]

    return datos


def calcula_retornos(df):

    retornos = df.pct_change().dropna()

    return retornos


def resumen_estadistico_retornos(df):

    resumen = pd.DataFrame({
        "Media": df.mean(),
        "Volatilidad": df.std(),
        "Asimetria": df.skew(),
        "Kurtosis": df.kurtosis(),
        "Maximo": df.max(),
        "Minimo": df.min()
    })

    return resumen


def plot_retornos(df):

    for activo in df.columns:

        fig, axes = plt.subplots(1, 3, figsize=(18, 5))

        # Serie temporal
        axes[0].plot(df.index, df[activo])
        axes[0].set_title(f"Serie de Retornos - {activo}")

        # Histograma
        sns.histplot(
            df[activo],
            bins=40,
            kde=True,
            ax=axes[1]
        )

        axes[1].set_title(f"Histograma - {activo}")

        # Boxplot
        sns.boxplot(
            y=df[activo],
            ax=axes[2]
        )

        axes[2].set_title(f"Boxplot - {activo}")

        plt.tight_layout()
        plt.show()
import numpy as np
import pickle
import matplotlib
import matplotlib.pyplot as plt
import string
import random

def compare_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                 xlabel: str,ylabel:str,title:str,label1:str,label2:str):
    """Funkcja służąca do porównywania dwóch wykresów typu plot. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    label1(str): nazwa serii z pierwszego wykresu,
    label2(str): nazwa serii z drugiego wykresu.

    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 3 
    """
    if x1.shape != y1.shape or  min(x1.shape)==0 or x2.shape != y2.shape or min(x2.shape)==0:
        return None

    fig, ax = plt.subplots()
    ax.plot(x1,y1,'b',linewidth=4,label=label1)
    ax.plot(x2,y2,'r',linewidth=2,label=label2)
    ax.set(title=title,xlabel=xlabel,ylabel=ylabel)
    plt.legend()
    # plt.title(title)
    # plt.xlabel(xlabel)
    # plt.ylabel(ylabel)
    return fig



    

def parallel_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                  x1label:str,y1label:str,x2label:str,y2label:str,title:str,orientation:str):

    if x1.shape != y1.shape or  min(x1.shape)==0 or x2.shape != y2.shape or min(x2.shape)==0:
        return None


    if orientation != 'h' and orientation != 'v':
        return None

    if orientation  == 'v':
        fig = plt.figure()
        ax1 = fig.add_subplot(1,2,1)
        ax2 = fig.add_subplot(1,2,2)
    if orientation  == 'h':
        fig=plt.figure()
        ax1 = fig.add_subplot(2,1,1)
        ax2 = fig.add_subplot(2,1,2)
        


    ax1.plot(x1,y1)
    ax1.set(xlabel=x1label,ylabel=y1label,title=title)

    ax2.plot(x2,y2)
    ax2.set(xlabel=x2label,ylabel=y2label)
    return fig





def log_plot(x:np.ndarray,y:np.ndarray,xlabel:np.ndarray,ylabel:str,title:str,log_axis:str):
    """Funkcja służąca do tworzenia wykresów ze skalami logarytmicznymi. 
    Szczegółowy opis w zadaniu 7.
    
    Parameters:
    x(np.ndarray): wektor wartości osi x,
    y(np.ndarray): wektor wartości osi y,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    log_axis(str): wartość oznacza:
        - 'x' oznacza skale logarytmiczną na osi x,
        - 'y' oznacza skale logarytmiczną na osi y,
        - 'xy' oznacza skale logarytmiczną na obu osiach.
    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x,y) zgody z opisem z zadania 7 
    """
    if x.shape != y.shape or  min(x.shape)==0:
        return None
    if log_axis != 'x' and log_axis != 'y' and log_axis != 'xy':
        return None
    fig, ax = plt.subplots()

    ax.plot(x, y)
    ax.set(xlabel=xlabel,ylabel=ylabel,title=title)
    if log_axis== 'x':
        ax.semilogx()
    if log_axis == 'y':
        ax.semilogy()
    if log_axis == 'xy':
        ax.loglog()

    return fig


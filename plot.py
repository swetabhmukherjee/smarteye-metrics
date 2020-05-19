#!/usr/bin/env python
# coding: utf-8
# Author : Swetabh

# In[1]: Imports

import pandas as pd
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import datetime as dt
from dateutil.relativedelta import relativedelta

register_matplotlib_converters()

# In[2]: CSV Operations

_csv = pd.read_csv('result.csv', index_col=False)
date = _csv['Date'].tolist()
total_images = _csv['Proxies Identified'].tolist()
precision = _csv['Precision'].tolist()
recall = _csv['Recall'].tolist()


# In[3]: Plot


def _plot(time_range="Last Week", _end=None):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    _date = [datetime.strptime(d, '%d/%m/%Y') for d in date]
    ax1.plot_date(_date, total_images, 'r-', label='Total Images')
    ax2.plot_date(_date, recall, 'g-', label='Recall')
    ax2.plot_date(_date, precision, 'b-', label='Precision')
    ax1.set_ylim([25, 80])
    ax2.set_ylim([0.3, 1.0])
    ax1.set_ylabel('Total Images Processed', color='black')
    ax2.set_ylabel('Precision | Recall', color='black')
    if _end is not None:
        fig.suptitle('Plot for Date Range: '+time_range+' to '+_end)
    else:
        fig.suptitle('Plot for '+time_range)
    fig.legend(loc='upper right')
    x_dates = mdates.DateFormatter('%d/%m/%Y')
    ax1.xaxis.set_major_formatter(x_dates)
    plt.gcf().autofmt_xdate()
    if _end is not None:
        start_date = dt.datetime.strptime(time_range, '%d/%m/%Y')
        end_date = dt.datetime.strptime(_end, '%d/%m/%Y')
        ax1.set_xlim(start_date, end_date)
        plt.show()

    else:
        start_date, end_date = _custom_date(time_range)
        ax1.set_xlim(start_date, end_date)
        plt.show()


def _custom_date(time_range):
    today = dt.date.today()
    start = ''
    end = ''
    # if time_range == 'last week' or time_range == 'Last Week':
    #     start_date = today - relativedelta(days=7)
    #     end_date = today - relativedelta(days=1)
    #     return start_date, end_date
    if time_range == 'last month' or time_range == 'Last Month':
        start = today - relativedelta(months=1)
        start_date = dt.date(start.year, start.month, 1)
        end_date = dt.date(today.year, today.month, 1) - relativedelta(days=1)
        return start_date, end_date
    elif time_range == 'this month' or time_range == 'This Month':
        start_date = today - relativedelta(days=(today.day - 1))
        end_date = today - relativedelta(days=1)
        return start_date, end_date
    else:
        start_date = today - relativedelta(days=7)
        end_date = today - relativedelta(days=1)
        return start_date, end_date


# In[5]: Main Function

# Default plot : Last Week
if __name__ == '__main__':
    _plot()

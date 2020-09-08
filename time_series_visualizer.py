import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = ['date'], index_col = 'date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
  fig, ax = plt.subplots()

    #Set height and width
  fig.set_figheight(5)
  fig.set_figwidth(15)

    #Set title
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    #Set labels
  plt.xlabel("Date")
  plt.ylabel("Page Views") 

    #Setting color
  plt.plot(df.index, df['value'], color='r')   

    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df["month"] = df.index.month
    df["year"] = df.index.year
    df_bar = df.groupby(["year", "month"])["value"].mean()
    df_bar = df_bar.unstack()
    
    # Draw bar plot

    fig = df_bar.plot(kind ="bar", legend = True, figsize = (15,10)).figure
    plt.xlabel("Years", fontsize = 15)
    plt.ylabel("Average Page Views", fontsize = 15)
    plt.legend(labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title = 'Months', fontsize = 12)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, ax = plt.subplots(1,2, figsize = (10,5))

    # Years box plot
    d1 = sns.boxplot(x='year', y='value', data=df_box, ax = ax[0])
    d1.set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")

    # Months box plot
   
    d2 = sns.boxplot(x='month', y='value', data=df_box, order =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax = ax[1])
    d2.set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

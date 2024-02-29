#draw bar chart from given data
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def main():
   vary()

def normak():
    years=[1950,1960,1970,1980,2000,2010]
    gdp=[300.2,543,1075.9,400,2000,1200]
    plt.plot(years,gdp,color='green',marker='o',linestyle='solid')
    plt.title("Data Science")
    plt.ylabel("Billions of $")
    plt.xlabel("years")
    plt.show()

def bar():
    #Bar chart
    movies=["extraction","matrix resurec","home alone","magnus","knights"]
    num_oscars=[23,15,32,12,76]
    xs=[i+0.1 for i,_ in enumerate(movies)]
    plt.bar(xs,num_oscars)
    plt.ylabel("Awards")
    plt.title("Movies")
    plt.xlabel("names")
    plt.xticks([i+0.5 for i, _ in enumerate(movies)],movies)
    plt.show()
def vary():
  variance=[1,2,4,8,16,32,64,128,256]
  bias_squared=[256,128,64,32,16,8,4,2,1]
  total_error=[x+y for x,y in zip(variance,bias_squared)]
  xs=[i for i,_ in enumerate(variance)]
  plt.plot(xs,variance, 'g-',label='variance')
  plt.plot(xs,bias_squared,'r-.',label='bias**2')
  plt.plot(xs,total_error,'b:', label='total error')
  plt.legend(loc=9)
  plt.xlabel("Model Complexity")
  plt.title("The bias-Variance Tradeoff")
  plt.show()
main()

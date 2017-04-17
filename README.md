# Big-Data-Final-Project
Big Data Final Project for ds-ga-1004

In this project, we use _311 Complaints from 2009 to 2016_ ([2009](https://data.cityofnewyork.us/Social-Services/new-311/9s88-aed8), [2010-2016](https://data.cityofnewyork.us/Social-Services/311/wpe2-h2i5)) as the main dataset. We first do data cleaning, exploring every column of the complaint dataset. Then, selecting several informative fields, we generate an overview of the data, and plot figures to make data more visible. Furthermore, we try combining other datasets to make reasonable explanations/hypotheses for some phenomenon in previous data analysis.

## Getting Started

These instructions will get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

**1. original 311 complaint data**
[311 complaints in 2009](https://data.cityofnewyork.us/Social-Services/new-311/9s88-aed8)
[311 complaints from 2010 to 2016](https://data.cityofnewyork.us/Social-Services/311/wpe2-h2i5)

**2. a Spark environment**
Spark is available on NYU dumbo.

**3. Anaconda installed**
[Anaconda Installer](https://www.continuum.io/downloads)

## Data Cleaning

The data cleaning park is done on Spark.
**To-Do**

## Plotting Figures

### Plotting environment

We use conda as our package and environment system, thus avoiding any inconsistency problem.

You can configure the project environment by

`./config.sh`

Then You can switch into our project environment by

`source activate bigdata`
or switch out by
`source deactivate`

When you see `(bigdata)` at the head of your command line prompt, you are in our project environment. Conda helps keep consistancy issues.

### Plotting program

We write our plotting program in Jupyter Notebook, which is built in Anaconda.

To open Jupyter Notebook in local host, please type in your command line

`(bigdata) your-machine-name$ jupyter notebook`

Our plotting program is in **311_playground.ipynb**. You can run it cell by cell to get figures. The output figures are located in **To-Do**

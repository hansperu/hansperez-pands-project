# Project Programming and Scripting

## The Irsis Flower data set

**Student:** Hans Pérez Rubín de Celis

**Student ID number:** G00387884


## 1.Projet Plan.
This project concerns the well-known Fisher’s Iris data set. You must research the data set and write documentation and code in Python to investigate it. 

## 2.- The Problem to solve.
You are expected to be able to break this project into several smaller tasks that are easier to solve, and to plug these together after they have been completed. 

## 3.- Methodology to follow
The methodology for software development in software engineering is a framework used to structure, plan and control the development process in information systems.

Basically the point here is to control the development process so that it is orderly and in this way as productive as possible.

This project has been developed fulfilling the following objectives:

### 3.1. Research the data set online and write a summary about it in your README.

### 3.2. Download the data set and add it to your repository.

### 3.3. Write a program called analysis.py that:
   
* outputs a summary of each variable to a single text file,

* saves a histogram of each variable to png files, and

* outputs a scatter plot of each pair of variables.

## I. Introduction.
The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus". 
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

In order to support this project, we have previously had to see the documentation and videos provided by both Prof. Andrew Beatty and Prof. Ian McLoughlin.
* [What is a program or script?](https://web.microsoftstream.com/video/025ef713-d7c8-492f-97f4-5590015da029)
* [GitHub workshop](https://web.microsoftstream.com/video/30318f36-5aaf-4827-8262-cd91b89a2644)

## II. Bibliographic Research Process.

Thanks to the database offered by the GMIT library and the information provided in the instructions document where we are instructed to start the research process from the UC Irvine Machine Learning Repository. [Iris data set](http://archive.ics.uci.edu/ml/datasets/Iris).

In the GMIT library database we have found more than 150 scientific articles and books that refer to Ronald Fisher. The results offered by the repository as a document are attached in a separate document.
 
There has been a detailed investigation of Fisher's Iris dataset, for example: In the GMIT library database we have selected three books.

The three etitles below (use the advanced search option in search + search. Enter the Python script and the iris dataset) refer to Fisher's iris dataset. Just use the 'search inside' function on each title and key in the iris dataset.

#### [Python Machine Learning - Second Edition](http://search.ebscohost.com/login.aspx?direct=true&AuthType=ip,sso&db=nlebk&AN=1606531&site=eds-live&scope=site&custid=s2873033&ebv=EB&ppid=pp_9)
Author:Raschka, Sebastian, Mirjalili, Vahid

![book1](https://user-images.githubusercontent.com/60121637/82153453-66aab500-985f-11ea-881a-fd5e2bbd3c8e.png)

#### [Mastering Social Media Mining with Python](http://search.ebscohost.com/login.aspx?direct=true&AuthType=ip,sso&db=e000xww&AN=1295360&site=eds-live&scope=site&custid=s2873033&ebv=EB&ppid=pp_32)
Author: Bonzanini, Marco

![book2](https://user-images.githubusercontent.com/60121637/82153488-a40f4280-985f-11ea-9b14-a7f0f4cf5d67.png)

#### [Python Data Science Essentials - Second Edition](http://search.ebscohost.com/login.aspx?direct=true&AuthType=ip,sso&db=e000xww&AN=1409191&site=eds-live&scope=site&custid=s2873033&ebv=EB&ppid=pp_Cover)
Author: Boschetti, Alberto, Massaron, Luca

![book3](https://user-images.githubusercontent.com/60121637/82153641-a756fe00-9860-11ea-8245-e15e478f1450.png)

#### Some journal articles:

Advanced search in search+find: iris dataset AND python programming language.  Limit to academic journals. Retrieves 4.  First 3 reference iris data set and give examples of code? Use CTRL F within the article and search for iris dataset.

These article are from Science Direct database so perhaps search that individual database only from our list of databases on library homepage.
Keyword search: iris datset and python script.  You will retrieve circa 68 results and you can limit them by subscribed journals(full text), pub title, date, article type.

A detailed research has also been done in Google Academico and has given us a result of 1350 articles and texts that refer to "Fisher’s Iris dataset + Python"

![image](https://user-images.githubusercontent.com/60121637/82152697-04e84c00-985b-11ea-9309-1e40e105c8b5.png)

The following table depicts an excerpt of the Iris dataset, which is a classic example in the field of machine learning. The Iris dataset contains the measurements of 150 Iris flowers from three different species—Setosa, Versicolor, and Virginica. Here, each flower sample represents one row in our dataset, and the flower measurements in centimeters are stored as columns, which we also call the features of the dataset:

![image](https://user-images.githubusercontent.com/60121637/82152976-a6bc6880-985c-11ea-9b17-427217a9c22b.png)

The following images have been compiled from the book Python Machine Learning by the author Raschka, Sebastian, Hirjalili, Vahid (Sencod Edition).

![image](https://user-images.githubusercontent.com/60121637/82153749-5e537980-9861-11ea-85b6-d2567e2435fd.png)

![image](https://user-images.githubusercontent.com/60121637/82153789-8c38be00-9861-11ea-8fbf-d98dc90f1ce3.png)

## III. Programming and scripting process.

### Technology
* Anaconda
* Python 3.8.2
* Visual Studio Code: March 2020 (version 1.44)
* Git 2.26.1
* Gihub
* GDB Online is an online compilation and debugging tool for Anaconda, Python,compile, run and debug online from anywhere in the world.
* Operating system: Ubuntu 19.10 - Windows 10 Pro - 64 bit

### Hardware requirements
- Number of cores: 4
- Release date: Intel (R) Core (TM) i7-4790 CPU
- RAM 8.00 GB
- Clock frequency: 3.6 GHz
- CPU Benchmark Score: 1833

### Objective of the project.

The main objective of this project to work with the Fisher dataset using machine learning and for this we will use Python.
The main Python package for machine learning is scikit-learn. It is an open source collection of machine learning algorithms that include tools to access and preprocess data, evaluate the output of an algorithm, and visualize the results.

Previously we will install [Anaconda](https://www.anaconda.com/products/individual) which is the most complete Suite for Data Science with Python.

You can install scikit-learn with the common procedure through CheeseShop:

`$ pip install scikit-learn`

![image](https://user-images.githubusercontent.com/60121637/82154218-3f0a1b80-9864-11ea-9278-c73e30a151b3.png)

The data that we're using is called the Fisher's Iris dataset, also referred to as Iris flower dataset. It was introduced in the 1930s by Ronald Fisher and it's today one of the classic datasets: given its small size, it's often used in the literature for toy examples. The dataset contains 50 samples from each of the three species of Iris, and for each sample four features are reported: the length and width of petals and sepals.

The dataset is commonly used as a showcase example for classification as the data comes with the correct labels for each sample, while its application for clustering is less common, mainly because there are just two well-visible clusters with a rather obvious separation. Given its small size and simple structure, it makes the case for a gentle introduction to data analysis with scikit-learn.

To visualize the data we will install matplotlib library with

`$ pip install matplotlib`

![image](https://user-images.githubusercontent.com/60121637/82154298-be97ea80-9864-11ea-8bfd-daff946fa271.png)

The next phase is to open through the anaconda terminal using the following code

`$ anaconda-navigator`

![image](https://user-images.githubusercontent.com/60121637/82154614-facc4a80-9866-11ea-872b-bd2446bb6c53.png)

Once inside Anaconda we must enter Jupyter

![image](https://user-images.githubusercontent.com/60121637/82154677-58f92d80-9867-11ea-9f96-1e27f486cf9a.png)

## IV. Process of downloading the dataset and adding it to the repository.

Firstly, the dataset must be imported, for this we will use the following code:
![image](https://user-images.githubusercontent.com/60121637/82160730-4266cc80-988f-11ea-8564-bfba5ec1873f.png)
Learn more about the iris dataset: UCI Machine Learning Repository
<http://archive.ics.uci.edu/ml/datasets/Iris>

Once the file named **iris.data** has been downloaded you can verify it by opening it with Visual Studio Code, image attached.

![image](https://user-images.githubusercontent.com/60121637/82160958-d1281900-9890-11ea-9545-c4badce0379a.png)

The next step is to load the iris dataset into scikit-learn

For more information <https://scikit-learn.org/stable/datasets/>

![image](https://user-images.githubusercontent.com/60121637/82161204-a9d24b80-9892-11ea-8c9b-4bbe2628468c.png)

* Each row is an **observation** (also known as: sample, example, instance, record)
* Each column is a **characteristic** (also known as: predictor, attribute, independent variable, input, regressor, covariate)

![image](https://user-images.githubusercontent.com/60121637/82162310-75af5880-989b-11ea-8ee2-8e0b18218659.png)

* Each of the values we are predicting is the **response** (also known as: target, result, label, dependent variable).
* Therefore the **classification** is supervised learning in which the answer is categorical.
* **Regression** is supervised learning in which the response is orderly and continuous.

Once this process is finished we must save the commands used in Jupyter with the name **"analisys.py"**

![image](https://user-images.githubusercontent.com/60121637/82198306-06198780-98f4-11ea-8ddf-2f71fd900fa6.png)

## V. Data visualization

First of all we must import [Matplotlib.pyplot](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.html) is a state-based interface to matplotlib. It provides a MATLAB-like way of plotting.

Pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation:

`import numpy as np`

`import matplotlib.pyplot as plt`

`x = np.arange(0, 5, 0.1)`

`y = np.sin(x)`

`plt.plot(x, y)`

We must also import [sklearn.datasets](https://scikit-learn.org/stable/index.html)

* Simple and efficient tools for predictive data analysis.

* Accessible to all and reusable in various contexts. Built on NumPy, SciPy and matplotlib

* Open source, commercially usable - BSD license

To carry out this exercise we have used [Anaconda-navigator](https://www.anaconda.com/products/individual) and within this we have used Jupyter to develop in conditions and show the visualization of the iris.dataset.

![importación](https://user-images.githubusercontent.com/60121637/82268401-ca6bd580-9966-11ea-85b7-6a8f61be9dfd.png)

Once [Matplotlib.pyplot](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.html) and [sklearn.datasets](https://scikit-learn.org/stable/index.html) are imported, you must also import the iris.data and use the code:

`print (iris.data)`

![import irisdata](https://user-images.githubusercontent.com/60121637/82268745-ab217800-9967-11ea-83cd-463c8c9c6ad5.png)

Using the command shown below you can see the data divided into blocks and horizontally

`print (iris.data.T)`

![horizontal](https://user-images.githubusercontent.com/60121637/82269000-4581bb80-9968-11ea-9fae-6b3be1d4f469.png)

This command allows you to see only the data of the first block

`features = iris.data.T`

`print(features[0])`

![bloque1](https://user-images.githubusercontent.com/60121637/82269336-4ff08500-9969-11ea-8bd9-4d32d768e464.png)


This command allows you to see the characteristics of the petals and the logintudity of each one of them in the different blocks of the iris.data

`sepal_length=features[0]`

`sepal_width=features[1]`

`petal_length=features[2]`

`petal_width=features[3]`

`print(iris.feature_names)`

![caracteristicas](https://user-images.githubusercontent.com/60121637/82269474-be354780-9969-11ea-88d8-792e903dd3d5.png)


#### Graphics encoding

This command allows you to see the characteristics of the petals and the length and width of each one.

`sepal_length_label=iris.feature_names[0]`

`sepal_width_label=iris.feature_names[1]

petal_length_label=iris.feature_names[2]

petal_width_label=iris.feature_names[3]

plt.scatter(sepal_length, sepal_width, c=iris.target)

plt.xlabel(sepal_length_label)

plt.ylabel(sepal_width_label)

plt.show()`

![grafico](https://user-images.githubusercontent.com/60121637/82269643-31d75480-996a-11ea-8253-e777c8184175.png)


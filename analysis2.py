{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Matplotlib.pyplot is imported first\n",
    "#klearn.datasets is imported first\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.datasets import load_iris\n",
    "iris = load_iris()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5.1 3.5 1.4 0.2]\n",
      " [4.9 3.  1.4 0.2]\n",
      " [4.7 3.2 1.3 0.2]\n",
      " [4.6 3.1 1.5 0.2]\n",
      " [5.  3.6 1.4 0.2]\n",
      " [5.4 3.9 1.7 0.4]\n",
      " [4.6 3.4 1.4 0.3]\n",
      " [5.  3.4 1.5 0.2]\n",
      " [4.4 2.9 1.4 0.2]\n",
      " [4.9 3.1 1.5 0.1]\n",
      " [5.4 3.7 1.5 0.2]\n",
      " [4.8 3.4 1.6 0.2]\n",
      " [4.8 3.  1.4 0.1]\n",
      " [4.3 3.  1.1 0.1]\n",
      " [5.8 4.  1.2 0.2]\n",
      " [5.7 4.4 1.5 0.4]\n",
      " [5.4 3.9 1.3 0.4]\n",
      " [5.1 3.5 1.4 0.3]\n",
      " [5.7 3.8 1.7 0.3]\n",
      " [5.1 3.8 1.5 0.3]\n",
      " [5.4 3.4 1.7 0.2]\n",
      " [5.1 3.7 1.5 0.4]\n",
      " [4.6 3.6 1.  0.2]\n",
      " [5.1 3.3 1.7 0.5]\n",
      " [4.8 3.4 1.9 0.2]\n",
      " [5.  3.  1.6 0.2]\n",
      " [5.  3.4 1.6 0.4]\n",
      " [5.2 3.5 1.5 0.2]\n",
      " [5.2 3.4 1.4 0.2]\n",
      " [4.7 3.2 1.6 0.2]\n",
      " [4.8 3.1 1.6 0.2]\n",
      " [5.4 3.4 1.5 0.4]\n",
      " [5.2 4.1 1.5 0.1]\n",
      " [5.5 4.2 1.4 0.2]\n",
      " [4.9 3.1 1.5 0.2]\n",
      " [5.  3.2 1.2 0.2]\n",
      " [5.5 3.5 1.3 0.2]\n",
      " [4.9 3.6 1.4 0.1]\n",
      " [4.4 3.  1.3 0.2]\n",
      " [5.1 3.4 1.5 0.2]\n",
      " [5.  3.5 1.3 0.3]\n",
      " [4.5 2.3 1.3 0.3]\n",
      " [4.4 3.2 1.3 0.2]\n",
      " [5.  3.5 1.6 0.6]\n",
      " [5.1 3.8 1.9 0.4]\n",
      " [4.8 3.  1.4 0.3]\n",
      " [5.1 3.8 1.6 0.2]\n",
      " [4.6 3.2 1.4 0.2]\n",
      " [5.3 3.7 1.5 0.2]\n",
      " [5.  3.3 1.4 0.2]\n",
      " [7.  3.2 4.7 1.4]\n",
      " [6.4 3.2 4.5 1.5]\n",
      " [6.9 3.1 4.9 1.5]\n",
      " [5.5 2.3 4.  1.3]\n",
      " [6.5 2.8 4.6 1.5]\n",
      " [5.7 2.8 4.5 1.3]\n",
      " [6.3 3.3 4.7 1.6]\n",
      " [4.9 2.4 3.3 1. ]\n",
      " [6.6 2.9 4.6 1.3]\n",
      " [5.2 2.7 3.9 1.4]\n",
      " [5.  2.  3.5 1. ]\n",
      " [5.9 3.  4.2 1.5]\n",
      " [6.  2.2 4.  1. ]\n",
      " [6.1 2.9 4.7 1.4]\n",
      " [5.6 2.9 3.6 1.3]\n",
      " [6.7 3.1 4.4 1.4]\n",
      " [5.6 3.  4.5 1.5]\n",
      " [5.8 2.7 4.1 1. ]\n",
      " [6.2 2.2 4.5 1.5]\n",
      " [5.6 2.5 3.9 1.1]\n",
      " [5.9 3.2 4.8 1.8]\n",
      " [6.1 2.8 4.  1.3]\n",
      " [6.3 2.5 4.9 1.5]\n",
      " [6.1 2.8 4.7 1.2]\n",
      " [6.4 2.9 4.3 1.3]\n",
      " [6.6 3.  4.4 1.4]\n",
      " [6.8 2.8 4.8 1.4]\n",
      " [6.7 3.  5.  1.7]\n",
      " [6.  2.9 4.5 1.5]\n",
      " [5.7 2.6 3.5 1. ]\n",
      " [5.5 2.4 3.8 1.1]\n",
      " [5.5 2.4 3.7 1. ]\n",
      " [5.8 2.7 3.9 1.2]\n",
      " [6.  2.7 5.1 1.6]\n",
      " [5.4 3.  4.5 1.5]\n",
      " [6.  3.4 4.5 1.6]\n",
      " [6.7 3.1 4.7 1.5]\n",
      " [6.3 2.3 4.4 1.3]\n",
      " [5.6 3.  4.1 1.3]\n",
      " [5.5 2.5 4.  1.3]\n",
      " [5.5 2.6 4.4 1.2]\n",
      " [6.1 3.  4.6 1.4]\n",
      " [5.8 2.6 4.  1.2]\n",
      " [5.  2.3 3.3 1. ]\n",
      " [5.6 2.7 4.2 1.3]\n",
      " [5.7 3.  4.2 1.2]\n",
      " [5.7 2.9 4.2 1.3]\n",
      " [6.2 2.9 4.3 1.3]\n",
      " [5.1 2.5 3.  1.1]\n",
      " [5.7 2.8 4.1 1.3]\n",
      " [6.3 3.3 6.  2.5]\n",
      " [5.8 2.7 5.1 1.9]\n",
      " [7.1 3.  5.9 2.1]\n",
      " [6.3 2.9 5.6 1.8]\n",
      " [6.5 3.  5.8 2.2]\n",
      " [7.6 3.  6.6 2.1]\n",
      " [4.9 2.5 4.5 1.7]\n",
      " [7.3 2.9 6.3 1.8]\n",
      " [6.7 2.5 5.8 1.8]\n",
      " [7.2 3.6 6.1 2.5]\n",
      " [6.5 3.2 5.1 2. ]\n",
      " [6.4 2.7 5.3 1.9]\n",
      " [6.8 3.  5.5 2.1]\n",
      " [5.7 2.5 5.  2. ]\n",
      " [5.8 2.8 5.1 2.4]\n",
      " [6.4 3.2 5.3 2.3]\n",
      " [6.5 3.  5.5 1.8]\n",
      " [7.7 3.8 6.7 2.2]\n",
      " [7.7 2.6 6.9 2.3]\n",
      " [6.  2.2 5.  1.5]\n",
      " [6.9 3.2 5.7 2.3]\n",
      " [5.6 2.8 4.9 2. ]\n",
      " [7.7 2.8 6.7 2. ]\n",
      " [6.3 2.7 4.9 1.8]\n",
      " [6.7 3.3 5.7 2.1]\n",
      " [7.2 3.2 6.  1.8]\n",
      " [6.2 2.8 4.8 1.8]\n",
      " [6.1 3.  4.9 1.8]\n",
      " [6.4 2.8 5.6 2.1]\n",
      " [7.2 3.  5.8 1.6]\n",
      " [7.4 2.8 6.1 1.9]\n",
      " [7.9 3.8 6.4 2. ]\n",
      " [6.4 2.8 5.6 2.2]\n",
      " [6.3 2.8 5.1 1.5]\n",
      " [6.1 2.6 5.6 1.4]\n",
      " [7.7 3.  6.1 2.3]\n",
      " [6.3 3.4 5.6 2.4]\n",
      " [6.4 3.1 5.5 1.8]\n",
      " [6.  3.  4.8 1.8]\n",
      " [6.9 3.1 5.4 2.1]\n",
      " [6.7 3.1 5.6 2.4]\n",
      " [6.9 3.1 5.1 2.3]\n",
      " [5.8 2.7 5.1 1.9]\n",
      " [6.8 3.2 5.9 2.3]\n",
      " [6.7 3.3 5.7 2.5]\n",
      " [6.7 3.  5.2 2.3]\n",
      " [6.3 2.5 5.  1.9]\n",
      " [6.5 3.  5.2 2. ]\n",
      " [6.2 3.4 5.4 2.3]\n",
      " [5.9 3.  5.1 1.8]]\n"
     ]
    }
   ],
   "source": [
    "#using the print command you can verify the import of the iris.data data\n",
    "print(iris.data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5.1 4.9 4.7 4.6 5.  5.4 4.6 5.  4.4 4.9 5.4 4.8 4.8 4.3 5.8 5.7 5.4 5.1\n",
      "  5.7 5.1 5.4 5.1 4.6 5.1 4.8 5.  5.  5.2 5.2 4.7 4.8 5.4 5.2 5.5 4.9 5.\n",
      "  5.5 4.9 4.4 5.1 5.  4.5 4.4 5.  5.1 4.8 5.1 4.6 5.3 5.  7.  6.4 6.9 5.5\n",
      "  6.5 5.7 6.3 4.9 6.6 5.2 5.  5.9 6.  6.1 5.6 6.7 5.6 5.8 6.2 5.6 5.9 6.1\n",
      "  6.3 6.1 6.4 6.6 6.8 6.7 6.  5.7 5.5 5.5 5.8 6.  5.4 6.  6.7 6.3 5.6 5.5\n",
      "  5.5 6.1 5.8 5.  5.6 5.7 5.7 6.2 5.1 5.7 6.3 5.8 7.1 6.3 6.5 7.6 4.9 7.3\n",
      "  6.7 7.2 6.5 6.4 6.8 5.7 5.8 6.4 6.5 7.7 7.7 6.  6.9 5.6 7.7 6.3 6.7 7.2\n",
      "  6.2 6.1 6.4 7.2 7.4 7.9 6.4 6.3 6.1 7.7 6.3 6.4 6.  6.9 6.7 6.9 5.8 6.8\n",
      "  6.7 6.7 6.3 6.5 6.2 5.9]\n",
      " [3.5 3.  3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 3.7 3.4 3.  3.  4.  4.4 3.9 3.5\n",
      "  3.8 3.8 3.4 3.7 3.6 3.3 3.4 3.  3.4 3.5 3.4 3.2 3.1 3.4 4.1 4.2 3.1 3.2\n",
      "  3.5 3.6 3.  3.4 3.5 2.3 3.2 3.5 3.8 3.  3.8 3.2 3.7 3.3 3.2 3.2 3.1 2.3\n",
      "  2.8 2.8 3.3 2.4 2.9 2.7 2.  3.  2.2 2.9 2.9 3.1 3.  2.7 2.2 2.5 3.2 2.8\n",
      "  2.5 2.8 2.9 3.  2.8 3.  2.9 2.6 2.4 2.4 2.7 2.7 3.  3.4 3.1 2.3 3.  2.5\n",
      "  2.6 3.  2.6 2.3 2.7 3.  2.9 2.9 2.5 2.8 3.3 2.7 3.  2.9 3.  3.  2.5 2.9\n",
      "  2.5 3.6 3.2 2.7 3.  2.5 2.8 3.2 3.  3.8 2.6 2.2 3.2 2.8 2.8 2.7 3.3 3.2\n",
      "  2.8 3.  2.8 3.  2.8 3.8 2.8 2.8 2.6 3.  3.4 3.1 3.  3.1 3.1 3.1 2.7 3.2\n",
      "  3.3 3.  2.5 3.  3.4 3. ]\n",
      " [1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 1.5 1.6 1.4 1.1 1.2 1.5 1.3 1.4\n",
      "  1.7 1.5 1.7 1.5 1.  1.7 1.9 1.6 1.6 1.5 1.4 1.6 1.6 1.5 1.5 1.4 1.5 1.2\n",
      "  1.3 1.4 1.3 1.5 1.3 1.3 1.3 1.6 1.9 1.4 1.6 1.4 1.5 1.4 4.7 4.5 4.9 4.\n",
      "  4.6 4.5 4.7 3.3 4.6 3.9 3.5 4.2 4.  4.7 3.6 4.4 4.5 4.1 4.5 3.9 4.8 4.\n",
      "  4.9 4.7 4.3 4.4 4.8 5.  4.5 3.5 3.8 3.7 3.9 5.1 4.5 4.5 4.7 4.4 4.1 4.\n",
      "  4.4 4.6 4.  3.3 4.2 4.2 4.2 4.3 3.  4.1 6.  5.1 5.9 5.6 5.8 6.6 4.5 6.3\n",
      "  5.8 6.1 5.1 5.3 5.5 5.  5.1 5.3 5.5 6.7 6.9 5.  5.7 4.9 6.7 4.9 5.7 6.\n",
      "  4.8 4.9 5.6 5.8 6.1 6.4 5.6 5.1 5.6 6.1 5.6 5.5 4.8 5.4 5.6 5.1 5.1 5.9\n",
      "  5.7 5.2 5.  5.2 5.4 5.1]\n",
      " [0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 0.2 0.2 0.1 0.1 0.2 0.4 0.4 0.3\n",
      "  0.3 0.3 0.2 0.4 0.2 0.5 0.2 0.2 0.4 0.2 0.2 0.2 0.2 0.4 0.1 0.2 0.2 0.2\n",
      "  0.2 0.1 0.2 0.2 0.3 0.3 0.2 0.6 0.4 0.3 0.2 0.2 0.2 0.2 1.4 1.5 1.5 1.3\n",
      "  1.5 1.3 1.6 1.  1.3 1.4 1.  1.5 1.  1.4 1.3 1.4 1.5 1.  1.5 1.1 1.8 1.3\n",
      "  1.5 1.2 1.3 1.4 1.4 1.7 1.5 1.  1.1 1.  1.2 1.6 1.5 1.6 1.5 1.3 1.3 1.3\n",
      "  1.2 1.4 1.2 1.  1.3 1.2 1.3 1.3 1.1 1.3 2.5 1.9 2.1 1.8 2.2 2.1 1.7 1.8\n",
      "  1.8 2.5 2.  1.9 2.1 2.  2.4 2.3 1.8 2.2 2.3 1.5 2.3 2.  2.  1.8 2.1 1.8\n",
      "  1.8 1.8 2.1 1.6 1.9 2.  2.2 1.5 1.4 2.3 2.4 1.8 1.8 2.1 2.4 2.3 1.9 2.3\n",
      "  2.5 2.3 1.9 2.  2.3 1.8]]\n"
     ]
    }
   ],
   "source": [
    "#Using this command you can see the data divided into blocks and horizontally\n",
    "print(iris.data.T)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5.1 4.9 4.7 4.6 5.  5.4 4.6 5.  4.4 4.9 5.4 4.8 4.8 4.3 5.8 5.7 5.4 5.1\n",
      " 5.7 5.1 5.4 5.1 4.6 5.1 4.8 5.  5.  5.2 5.2 4.7 4.8 5.4 5.2 5.5 4.9 5.\n",
      " 5.5 4.9 4.4 5.1 5.  4.5 4.4 5.  5.1 4.8 5.1 4.6 5.3 5.  7.  6.4 6.9 5.5\n",
      " 6.5 5.7 6.3 4.9 6.6 5.2 5.  5.9 6.  6.1 5.6 6.7 5.6 5.8 6.2 5.6 5.9 6.1\n",
      " 6.3 6.1 6.4 6.6 6.8 6.7 6.  5.7 5.5 5.5 5.8 6.  5.4 6.  6.7 6.3 5.6 5.5\n",
      " 5.5 6.1 5.8 5.  5.6 5.7 5.7 6.2 5.1 5.7 6.3 5.8 7.1 6.3 6.5 7.6 4.9 7.3\n",
      " 6.7 7.2 6.5 6.4 6.8 5.7 5.8 6.4 6.5 7.7 7.7 6.  6.9 5.6 7.7 6.3 6.7 7.2\n",
      " 6.2 6.1 6.4 7.2 7.4 7.9 6.4 6.3 6.1 7.7 6.3 6.4 6.  6.9 6.7 6.9 5.8 6.8\n",
      " 6.7 6.7 6.3 6.5 6.2 5.9]\n"
     ]
    }
   ],
   "source": [
    "#This command allows you to see only the data of the first block\n",
    "features = iris.data.T\n",
    "print(features[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']\n"
     ]
    }
   ],
   "source": [
    "#This command allows you to see the characteristics of the petals and the logintudity of each one of them in the different blocks of the iris.data\n",
    "sepal_length=features[0]\n",
    "sepal_width=features[1]\n",
    "petal_length=features[2]\n",
    "petal_width=features[3]\n",
    "\n",
    "print(iris.feature_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Graphics encoding\n",
    "#This command allows you to see the characteristics of the petals and the length and width of each one.\n",
    "sepal_length_label=iris.feature_names[0]\n",
    "sepal_width_label=iris.feature_names[1]\n",
    "petal_length_label=iris.feature_names[2]\n",
    "petal_width_label=iris.feature_names[3]\n",
    "\n",
    "plt.scatter(sepal_length, sepal_width, c=iris.target)\n",
    "plt.xlabel(sepal_length_label)\n",
    "plt.ylabel(sepal_width_label)\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

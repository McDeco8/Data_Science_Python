#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Example 1: Normal Distribution
mean = 0
std_dev = 1

# Generate random samples from a normal distribution
samples = np.random.normal(mean, std_dev, 1000)

# Plot the histogram of the samples
plt.hist(samples, bins=30, density=True, alpha=0.5, color='g')

# Plot the probability density function (PDF)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)
plt.plot(x, p, 'k', linewidth=2)

plt.title('Normal Distribution')
plt.show()


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Example 2: Poisson Distribution
lambda_param = 3

# Generate random samples from a Poisson distribution
samples = np.random.poisson(lambda_param, 1000)

# Plot the histogram of the samples
plt.hist(samples, bins=20, density=True, alpha=0.5, color='b')

# Plot the probability mass function (PMF)
x = np.arange(0, 20)
p = poisson.pmf(x, lambda_param)
plt.vlines(x, 0, p, colors='k', linestyles='-', lw=2)

plt.title('Poisson Distribution')
plt.show()


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Example 3: Exponential Distribution
lambda_param = 0.5

# Generate random samples from an exponential distribution
samples = np.random.exponential(1/lambda_param, 1000)

# Plot the histogram of the samples
plt.hist(samples, bins=30, density=True, alpha=0.5, color='r')

# Plot the probability density function (PDF)
x = np.linspace(0, 10, 100)
p = expon.pdf(x, scale=1/lambda_param)
plt.plot(x, p, 'k', linewidth=2)

plt.title('Exponential Distribution')
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Example 4: Binomial Distribution
n = 10
p = 0.5

# Generate random samples from a binomial distribution
samples = np.random.binomial(n, p, 1000)

# Plot the histogram of the samples
plt.hist(samples, bins=np.arange(0, n+2)-0.5, density=True, alpha=0.5, color='m')

# Plot the probability mass function (PMF)
x = np.arange(0, n+1)
p = binom.pmf(x, n, p)
plt.vlines(x, 0, p, colors='k', linestyles='-', lw=2)

plt.title('Binomial Distribution')
plt.show()


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Example 5: Chi-Square Distribution
df = 3

# Generate random samples from a chi-square distribution
samples = np.random.chisquare(df, 1000)

# Plot the histogram of the samples
plt.hist(samples, bins=30, density=True, alpha=0.5, color='c')

# Plot the probability density function (PDF)
x = np.linspace(0, 20, 100)
p = chi2.pdf(x, df)
plt.plot(x, p, 'k', linewidth=2)

plt.title('Chi-Square Distribution')
plt.show()


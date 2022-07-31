import math
def Z_cal(p0,p,n,q0,k):
    Z_tab = 1.96
    numenator = float(p-p0)
    denom = float((p0*q0)/n)
    denom1 = float(math.sqrt(denom))
    final = float(numenator/denom1)
    absolute = abs(final)
    if final < 0:
        if Z_tab > absolute:
            print(Z_tab, '>', absolute, '  (True)', '   (Two Tailed test)')
            print("Hypothesis is True")
            confidence_interval(p,n)
    if final < 0:
        if Z_tab < absolute:
            print(Z_tab, '<', absolute, '  (False)', '   (Two Tailed test)')
            print("Hypothesis is False")
            print('Alternative Hypothesis is True which less than', k)
    if final > 0:
        if Z_tab > absolute:
            print(Z_tab, '>', absolute, '  (True)', '   (One Tailed test)')
            print("Hypothesis is True")
            confidence_interval(p, n)
    if final > 0:
        if Z_tab < absolute:
            print(Z_tab, '<', absolute, '  (False)', '   (One Tailed test)')
            print("Hypothesis is False")
            print('Alternative Hypothesis is True which greater than', k)
def hypothesis(h0):
    print('Hypothesis')
    h = int(h0)
    print('H0 =', h)
    print('H1 <', h)
def confidence_interval(p,n):
    q = 1-p
    lo = math.sqrt((p*q)/n)
    lower = p-1.96*lo
    upper = p+1.96*lo
    print('Confidence interval')
    print(lower, '<', 'p', '<', upper)

h0_initial = float(input('how much you claim the population percentage (fertilizer consumption since 2010?) ) '))
hypothesis(h0_initial)
h0_initial_1 = h0_initial/100

population_size = float(input('what is your population size? '))
p0=h0_initial_1

local = float(input('how many people (belongs to farming) says, useage of fertilizers has been decreased? '))
success_rate = float(local/population_size)
q0 = float(1-p0)
alpha = 0.05      #because level of significance is 95% so alpha will be 5%
Z_cal(p0, success_rate, population_size, q0, h0_initial)

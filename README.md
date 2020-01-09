# Yahoo-Most-Active-App
Repeatedly get the most active stocks on yahoo finance and have data sent to your email (every 5-10 minutes)
Great way to get automated updates on the market with detailed data to make quick, easy and profitable trades!


# Scrape and organize Yahoo Finance Most Active stocks into dataframes and csv files:

                                    Name   Price Dollar Change Percentage Change  Volume Market Cap
0                            NIO Limited  3.3900       +0.1500             +4.63  63.048     3.562B
1                    Avon Products, Inc.    5.60         -0.05             -0.88  62.815     2.481B
2           Advanced Micro Devices, Inc.   47.83         -0.42             -0.87  52.962     56.64B
3                     Ford Motor Company    9.25          0.00              0.00  45.686    37.716B
4                Uber Technologies, Inc.   33.93         +1.12             +3.41  43.706    56.797B
5               General Electric Company   11.94         -0.11             -0.91    46.9   104.279B
6            Bank of America Corporation   34.97         +0.35             +1.01  41.746   321.689B
7                           Macy's, Inc.   18.10         +0.43             +2.43  35.225     5.403B
8                              AT&T Inc.   39.37         +0.12             +0.31    37.9   285.832B
9               Rolls-Royce Holdings plc  0.0099       -0.0027            -21.43  32.929   215.827B
10                     Nokia Corporation  4.0200       +0.0700             +1.77  31.982    22.217B
11                           Tesla, Inc.  492.14        +23.08             +4.92  30.558    84.525B
12               Micron Technology, Inc.   57.52         -0.75             -1.29  25.987    63.897B
13                       Transocean Ltd.    6.42         -0.47             -6.82  24.449     3.797B
14                 SmileDirectClub, Inc.   10.60         +0.46             +4.54   23.49     4.052B
15                 Microsoft Corporation  160.09         +2.51             +1.59  26.596     1.237T
16                    Luckin Coffee Inc.   39.46         +4.35            +12.39  21.981     9.483B
17  Petroleo Brasileiro S.A. - Petrobras   15.70         -0.36             -2.24  22.393     99.56B
18                      Yamana Gold Inc.  3.7100       -0.2200             -5.60  22.467      3.58B
19                   Cisco Systems, Inc.   47.52         +0.03             +0.06  21.756   204.936B
20            Itau Unibanco Holding S.A.    8.75         -0.13             -1.46  23.644    79.946B
21                    Encana Corporation  4.5000       -0.3800             -7.79  21.014      5.78B
22                     Intel Corporation   58.97         +0.04             +0.07  19.449   259.678B
23                Amarin Corporation plc   19.46         -0.62             -3.09  18.994     7.083B
24                     Beyond Meat, Inc.   81.48         -2.41             -2.87  18.171     5.083B



# Be able to compare multiple dataframes/csv files to review differences in Price, Volume and other key trading metrics:


                                         Price  Dollar Change  Percentage Change  Volume  ... Price Diff  Dollar Change Diff  Percentage Change Diff  Volume Diff
Name                                                                                      ...                                                                    
Uber Technologies, Inc.                33.9300         1.1200               3.41  43.706  ...     2.5600              0.7400                    2.18       25.123
AT&T Inc.                              39.3700         0.1200               0.31  37.900  ...     0.3100             -0.0800                   -0.20       13.532
Tesla, Inc.                           492.1400        23.0800               4.92  30.558  ...    49.1300             10.3300                    1.96       13.189
Rolls-Royce Holdings plc                0.0099        -0.0027             -21.43  32.929  ...    -0.0001             -0.0081                 -138.82       12.299
Nokia Corporation                       4.0200         0.0700               1.77  31.982  ...     0.2100              0.1300                    3.32        7.014
Microsoft Corporation                 160.0900         2.5100               1.59  26.596  ...     1.4700              4.5100                    2.84        6.822
Petroleo Brasileiro S.A. - Petrobras   15.7000        -0.3600              -2.24  22.393  ...    -0.2900             -0.0800                   -0.52        4.858
Transocean Ltd.                         6.4200        -0.4700              -6.82  24.449  ...    -0.6200             -0.5800                   -8.41        2.173
Ford Motor Company                      9.2500         0.0000               0.00  45.686  ...     0.0400              0.2100                    2.23        1.287
Encana Corporation                      4.5000        -0.3800              -7.79  21.014  ...    -0.3000             -0.4400                   -9.06       -1.465
Bank of America Corporation            34.9700         0.3500               1.01  41.746  ...     0.0700              1.0900                    3.09       -6.874
Advanced Micro Devices, Inc.           47.8300        -0.4200              -0.87  52.962  ...    -0.7700              0.0800                    0.15      -18.177
NIO Limited                             3.3900         0.1500               4.63  63.048  ...    -0.4400              0.0400                    1.67      -19.585
General Electric Company               11.9400        -0.1100              -0.91  46.900  ...    -0.0300             -0.1500                   -1.25      -37.242
Avon Products, Inc.                     5.6000        -0.0500              -0.88  62.815  ...     0.0000              0.0000                    0.00      -90.822


# Have csv files emailed to yourself or any recipient every 5-10 minutes (it is completely up to you on how often you want to review the data!)


# Quick Note:
I will be adding more to this project in terms of plotting price/volume data and also having that data emailed repeatedly along with csv files to visualize market trends



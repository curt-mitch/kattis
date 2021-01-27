Research often involves dealing with large quantities of data, and those data are often too massive to examine manually. Statistical descriptions of data can help humans understand their basic properties. Consider a sample of 𝑛 numbers 𝑋=(𝑥1,𝑥2,…,𝑥𝑛). Of many statistics that can be computed on 𝑋, some of the most important are the following:

min(𝑋): the smallest value in 𝑋

max(𝑋): the largest value in 𝑋

range(𝑋): max(𝑋)−min(𝑋)

Write a program that will analyze samples of data and report these values for each sample.

Input
The input contains between 1 and 10 test cases. Each test case is described by one line of input, which begins with an integer 1≤𝑛≤30 and is followed by 𝑛 integers which make up the sample to be analyzed. Each value in the sample will be in the range −1000000 to 1000000. Input ends at the end of file.

Output
For each case, display Case X:, where X is the case number, followed by the min, max, and range of the sample (in that order). Follow the format of the sample output.
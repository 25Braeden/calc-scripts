import math

def calculate_z_score(x1, n1, x2, n2):
 p1 = x1 / n1
 p2 = x2 / n2
 p = (x1 + x2) / (n1 + n2)
 q = 1 - p
 z = (p1 - p2) / math.sqrt(p * q * (1/n1 + 1/n2))
 return z

def normal_cdf(x):
 # Coefficients for a simple polynomial approximation (Abramowitz and Stegun, formula 26.2.17)
 # The absolute error of this approximation is less than 7.5e-8 for all x
 t = 1 / (1 + 0.2316419 * abs(x))
 t2 = t * t
 t3 = t2 * t
 t4 = t3 * t
 t5 = t4 * t
 poly = 1.0 - 1.0 / (math.sqrt(2*math.pi)) * math.exp(-x*x / 2) * (0.319381530 * t - 0.356563782 * t2 + 1.781477937 * t3 - 1.821255978 * t4 + 1.330274429 * t5)
 if x >= 0:
     return 1 - poly
 else:
     return poly

def calculate_p_value(z, test_type):
 if test_type == 'left':
     p_value = normal_cdf(z)
 elif test_type == 'right':
     p_value = 1 - normal_cdf(z)
 elif test_type == 'two':
     p_value = 2 * (1 - normal_cdf(abs(z)))
 return p_value

def main():
 x1 = int(input("Enter the number of successes for the first group: "))
 n1 = int(input("Enter the sample size for the first group: "))
 x2 = int(input("Enter the number of successes for the second group: "))
 n2 = int(input("Enter the sample size for the second group: "))
 test_type = input("Enter the test type (left, right, two): ")

 z_score = calculate_z_score(x1, n1, x2, n2)
 p_value = calculate_p_value(z_score, test_type)

 print("Z-score: " + str(z_score))
 print("P-value: " + str(p_value))

if __name__ == "__main__":
 main()

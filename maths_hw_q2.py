import datetime
import numpy as np

# Generate 50 random numbers from a normal distribution with mean μ = 10 and standard deviation σ = 0.5
mean_normal = 10
std_dev_normal = 0.5
normal_numbers = np.random.normal(mean_normal, std_dev_normal, 50)

# Generate 50 random numbers within the range [-20, +20] from a uniform distribution
low_uniform = -20
high_uniform = 20
uniform_numbers = np.random.uniform(low_uniform, high_uniform, 50)


def verify_Chebyshev_ineq(lst, k):
    # Count the number of elements within the range [μ - kσ, μ + kσ]
    count_within_range = sum((mean_normal - k * std_dev_normal <= lst) & (lst <= mean_normal + k * std_dev_normal))

    # Calculate the probability P(|X - μ| < kσ) and 1 - 1/k^2
    probability = count_within_range / len(lst)
    chebyshev_inequality = 1 - 1 / (k ** 2)

    # Determine if the inequality is satisfied
    inequality_satisfied = probability >= chebyshev_inequality

    print(f"Probability of |X - μ| = {probability:.2f} ; 1 - 1/(k^2) = {chebyshev_inequality}")
    print(f"When k = {k} , P(|X - μ| < kσ) >= 1 - 1/k^2 is {inequality_satisfied}")


# Testcases for normal distribution
k_values_normal = [1, np.sqrt(2), 1.5, 2, 3]

for k in k_values_normal:
    print("k =", k)
    print("For normal distribution:")
    verify_Chebyshev_ineq(normal_numbers, k)
    print("=" * 50)  # Separate each set of results

# Testcases for uniform distribution
k_values_uniform = [1, 1.5, 2, 2.5, 3]

for k in k_values_uniform:
    print("k =", k)
    print("For uniform distribution:")
    verify_Chebyshev_ineq(uniform_numbers, k)
    print("=" * 50)  # Separate each set of results

current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Current date and time: {current_datetime}")
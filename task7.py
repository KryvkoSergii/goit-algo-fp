import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_trials):
    outcomes = {}
    for _ in range(num_trials):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        outcomes[total] = outcomes.get(total, 0) + 1

    probabilities = {key: value / num_trials for key, value in outcomes.items()}
    return probabilities

def theoretical_probabilities():
    theoretical_probs = {}
    for i in range(2, 13):
        favorable_outcomes = 0
        for j in range(1, 7):
            if 1 <= i - j <= 6:
                favorable_outcomes += 1
        theoretical_probs[i] = favorable_outcomes / 36
    return theoretical_probs

def plot_results(monte_carlo_probs, theoretical_probs):
    x = list(range(2, 13))
    monte_carlo_y = [monte_carlo_probs.get(i, 0) for i in x]
    theoretical_y = [theoretical_probs[i] for i in x]

    plt.bar(x, monte_carlo_y, alpha=0.5, label='Monte Carlo Симуляція')
    plt.plot(x, theoretical_y, marker='o', linestyle='-', color='r', label='Теоретична вірогідність')
    plt.xlabel('Сума кубиків')
    plt.ylabel('Вірогідність')
    plt.title('Порівняння симуляції Monte Carlo Simulation та теоретична вірогідність')
    plt.legend()
    plt.show()

# Кількість спроб для Монте-Карло симуляції
num_trials = 100000

# Виконати симуляцію
monte_carlo_probs = monte_carlo_simulation(num_trials)

# Отримати теоретичні ймовірності
theoretical_probs = theoretical_probabilities()

# Порівняти результати
plot_results(monte_carlo_probs, theoretical_probs)


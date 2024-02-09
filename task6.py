def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info["cost"] <= budget:
            selected_items.append(item_name)
            total_cost += item_info["cost"]
            total_calories += item_info["calories"]

    return {"selected_items": selected_items, "total_cost": total_cost, "total_calories": total_calories}

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            item_cost = items[i - 1]["cost"]
            item_calories = items[i - 1]["calories"]

            if item_cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_cost] + item_calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1]["name"])
            j -= items[i - 1]["cost"]
        i -= 1

    return {"selected_items": selected_items[::-1], "total_cost": dp[n][budget], "total_calories": dp[n][budget]}

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300, "name": "pizza"},
    "hamburger": {"cost": 40, "calories": 250, "name": "hamburger"},
    "hot-dog": {"cost": 30, "calories": 200, "name": "hot-dog"},
    "pepsi": {"cost": 10, "calories": 100, "name": "pepsi"},
    "cola": {"cost": 15, "calories": 220, "name": "cola"},
    "potato": {"cost": 25, "calories": 350, "name": "potato"}
}

# Бюджет
budget = 60

# Жадібний алгоритм
result_greedy = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", result_greedy["selected_items"])
print("Total cost:", result_greedy["total_cost"])
print("Total calories:", result_greedy["total_calories"])
print()

# Алгоритм динамічного програмування
result_dp = dynamic_programming([x for x in items.values()], budget)
print("Dynamic Programming Algorithm:")
print("Selected items:", result_dp["selected_items"])
print("Total cost:", result_dp["total_cost"])
print("Total calories:", result_dp["total_calories"])

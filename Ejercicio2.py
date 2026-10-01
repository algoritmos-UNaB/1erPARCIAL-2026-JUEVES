def total_donas_iterativo(a, b):
    total = 0
    for _ in range(b):
        total += a
    return total

if __name__ == "__main__":
    print("Total donas (3 por persona, 5 personas):", total_donas_iterativo(3, 5)) # Devuelve 15
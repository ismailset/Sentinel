def analyze_log(file):
    errors = 0
    with open(file) as f:
        for line in f:
            if "error" in line.lower():
                errors += 1
    print(f"Errors found: {errors}")

import csv

print("Searching...")
try:
    with open('notebooks/data/train.csv', 'r') as f:
        reader = csv.DictReader(f)
        matches = []
        for row in reader:
            try:
                carat = float(row['carat'])
                if 0.99 <= carat <= 1.01 and row['cut'] == 'Ideal' and row['color'] == 'G' and row['clarity'] == 'VS1':
                    matches.append(row)
            except ValueError:
                continue

        if matches:
            # Calculate averages
            avg_depth = sum(float(r['depth']) for r in matches) / len(matches)
            avg_table = sum(float(r['table']) for r in matches) / len(matches)
            avg_x = sum(float(r['x']) for r in matches) / len(matches)
            avg_y = sum(float(r['y']) for r in matches) / len(matches)
            avg_z = sum(float(r['z']) for r in matches) / len(matches)
            
            result = f"depth: {avg_depth:.2f}\ntable: {avg_table:.2f}\nx: {avg_x:.2f}\ny: {avg_y:.2f}\nz: {avg_z:.2f}"
            print(result)
            with open('fast_dim.txt', 'w') as out:
                out.write(result)
        else:
            print("No matches")
            with open('fast_dim.txt', 'w') as out:
                out.write("No matches")

except Exception as e:
    print(f"Error: {e}")

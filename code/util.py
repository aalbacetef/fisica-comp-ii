import csv

def write_csv(hdr: list[str], rows: list, name: str):
    data = [hdr] + rows
    with open(name, mode="w", newline="") as f:
        w = csv.writer(f)
        for row in data:
            w.writerow(row)

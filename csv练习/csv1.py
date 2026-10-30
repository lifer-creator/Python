import csv

DATA = "blorp_q7.csv"
OUT = "blorp_q7_summary.csv"

def load(path):
    """读 CSV，返回 (表头 list, 数据行 list[list[str]])"""
    with open(path, encoding="utf-8-sig", newline="") as f:   # TODO 1 填编码串
        reader = csv.DictReader(f)                            # TODO 2
        header = reader.fieldnames                                  # TODO 3 取走表头
        rows = [r for r in reader if r]               # 空行跳过（送你）
    return header, rows

def summarize(header, rows):
    """返回 [(列名, 平均值, 最大值), ...]"""
    stats = []
    for i in range(1, len(header)):                   # 第 0 列是名字，跳过
        col = [float(r[header[i]]) for r in rows]                      # TODO 4 转成数字
        if not col:                                   # 空列保护（送你）
            continue
        stats.append((header[i], sum(col)/len(col), max(col)))             # TODO 5 平均、最大
    return stats

def save(path, stats):
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)                                   # TODO 6
        writer.writerow(["列名", "平均值", "最大值"])
        for name, avg, mx in stats:
            writer.writerow([name, f"{avg:.2f}", mx]) # 格式化（送你）
    print("已写入", path)

def main():
    header, rows = load(DATA)
    stats = summarize(header, rows)
    for name, avg, mx in stats:
        print(f"{name}: 平均 {avg:.2f}  最大 {mx}")
    save(OUT, stats)

if __name__ == "__main__":
    main()
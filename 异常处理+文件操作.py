from pathlib import Path
path=Path("text.txt")
def lioad_lines(path):
    try:
        a=[]
        for line in path.read_text(encoding="utf-8").splitlines():
            a.append(line)
        return a
    except FileNotFoundError :
        print("文件不存在")
        return []
    except UnicodeDecodeError:
        print("没按照utf-8编码")
    finally:
        print("load_lines 结束")
print(lioad_lines(path))


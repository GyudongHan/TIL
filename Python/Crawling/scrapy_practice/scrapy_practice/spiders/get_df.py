import pandas as pd

# json 파일 불러오기
def main():
    data = pd.read_json("popluation.json")
    data = pd.DataFrame(data)

    print(data.head())

if __name__ == "__main__":
    main()
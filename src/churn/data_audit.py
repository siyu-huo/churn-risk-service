from pathlib import Path

import pandas as pd


DATA_PATH = Path("D:/projects\churn-risk-service/data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"找不到数据文件：{DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    print("数据形状：", df.shape)
    print("\n列名：")
    print(df.columns.tolist())

    print("\n数据类型：")
    print(df.dtypes)

    print("\n缺失值：")
    print(df.isna().sum())

    print("\n重复行：", df.duplicated().sum())

    print("\n目标变量分布：")
    print(df["Churn"].value_counts(dropna=False))

    print("\n目标变量比例：")
    print(df["Churn"].value_counts(normalize=True, dropna=False))

    print("\n数值特征：")
    print(df.select_dtypes(include="number").columns.tolist())

    print("\n类别特征：")
    print(df.select_dtypes(exclude="number").columns.tolist())


if __name__ == "__main__":
    main()
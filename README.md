# Churn Risk Service

基于公开客户数据的客户流失预测服务。

## 项目目标

根据客户基本信息、合同信息和服务使用情况，预测客户是否会流失。

## 当前进度

- [x] 初始化项目结构
- [ ] 数据审查
- [ ] 逻辑回归 baseline
- [ ] 树模型对比
- [ ] 模型解释
- [ ] FastAPI 接口
- [ ] Streamlit 页面
- [ ] Docker 部署

## 技术栈

- Python
- Pandas
- Scikit-learn
- FastAPI
- Streamlit

## Prediction Target

- `Churn = Yes`：客户流失
- `Churn = No`：客户未流失

## Evaluation Metrics

主要指标：

- ROC-AUC
- Recall
- F1-score
- Brier Score

由于流失和未流失客户可能数量不平衡，因此不能只使用 Accuracy。

## Data Audit

数据审查脚本位于 `src/churn/data_audit.py`。

审查内容包括：

- 数据规模
- 字段类型
- 缺失值
- 重复样本
- `Churn` 类别分布
- 数值特征和类别特征

`customerID` 是客户标识符，不作为模型特征。

`Churn` 是预测目标。`TotalCharges` 需要转换为数值类型，无法转换的空字符串将作为缺失值处理。

训练集、验证集和测试集必须在预处理前划分，避免数据泄漏。

审查结果：数据形状： (7043, 21)

列名：
['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn']

数据类型：
customerID              str
gender                  str
SeniorCitizen         int64
Partner                 str
Dependents              str
tenure                int64
PhoneService            str
MultipleLines           str
InternetService         str
OnlineSecurity          str
OnlineBackup            str
DeviceProtection        str
TechSupport             str
StreamingTV             str
StreamingMovies         str
Contract                str
PaperlessBilling        str
PaymentMethod           str
MonthlyCharges      float64
TotalCharges            str
Churn                   str
dtype: object

缺失值：
customerID          0
gender              0
SeniorCitizen       0
Partner             0
Dependents          0
tenure              0
PhoneService        0
MultipleLines       0
InternetService     0
OnlineSecurity      0
OnlineBackup        0
DeviceProtection    0
TechSupport         0
StreamingTV         0
StreamingMovies     0
Contract            0
PaperlessBilling    0
PaymentMethod       0
MonthlyCharges      0
TotalCharges        0
Churn               0
dtype: int64

重复行： 0

目标变量分布：
Churn
No     5174
Yes    1869
Name: count, dtype: int64

目标变量比例：
Churn
No     0.73463
Yes    0.26537
Name: proportion, dtype: float64

数值特征：
['SeniorCitizen', 'tenure', 'MonthlyCharges']

类别特征：
['customerID', 'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'TotalCharges', 'Churn']
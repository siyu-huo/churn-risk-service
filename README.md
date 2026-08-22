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
import csv
import os

# 文件路径
input_file = "/home/zw/Downloads/题目数据.csv"
output_dir = "/home/zw/Downloads"
output_file = os.path.join(output_dir, "处理后的题目数据.csv")

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 读取原始数据
with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    rows = list(reader)

# 第一行是表头
header = rows[0]
# 数据行
data_rows = rows[1:]

# 模型列索引（假设列名为'模型1','模型2','模型3','模型4'，按顺序对应索引1~4）
model_cols = [1, 2, 3, 4]  # 因为第0列是题号（或uuid列）

# 处理每一行
processed_rows = [header + ['平均值']]  # 新表头，增加平均值列

for row in data_rows:
    # 如果行数不足，跳过（但一般不会）
    if len(row) <= max(model_cols):
        # 补齐列数，以防缺失
        row += [''] * (max(model_cols) + 1 - len(row))
    
    # 1. 缺失数据填0：对于数值列，如果为空字符串或空，则设为0
    numeric_values = []
    for col_idx in model_cols:
        val = row[col_idx].strip() if col_idx < len(row) else ''
        if val == '':
            numeric_values.append(0.0)
        else:
            try:
                num = float(val)
            except ValueError:
                num = 0.0  # 非数字视为错误，置0
            # 2. 保证范围0~1，否则置0
            if num < 0 or num > 1:
                num = 0.0
            numeric_values.append(num)
            # 更新回row中（如果需要保留清洗后的值，可以写回）
            row[col_idx] = str(num)
    
    # 3. 计算平均值
    avg = sum(numeric_values) / len(numeric_values)
    row.append(str(avg))  # 添加平均值列
    
    processed_rows.append(row)

# 写入新文件
with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(processed_rows)

print(f"处理完成，结果已保存至：{output_file}")
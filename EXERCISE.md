# 🐍 Python 垃圾分类程序 - 练习指南

## ✅ 程序已完成

### 功能演示

```bash
# 1. 查询单个垃圾
$env:PYTHONIOENCODING="utf-8"; python classifier.py -q 苹果
# 输出：[W] 苹果 -> 湿垃圾

# 2. 批量查询
$env:PYTHONIOENCODING="utf-8"; python classifier.py -b 苹果 电池 塑料瓶 餐巾纸
# 输出：按分类分组显示

# 3. 查看统计
$env:PYTHONIOENCODING="utf-8"; python classifier.py -s
# 输出：180 项数据，四类分布

# 4. 交互模式
$env:PYTHONIOENCODING="utf-8"; python classifier.py
# 进入交互式查询
```

---

## 📚 练习任务

### Level 1: 理解代码结构

**任务 1.1**: 阅读 `database.py`
- 找到 `GARBAGE_DATABASE` 字典
- 数一数每个分类有多少项
- 理解数据结构

**问题：**
1. 可回收物有多少项？
2. 湿垃圾有哪些示例？
3. 如果想添加"旧手机"，应该放在哪个分类？

**任务 1.2**: 阅读 `classifier.py`
- 找到 `search_garbage_detailed()` 函数
- 理解精确匹配和模糊匹配的逻辑
- 看看返回值是什么格式

---

### Level 2: 修改数据库

**任务 2.1**: 添加新垃圾
在 `database.py` 的 `GARBAGE_DATABASE` 中添加：
```python
"旧手机": GarbageType.RECYCLABLE,
"旧电脑": GarbageType.RECYCLABLE,
"猫粮": GarbageType.WET,
"狗粮": GarbageType.WET,
```

**验证：**
```bash
$env:PYTHONIOENCODING="utf-8"; python classifier.py -q 旧手机
$env:PYTHONIOENCODING="utf-8"; python classifier.py -b 猫粮 狗粮
```

**任务 2.2**: 修改分类说明
在 `CATEGORY_INFO` 中，修改湿垃圾的提示：
```python
"tip": "沥干水分，去除包装，尽快投放",
```

---

### Level 3: 理解函数

**任务 3.1**: 模糊匹配算法
找到这段代码：
```python
for garbage_name, category in GARBAGE_DATABASE.items():
    if name in garbage_name or garbage_name in name:
        matches.append(...)
```

**问题：**
1. `name in garbage_name` 是什么意思？举例说明
2. `garbage_name in name` 是什么意思？举例说明
3. 如果输入"苹果"，会匹配到哪些垃圾？

**任务 3.2**: 批量查询函数
阅读 `batch_search()` 函数：
1. 它如何统计每个分类的数量？
2. 如何遍历用户输入的垃圾列表？
3. 输出格式是怎样的？

---

### Level 4: 添加功能

**任务 4.1**: 添加随机测试功能
在 `classifier.py` 中添加：
```python
import random

def random_quiz():
    """随机测试功能"""
    garbage_list = list(GARBAGE_DATABASE.keys())
    correct = 0
    total = 5
    
    print("\n=== 垃圾分类小测试 ===\n")
    
    for i in range(total):
        garbage = random.choice(garbage_list)
        answer = input(f"{i+1}. {garbage} 属于什么垃圾？")
        # TODO: 判断答案是否正确
    
    print(f"\n得分：{correct}/{total}")
```

**任务 4.2**: 添加导出功能
添加一个函数，将查询结果导出到文件：
```python
def export_to_file(results, filename="result.txt"):
    """导出查询结果到文件"""
    with open(filename, "w", encoding="utf-8") as f:
        for result in results:
            f.write(f"{result}\n")
    print(f"结果已保存到 {filename}")
```

**任务 4.3**: 添加搜索历史
实现一个功能，记录用户查询过的垃圾：
```python
search_history = []

def add_to_history(name, result):
    """添加查询到历史记录"""
    search_history.append({
        "name": name,
        "found": result["found"],
    })

def show_history():
    """显示搜索历史"""
    print("\n搜索历史：")
    for item in search_history[-10:]:  # 显示最近 10 条
        print(f"  - {item['name']}: {'找到' if item['found'] else '未找到'}")
```

---

### Level 5: 挑战任务

**任务 5.1**: 添加图片识别（扩展）
思路：
1. 使用百度 AI 或腾讯 AI 的图片识别 API
2. 上传图片，识别物体
3. 根据识别结果查询垃圾分类

**任务 5.2**: 添加 GUI 界面
使用 `tkinter` 创建图形界面：
```python
import tkinter as tk
from tkinter import ttk

def create_gui():
    root = tk.Tk()
    root.title("垃圾分类查询")
    
    # 输入框
    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)
    
    # 查询按钮
    btn = tk.Button(root, text="查询", command=lambda: search(entry.get()))
    btn.pack()
    
    # 结果显示
    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=20)
    
    root.mainloop()
```

**任务 5.3**: 添加 Web 界面
使用 `Flask` 创建简单的 Web 应用：
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search')
def search():
    name = request.args.get('name')
    result = search_garbage_detailed(name)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 📖 知识点总结

### Python 基础
- ✅ 字典操作：`dict[key]`, `dict.get()`, `dict.items()`
- ✅ 列表操作：`list.append()`, `list[:10]` 切片
- ✅ 字符串操作：`string.lower()`, `string.strip()`, `f-string`
- ✅ 函数定义：`def func_name(param):`
- ✅ 条件判断：`if-elif-else`
- ✅ 循环：`for`, `while`

### Python 进阶
- ✅ 模块导入：`from module import function`
- ✅ 命令行参数：`argparse`
- ✅ 异常处理：`try-except`
- ✅ 文件操作：`open()`, `with` 语句

### 算法思维
- ✅ 精确匹配 vs 模糊匹配
- ✅ 批量处理
- ✅ 数据分组统计
- ✅ 交互式程序设计

---

## 💡 下一步建议

1. **完成 Level 2** - 先熟悉修改数据库
2. **尝试 Level 3** - 理解代码逻辑
3. **挑战 Level 4** - 添加自己的功能
4. **探索 Level 5** - 扩展成完整应用

---

## ❓ 遇到问题？

常见问题：
- "添加数据后不生效" → 检查是否重新运行了程序
- "中文显示乱码" → 设置 `$env:PYTHONIOENCODING="utf-8"`
- "找不到模块" → 确保在正确的目录下运行

随时问我！

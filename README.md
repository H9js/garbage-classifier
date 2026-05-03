# 🗑️ 垃圾分类识别程序

一个实用的命令行垃圾分类查询工具，支持模糊搜索、批量查询和交互模式。基于 Python 开发，无需额外依赖。

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Database](https://img.shields.io/badge/Items-180+-orange.svg)](database.py)

## ✨ 功能特点

- 🔍 **精确查询** - 输入垃圾名称，立即返回分类
- 🎯 **模糊搜索** - 找不到准确匹配时，推荐相似项
- 📦 **批量查询** - 一次查询多个垃圾，自动分组统计
- 💬 **交互模式** - 友好的命令行交互界面
- 📊 **数据统计** - 查看数据库分类统计
- 🚀 **零依赖** - 仅需 Python 标准库

## 🚀 快速开始

### 环境要求
- Python 3.8+
- Windows / macOS / Linux

### 安装使用

```bash
# 1. 克隆项目
git clone https://github.com/H9js/garbage-classifier.git
cd garbage-classifier

# 2. 直接运行（无需安装依赖）
python classifier.py

# 3. 查询单个垃圾
python classifier.py -q 苹果

# 4. 批量查询
python classifier.py -b 苹果 电池 塑料瓶 餐巾纸

# 5. 查看统计
python classifier.py -s
```

## 📖 使用示例

### 查询单个垃圾

```bash
$ python classifier.py -q 苹果
[W] 苹果 -> 湿垃圾
分类说明：易腐烂的生物质生活垃圾
提示：沥干水分，去除包装
```

### 批量查询

```bash
$ python classifier.py -b 苹果 电池 塑料瓶 餐巾纸

==================================================
垃圾分类批量查询结果
==================================================

[R] 可回收物:
  - 塑料瓶

[H] 有害垃圾:
  - 电池

[W] 湿垃圾:
  - 苹果

[D] 干垃圾:
  - 餐巾纸

--------------------------------------------------
统计：共查询 4 项，已知 4 项，未知 0 项
==================================================
```

### 交互模式

```bash
$ python classifier.py

==================================================
欢迎使用垃圾分类查询系统
==================================================

请输入垃圾名称：电池
[H] 电池 -> 有害垃圾
```

更多使用示例请查看 [EXAMPLES.md](EXAMPLES.md)

## 🗑️ 垃圾分类标准

本项目采用**上海标准**（2019 年版），分为四类：

| 分类 | 标识 | 颜色 | 说明 | 示例 |
|------|------|------|------|------|
| **可回收物** | R | 🔵 蓝色 | 适宜回收利用的生活垃圾 | 废纸张、废塑料、废玻璃、废金属 |
| **有害垃圾** | H | 🔴 红色 | 对人体健康或自然环境有害 | 废电池、废灯管、废药品、废油漆 |
| **湿垃圾** | W | 🟤 棕色 | 易腐烂的生物质生活垃圾 | 食材废料、剩菜剩饭、果皮果核 |
| **干垃圾** | D | ⚫ 黑色 | 除以上三类外的其他生活垃圾 | 餐巾纸、卫生间用纸、塑料袋、烟蒂 |

> 💡 **提示**：其他城市名称可能不同（如北京/深圳称"厨余垃圾"），但分类逻辑基本一致。

## 📊 数据库统计

| 分类 | 数量 | 占比 |
|------|------|------|
| 可回收物 | 24 项 | 13% |
| 有害垃圾 | 21 项 | 12% |
| 湿垃圾 | 57 项 | 32% |
| 干垃圾 | 78 项 | 43% |
| **总计** | **180+ 项** | **100%** |

查看完整数据：[database.py](database.py)

## 📁 项目结构

```
garbage-classifier/
├── classifier.py          # 主程序（查询逻辑）
├── database.py            # 垃圾分类数据库（180+ 项数据）
├── README.md              # 项目说明
├── EXAMPLES.md            # 使用示例
├── EXERCISE.md            # Python 练习指南（学习者必看）
├── requirements.txt       # Python 依赖（本项目无需额外依赖）
├── LICENSE                # MIT 许可证
└── .gitignore             # Git 忽略文件
```

## 🛠️ 扩展开发

这个项目可以作为 Python 学习的起点，尝试添加以下功能：

### 初学者练习
- [ ] 添加更多垃圾分类数据
- [ ] 修改提示语和输出格式
- [ ] 添加查询历史记录功能

### 进阶挑战
- [ ] **GUI 界面** - 使用 tkinter 创建图形界面
- [ ] **Web 版本** - 使用 Flask/FastAPI 提供 Web API
- [ ] **数据导出** - 支持导出查询结果为 Excel/CSV
- [ ] **用户测试** - 添加垃圾分类小测试功能
- [ ] **图片识别** - 接入 AI API 实现拍照识别

查看练习指南：[EXERCISE.md](EXERCISE.md)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

可以贡献：
- ✅ 添加更多垃圾分类数据
- ✅ 修复 Bug
- ✅ 添加新功能
- ✅ 改进文档
- ✅ 适配不同城市标准

### 如何贡献

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📚 学习资源

如果你是 Python 初学者，可以参考：

- [Python 官方教程](https://docs.python.org/zh-cn/3/tutorial/)
- [菜鸟教程 - Python](https://www.runoob.com/python3/)
- [B 站 Python 零基础教程](https://search.bilibili.com/all?keyword=python 零基础)

## ❓ 常见问题

### Q: 为什么有些垃圾查不到？

A: 数据库目前包含 180+ 项常见垃圾。如果查不到：
1. 尝试输入更通用的名称
2. 查看模糊搜索推荐的相似项
3. 提交 Issue 建议添加

### Q: 不同城市分类标准不同怎么办？

A: 本项目采用上海标准，其他城市名称可能不同（如"厨余垃圾"），但分类逻辑基本一致。如需适配其他城市，可以修改 `database.py` 中的分类说明。

### Q: 如何在项目中使用？

A: 直接导入函数即可：

```python
from classifier import search_garbage_detailed

result = search_garbage_detailed("苹果")
if result["found"]:
    print(f"{result['name']} 属于 {result['category']}")
```

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 👤 作者

**H9js** - 初学者的第一个 Python 项目

这是一个学习项目，用于展示 Python 编程技能，同时帮助更多人了解垃圾分类。

## 🎯 项目状态

- ✅ **已完成** - 核心功能完整
- 📖 **适合学习** - 代码清晰，有详细注释
- 🚀 **持续更新** - 欢迎贡献

---

**如果这个项目对你有帮助，请给一个 ⭐ Star！**

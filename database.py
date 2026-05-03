# -*- coding: utf-8 -*-
"""
垃圾分类数据库
包含常见垃圾及其分类
"""

# 垃圾分类枚举
class GarbageType:
    RECYCLABLE = "可回收物"      # 🔵 蓝色
    HAZARDOUS = "有害垃圾"        # 🔴 红色
    WET = "湿垃圾"               # 🟤 棕色
    DRY = "干垃圾"               # ⚫ 黑色


# 垃圾分类数据库
# 格式：垃圾名称：分类
GARBAGE_DATABASE = {
    # ========== 可回收物 ==========
    "报纸": GarbageType.RECYCLABLE,
    "书本": GarbageType.RECYCLABLE,
    "纸箱": GarbageType.RECYCLABLE,
    "塑料瓶": GarbageType.RECYCLABLE,
    "玻璃瓶": GarbageType.RECYCLABLE,
    "易拉罐": GarbageType.RECYCLABLE,
    "旧衣服": GarbageType.RECYCLABLE,
    "旧鞋子": GarbageType.RECYCLABLE,
    "金属": GarbageType.RECYCLABLE,
    "铁罐": GarbageType.RECYCLABLE,
    "铝罐": GarbageType.RECYCLABLE,
    "塑料玩具": GarbageType.RECYCLABLE,
    "电线": GarbageType.RECYCLABLE,
    "插座": GarbageType.RECYCLABLE,
    "充电宝": GarbageType.RECYCLABLE,
    "手机": GarbageType.RECYCLABLE,
    "电脑": GarbageType.RECYCLABLE,
    "家电": GarbageType.RECYCLABLE,
    "床单": GarbageType.RECYCLABLE,
    "窗帘": GarbageType.RECYCLABLE,
    "背包": GarbageType.RECYCLABLE,
    "钱包": GarbageType.RECYCLABLE,
    "皮带": GarbageType.RECYCLABLE,
    "毛巾": GarbageType.RECYCLABLE,
    "毛线": GarbageType.RECYCLABLE,
    "雨伞": GarbageType.RECYCLABLE,
    "镜子": GarbageType.RECYCLABLE,
    "梳子": GarbageType.RECYCLABLE,
    
    # ========== 有害垃圾 ==========
    "电池": GarbageType.HAZARDOUS,
    "充电电池": GarbageType.HAZARDOUS,
    "纽扣电池": GarbageType.HAZARDOUS,
    "蓄电池": GarbageType.HAZARDOUS,
    "灯管": GarbageType.HAZARDOUS,
    "节能灯": GarbageType.HAZARDOUS,
    "荧光灯": GarbageType.HAZARDOUS,
    "水银温度计": GarbageType.HAZARDOUS,
    "血压计": GarbageType.HAZARDOUS,
    "药品": GarbageType.HAZARDOUS,
    "药片": GarbageType.HAZARDOUS,
    "药水": GarbageType.HAZARDOUS,
    "油漆": GarbageType.HAZARDOUS,
    "油漆桶": GarbageType.HAZARDOUS,
    "杀虫剂": GarbageType.HAZARDOUS,
    "消毒剂": GarbageType.HAZARDOUS,
    "指甲油": GarbageType.HAZARDOUS,
    "洗甲水": GarbageType.HAZARDOUS,
    "化妆品": GarbageType.HAZARDOUS,
    "墨盒": GarbageType.HAZARDOUS,
    "硒鼓": GarbageType.HAZARDOUS,
    
    # ========== 湿垃圾 ==========
    "苹果": GarbageType.WET,
    "苹果核": GarbageType.WET,
    "香蕉皮": GarbageType.WET,
    "橙子皮": GarbageType.WET,
    "西瓜皮": GarbageType.WET,
    "葡萄": GarbageType.WET,
    "葡萄皮": GarbageType.WET,
    "梨": GarbageType.WET,
    "桃子": GarbageType.WET,
    "芒果": GarbageType.WET,
    "菠萝": GarbageType.WET,
    "草莓": GarbageType.WET,
    "蔬菜": GarbageType.WET,
    "菜叶": GarbageType.WET,
    "萝卜": GarbageType.WET,
    "土豆": GarbageType.WET,
    "鸡蛋": GarbageType.WET,
    "蛋壳": GarbageType.WET,
    "米饭": GarbageType.WET,
    "面条": GarbageType.WET,
    "面包": GarbageType.WET,
    "蛋糕": GarbageType.WET,
    "饼干": GarbageType.WET,
    "肉类": GarbageType.WET,
    "猪肉": GarbageType.WET,
    "牛肉": GarbageType.WET,
    "羊肉": GarbageType.WET,
    "鸡肉": GarbageType.WET,
    "鸭肉": GarbageType.WET,
    "鱼肉": GarbageType.WET,
    "虾": GarbageType.WET,
    "蟹": GarbageType.WET,
    "贝类": GarbageType.WET,
    "茶叶": GarbageType.WET,
    "茶渣": GarbageType.WET,
    "咖啡": GarbageType.WET,
    "咖啡渣": GarbageType.WET,
    "坚果": GarbageType.WET,
    "瓜子": GarbageType.WET,
    "花生": GarbageType.WET,
    "核桃": GarbageType.WET,
    "糖果": GarbageType.WET,
    "巧克力": GarbageType.WET,
    "果冻": GarbageType.WET,
    "薯片": GarbageType.WET,
    "话梅": GarbageType.WET,
    "果皮": GarbageType.WET,
    "果核": GarbageType.WET,
    "剩菜": GarbageType.WET,
    "剩饭": GarbageType.WET,
    "食物残渣": GarbageType.WET,
    "过期食品": GarbageType.WET,
    "宠物食品": GarbageType.WET,
    "花卉": GarbageType.WET,
    "绿植": GarbageType.WET,
    "中药": GarbageType.WET,
    "药渣": GarbageType.WET,
    
    # ========== 干垃圾 ==========
    "餐巾纸": GarbageType.DRY,
    "卫生纸": GarbageType.DRY,
    "纸巾": GarbageType.DRY,
    "湿巾": GarbageType.DRY,
    "尿不湿": GarbageType.DRY,
    "卫生巾": GarbageType.DRY,
    "烟头": GarbageType.DRY,
    "烟灰": GarbageType.DRY,
    "烟盒": GarbageType.DRY,
    "塑料袋": GarbageType.DRY,
    "保鲜膜": GarbageType.DRY,
    "保鲜袋": GarbageType.DRY,
    "一次性餐具": GarbageType.DRY,
    "塑料碗": GarbageType.DRY,
    "塑料杯": GarbageType.DRY,
    "塑料盒": GarbageType.DRY,
    "泡沫": GarbageType.DRY,
    "泡沫塑料": GarbageType.DRY,
    "橡皮泥": GarbageType.DRY,
    "橡皮": GarbageType.DRY,
    "笔": GarbageType.DRY,
    "圆珠笔": GarbageType.DRY,
    "中性笔": GarbageType.DRY,
    "铅笔": GarbageType.DRY,
    "毛笔": GarbageType.DRY,
    "胶带": GarbageType.DRY,
    "透明胶": GarbageType.DRY,
    "创可贴": GarbageType.DRY,
    "棉签": GarbageType.DRY,
    "化妆棉": GarbageType.DRY,
    "面膜": GarbageType.DRY,
    "洗发水": GarbageType.DRY,
    "沐浴露": GarbageType.DRY,
    "牙膏": GarbageType.DRY,
    "牙刷": GarbageType.DRY,
    "漱口杯": GarbageType.DRY,
    "毛巾": GarbageType.DRY,
    "抹布": GarbageType.DRY,
    "拖把": GarbageType.DRY,
    "扫把": GarbageType.DRY,
    "垃圾桶": GarbageType.DRY,
    "花盆": GarbageType.DRY,
    "陶瓷": GarbageType.DRY,
    "碗": GarbageType.DRY,
    "盘子": GarbageType.DRY,
    "杯子": GarbageType.DRY,
    "玻璃杯": GarbageType.DRY,
    "镜子": GarbageType.DRY,
    "梳子": GarbageType.DRY,
    "指甲剪": GarbageType.DRY,
    "剃须刀": GarbageType.DRY,
    "打火机": GarbageType.DRY,
    "火柴": GarbageType.DRY,
    "蜡烛": GarbageType.DRY,
    "香": GarbageType.DRY,
    "钥匙": GarbageType.DRY,
    "锁": GarbageType.DRY,
    "工具": GarbageType.DRY,
    "钉子": GarbageType.DRY,
    "螺丝": GarbageType.DRY,
    "电线": GarbageType.DRY,
    "网线": GarbageType.DRY,
    "光盘": GarbageType.DRY,
    "磁带": GarbageType.DRY,
    "照片": GarbageType.DRY,
    "发票": GarbageType.DRY,
    "收据": GarbageType.DRY,
    "名片": GarbageType.DRY,
    "信封": GarbageType.DRY,
    "文件": GarbageType.DRY,
    "档案": GarbageType.DRY,
    "猫砂": GarbageType.DRY,
    "狗砂": GarbageType.DRY,
    "宠物粪便": GarbageType.DRY,
    "灰尘": GarbageType.DRY,
    "煤渣": GarbageType.DRY,
    "建筑废料": GarbageType.DRY,
    "装修垃圾": GarbageType.DRY,
}

# 分类说明
CATEGORY_INFO = {
    GarbageType.RECYCLABLE: {
        "emoji": "R",
        "color": "蓝色",
        "description": "适宜回收利用的生活垃圾",
        "examples": ["废纸张", "废塑料", "废玻璃", "废金属", "废织物"],
        "tip": "保持清洁干燥，避免污染",
    },
    GarbageType.HAZARDOUS: {
        "emoji": "H",
        "color": "红色",
        "description": "对人体健康或自然环境有害的垃圾",
        "examples": ["废电池", "废灯管", "废药品", "废油漆", "废杀虫剂"],
        "tip": "轻放，避免破损泄漏",
    },
    GarbageType.WET: {
        "emoji": "W",
        "color": "棕色",
        "description": "易腐烂的生物质生活垃圾",
        "examples": ["食材废料", "剩菜剩饭", "过期食品", "果皮果核", "花卉绿植"],
        "tip": "沥干水分，去除包装",
    },
    GarbageType.DRY: {
        "emoji": "D",
        "color": "黑色",
        "description": "除以上三类外的其他生活垃圾",
        "examples": ["餐巾纸", "卫生间用纸", "塑料袋", "一次性餐具", "烟蒂"],
        "tip": "尽量保持干燥",
    },
}


def get_category_emoji(category: str) -> str:
    """获取分类对应的 emoji"""
    return CATEGORY_INFO.get(category, {}).get("emoji", "⚪")


def get_category_info(category: str) -> dict:
    """获取分类详细信息"""
    return CATEGORY_INFO.get(category, {})


def get_all_categories() -> list:
    """获取所有分类"""
    return list(CATEGORY_INFO.keys())


def get_database_size() -> int:
    """获取数据库大小"""
    return len(GARBAGE_DATABASE)

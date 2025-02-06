from dataclasses import dataclass

@dataclass
class LightBowgunData:
  x: int
  y: int

# Pointクラスのインスタンスを作成
p = LightBowgunData(10, 20)

# 属性にアクセス
print(p.x)  # 10
print(p.y)  # 20
# <a id="VirtualGeometry_World_PlanetErrorMetric"></a> Enum PlanetErrorMetric

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Cell の細かさを決める誤差の定義(Docs/Plans/VirtualGeometryNaniteMigration.md の E1 / E2)。

```csharp
public enum PlanetErrorMetric
```

## フィールド（Fields）

`ProjectedArea = 1` 

quad の一辺に sqrt(視線と地面のなす角の正弦)を掛ける。斜めに見る地面の奥行き方向の縮みを、半分だけ見込む。



`QuadSize = 0` 

画面上の quad の一辺(px)。従来。視線と地面の角度は見ない。

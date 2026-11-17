# <a id="VirtualGeometry_World_IPlanetAnchorPropertySource"></a> Interface IPlanetAnchorPropertySource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

指定Cellを描画アンカーとして、その原点からの相対頂点すべてに同じpropertyを使える供給元。
CellのLOD・タイル番号で表面の意味を変えず、shaderがアンカー相対位置から連続な値を復元すること。
per-Cell texture/tileは、この契約を実装せず既存描画または個別のrecord adapterを使う。

```csharp
public interface IPlanetAnchorPropertySource : IPlanetCellPropertySource
```

#### 実装するインターフェース（Implements）

[IPlanetCellPropertySource](VirtualGeometry.World.IPlanetCellPropertySource.md)

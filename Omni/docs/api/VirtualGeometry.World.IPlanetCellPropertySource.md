# <a id="VirtualGeometry_World_IPlanetCellPropertySource"></a> Interface IPlanetCellPropertySource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Cell の draw の MaterialPropertyBlock に、Layer の shader が使う値を外から足す口(Cell ごとの色のタイルの番号など)。
<xref href="VirtualGeometry.World.PlanetHeightTerrainSource.CellProperties" data-throw-if-not-resolved="false"></xref> に設定すると、Cell ごとの標準の値(_PlanetCellUp など)の後に呼ばれる。main thread から、
描く Cell ごとに毎 frame 呼ばれる(重い処理を入れない)。

```csharp
public interface IPlanetCellPropertySource
```

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetCellPropertySource_WriteProperties_VirtualGeometry_World_PlanetCellKey__System_Single_UnityEngine_MaterialPropertyBlock_"></a> WriteProperties\(in PlanetCellKey, float, MaterialPropertyBlock\)

key の Cell の draw の値を block に書く。priority は大きいほど先に取りたい(まだ届いていない値を要求するときの優先度)。
値が無い間も、shader が見分けられる値(例: 番号 −1)を必ず書くこと(MaterialPropertyBlock は前の Cell の値を残さないが、書かないと shader の既定値になる)。

```csharp
void WriteProperties(in PlanetCellKey key, float priority, MaterialPropertyBlock block)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`block` MaterialPropertyBlock

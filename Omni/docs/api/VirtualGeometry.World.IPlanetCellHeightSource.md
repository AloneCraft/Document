# <a id="VirtualGeometry_World_IPlanetCellHeightSource"></a> Interface IPlanetCellHeightSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Cell の格子の高さを、高さの供給元(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>をサンプルする代わりに、外から渡す口。
ストリーミングで届いた高さ、焼いた高さ、サーバーが計算した高さなどを、Cell の頂点に使う(<xref href="VirtualGeometry.World.PlanetCellMeshBuilder.BuildFromHeights(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref>)。
main thread から呼ばれる。同じ Cell には、Ready になった後は常に同じ高さを返すこと(作り直した Cell と接地の三角形が一致する前提)。

```csharp
public interface IPlanetCellHeightSource
```

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetCellHeightSource_TryGetRingHeights_VirtualGeometry_World_PlanetCellKey__System_Single_System_Double___System_Double___System_Boolean__"></a> TryGetRingHeights\(in PlanetCellKey, float, double\[\], double\[\], out bool\)

key の Cell の格子の高さ(外の 1 周を含む <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.RingSide" data-throw-if-not-resolved="false"></xref>²、行 j・列 i の順に j·RingSide+i)を ringHeights に書く。
陰影用の別の高さを持つなら shadingHeights にも書いて hasShading を true にする(持たなければ false で、書かない)。
priority は大きいほど先に取りたい(Pending を返すときの取得の優先度)。

```csharp
PlanetCellHeightStatus TryGetRingHeights(in PlanetCellKey key, float priority, double[] ringHeights, double[] shadingHeights, out bool hasShading)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`ringHeights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`shadingHeights` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

`hasShading` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [PlanetCellHeightStatus](VirtualGeometry.World.PlanetCellHeightStatus.md)

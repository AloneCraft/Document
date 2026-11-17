# <a id="VirtualGeometry_World_PlanetCraterShadingSource"></a> Class PlanetCraterShadingSource

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

生成クレーターの陰影(Shaders/PlanetCraters.hlsl の VGPlanetCraters)へ、Cell ごとの値を書く。内側の値(色タイル・色のゆらぎなど)を先に書く。
値は Cell の球面上の原点(R·中心の方向)の、段 0 の格子番号(48 ビット)と端数、シード、置かない範囲(Cell の原点からの相対位置)。並びは hlsl の冒頭の契約と同じ。

```csharp
public sealed class PlanetCraterShadingSource : IPlanetCellPropertySource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetCraterShadingSource](VirtualGeometry.World.PlanetCraterShadingSource.md)

#### 実装するインターフェース（Implements）

[IPlanetCellPropertySource](VirtualGeometry.World.IPlanetCellPropertySource.md)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetCraterShadingSource__ctor_VirtualGeometry_World_IPlanetCellPropertySource_VirtualGeometry_World_PlanetCraterField_System_Int32_"></a> PlanetCraterShadingSource\(IPlanetCellPropertySource, PlanetCraterField, int\)

```csharp
public PlanetCraterShadingSource(IPlanetCellPropertySource inner, PlanetCraterField field, int capacity)
```

#### 引数（Parameters）

`inner` [IPlanetCellPropertySource](VirtualGeometry.World.IPlanetCellPropertySource.md)

`field` [PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md)

`capacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetCraterShadingSource_Field"></a> Field

```csharp
public PlanetCraterField Field { get; }
```

#### 値（Property Value）

 [PlanetCraterField](VirtualGeometry.World.PlanetCraterField.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCraterShadingSource_TryGetValues_VirtualGeometry_World_PlanetCellKey__UnityEngine_Vector4__UnityEngine_Vector4__UnityEngine_Vector4__UnityEngine_Vector4____UnityEngine_Vector4____"></a> TryGetValues\(in PlanetCellKey, out Vector4, out Vector4, out Vector4, out Vector4\[\], out Vector4\[\]\)

key の Cell の値(検証用にも使う)。Cell の原点を作れない、格子番号が範囲外なら false。

```csharp
public bool TryGetValues(in PlanetCellKey key, out Vector4 a, out Vector4 b, out Vector4 c, out Vector4[] keepOut, out Vector4[] keepOutParams)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`a` Vector4

`b` Vector4

`c` Vector4

`keepOut` Vector4\[\]

`keepOutParams` Vector4\[\]

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCraterShadingSource_WriteProperties_VirtualGeometry_World_PlanetCellKey__System_Single_UnityEngine_MaterialPropertyBlock_"></a> WriteProperties\(in PlanetCellKey, float, MaterialPropertyBlock\)

key の Cell の draw の値を block に書く。priority は大きいほど先に取りたい(まだ届いていない値を要求するときの優先度)。
値が無い間も、shader が見分けられる値(例: 番号 −1)を必ず書くこと(MaterialPropertyBlock は前の Cell の値を残さないが、書かないと shader の既定値になる)。

```csharp
public void WriteProperties(in PlanetCellKey key, float priority, MaterialPropertyBlock block)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`block` MaterialPropertyBlock

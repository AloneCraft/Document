# <a id="VirtualGeometry_World_PlanetCellMorph"></a> Class PlanetCellMorph

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

階層の境目で細かさが跳ばないよう、Cell の頂点を親(1 つ粗い階層)の面へ連続的に寄せる(geomorph)ための、CPU 側の純関数。
頂点 shader(<code>Shaders/PlanetMorph.hlsl</code>)が同じ規則で、4 隅の寄せる割合 m(0 = 自分の形、1 = 親の面)を格子で双線形に補間し、位置と法線を寄せる。
設計: <code>Docs/Plans/VirtualGeometryNaniteMigration.md</code> §2.3.4。

```csharp
public static class PlanetCellMorph
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetCellMorph](VirtualGeometry.World.PlanetCellMorph.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCellMorph_NoMorphAtErrorRatio"></a> NoMorphAtErrorRatio

寄せる割合が 0 になる、親の画面誤差 ÷ TargetPixels。親の quad が目標の 2 倍に見えるなら、子は目標どおりなので、そのまま使う。

```csharp
public const float NoMorphAtErrorRatio = 2
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellMorph_Amount_System_Single_System_Single_System_Single_"></a> Amount\(float, float, float\)

親の画面誤差 parentError(px)から、寄せる割合(0〜1)を求める。誤差が目標より下がる(合併に近い)ほど 1(親の面と同じ形)、
2 倍以上なら 0。滑らか(smoothstep)で、split・merge が起きうる範囲(目標の (1±ヒステリシス) 倍)では 1 なので、入れ替わっても形が跳ばない。

```csharp
public static float Amount(float parentError, float targetPixels, float hysteresis)
```

#### 引数（Parameters）

`parentError` [float](https://learn.microsoft.com/dotnet/api/system.single)

`targetPixels` [float](https://learn.microsoft.com/dotnet/api/system.single)

`hysteresis` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellMorph_CornerAmounts_VirtualGeometry_World_PlanetCellKey__System_Single___System_Single_System_Single_System_Func_VirtualGeometry_World_PlanetCellKey_System_Int32__System_Single___"></a> CornerAmounts\(in PlanetCellKey, float\[\], float, float, Func<PlanetCellKey, int\>, float\[\]\)

4 隅の寄せる割合。隅ごとに、その隅を共有する Cell(辺の隣 2 つと対角の 1 つ)のどれかが自分より粗ければ 1 にする
(粗い Cell の辺・隅に細かい側を載せて、割れを作らない。隅の値は位置と階層だけで決まるので、隅を共有する同じ階層の Cell と一致する)。
coverLevel は、選ばれた Cell の集合で、引数の Cell の領域を覆っている Cell の階層(祖先を含む。覆う Cell が無ければ −1)。

```csharp
public static void CornerAmounts(in PlanetCellKey key, float[] parentErrors, float targetPixels, float hysteresis, Func<PlanetCellKey, int> coverLevel, float[] result)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`parentErrors` [float](https://learn.microsoft.com/dotnet/api/system.single)\[\]

`targetPixels` [float](https://learn.microsoft.com/dotnet/api/system.single)

`hysteresis` [float](https://learn.microsoft.com/dotnet/api/system.single)

`coverLevel` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md), [int](https://learn.microsoft.com/dotnet/api/system.int32)\>

`result` [float](https://learn.microsoft.com/dotnet/api/system.single)\[\]

### <a id="VirtualGeometry_World_PlanetCellMorph_CornerOffsets_System_Int32_System_Int32__System_Int32__"></a> CornerOffsets\(int, out int, out int\)

隅の番号: 0 = (0,0)、1 = (N,0)、2 = (0,N)、3 = (N,N)(格子の x が右、y が上)。

```csharp
public static void CornerOffsets(int corner, out int dx, out int dy)
```

#### 引数（Parameters）

`corner` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`dx` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`dy` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellMorph_DisplacementBound_UnityEngine_Vector3_System_Single_UnityEngine_Vector3_System_Single_System_Single_"></a> DisplacementBound\(Vector3, float, Vector3, float, float\)

2 つの球に含まれる点どうしの距離の上界。線形 morph の最大移動量として cluster のカリング半径へ加える。

```csharp
public static float DisplacementBound(Vector3 childCenter, float childRadius, Vector3 parentCenter, float parentRadius, float maximumAmount)
```

#### 引数（Parameters）

`childCenter` Vector3

`childRadius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`parentCenter` Vector3

`parentRadius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`maximumAmount` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellMorph_Interpolate_System_Single___System_Int32_System_Int32_System_Int32_"></a> Interpolate\(float\[\], int, int, int\)

隅の 4 つの割合から、格子の点 (i, j)(0〜n)の割合(双線形)。

```csharp
public static float Interpolate(float[] corners, int n, int i, int j)
```

#### 引数（Parameters）

`corners` [float](https://learn.microsoft.com/dotnet/api/system.single)\[\]

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`i` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`j` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellMorph_ParentReference_System_Int32_System_Int32_System_Int32_System_Int32_System_Int32_System_Int32__System_Int32__System_Int32__System_Int32__"></a> ParentReference\(int, int, int, int, int, out int, out int, out int, out int\)

子の格子の点 (i, j)(0〜n)が載る親の面を、親の頂点の参照(最大 2 つ)で表す(頂点 shader と同じ規則)。親の面は、親の三角形(格子の四角の b–c の対角線で 2 分割)。
偶数×偶数は親の頂点 1 つ、辺の中点は 2 つの平均、四角の中心は対角線 b=(x+1,y)・c=(x,y+1) の平均。
quadrantX・quadrantY は、子が親の何番目の子か(0 または 1)。返す値は親の格子の座標 (pi0,pj0)・(pi1,pj1)(同じなら 1 つ)。

```csharp
public static void ParentReference(int n, int quadrantX, int quadrantY, int i, int j, out int pi0, out int pj0, out int pi1, out int pj1)
```

#### 引数（Parameters）

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`quadrantX` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`quadrantY` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`i` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`j` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pi0` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pj0` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pi1` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pj1` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellMorph_TouchesCoarserCell_VirtualGeometry_World_PlanetCellKey__System_Int32_System_Func_VirtualGeometry_World_PlanetCellKey_System_Int32__"></a> TouchesCoarserCell\(in PlanetCellKey, int, Func<PlanetCellKey, int\>\)

隅 corner を共有する他の Cell(辺の隣 2 つ・対角 1 つ)に、key より粗い階層の Cell があるか。

```csharp
public static bool TouchesCoarserCell(in PlanetCellKey key, int corner, Func<PlanetCellKey, int> coverLevel)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`corner` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`coverLevel` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md), [int](https://learn.microsoft.com/dotnet/api/system.int32)\>

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

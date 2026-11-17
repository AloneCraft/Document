# <a id="VirtualGeometry_World_PlanetCellFrame"></a> Struct PlanetCellFrame

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Cell の中心の値を Logical 精度(Omni の Q95.96 固定小数点)で持つ。
頂点は Cell の原点からの相対量だけを float で持ち、float にすると精度が足りない値(中心の正接、Cell の原点、ノイズの格子の基点)はここで求める。
中心の角度は π·n/2^(L+2)(n=2x+1−2^L)で、n/2^(L+2) を固定小数点で正確に作るので、階層は <xref href="VirtualGeometry.World.PlanetCellFrame.MaximumLevel" data-throw-if-not-resolved="false"></xref> までに限る。
Cell の原点(<xref href="VirtualGeometry.World.PlanetCellFrame.Origin" data-throw-if-not-resolved="false"></xref>)は、中心の方向の地表の高さ(<xref href="VirtualGeometry.World.PlanetCellFrame.HeightShift" data-throw-if-not-resolved="false"></xref>)だけ半径 R の球面から持ち上げた点。
頂点の高さ方向の成分が地形の起伏ぶんの大きさになるので、起伏が数 km あっても float の刻みが mm を超えない。
ノイズの格子・波の位相・実データの方向など、高さ 0 の球面で定義する値は <xref href="VirtualGeometry.World.PlanetCellFrame.SphereOrigin" data-throw-if-not-resolved="false"></xref> から求める(持ち上げた原点から求めると、隣の Cell と食い違う)。

```csharp
public readonly struct PlanetCellFrame
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCellFrame_ApproximateOrigin"></a> ApproximateOrigin

Origin の float の近似(選択・bounds・Unity の world 空間での配置用)。

```csharp
public readonly Vector3 ApproximateOrigin
```

#### 値（Field Value）

 Vector3

### <a id="VirtualGeometry_World_PlanetCellFrame_ApproximateSphereOrigin"></a> ApproximateSphereOrigin

SphereOrigin の float の近似。

```csharp
public readonly Vector3 ApproximateSphereOrigin
```

#### 値（Field Value）

 Vector3

### <a id="VirtualGeometry_World_PlanetCellFrame_ApproximateTangent"></a> ApproximateTangent

TangentU、TangentV の float の近似(頂点の生成用)。

```csharp
public readonly Vector2 ApproximateTangent
```

#### 値（Field Value）

 Vector2

### <a id="VirtualGeometry_World_PlanetCellFrame_Direction"></a> Direction

Cell の中心の外向きの単位方向(Logical)。

```csharp
public readonly Vector3 Direction
```

#### 値（Field Value）

 Vector3

### <a id="VirtualGeometry_World_PlanetCellFrame_HeightShift"></a> HeightShift

Origin を SphereOrigin から外向きに持ち上げた距離(m、float)。GPU にも同じ値を渡す。持ち上げない Cell は 0。

```csharp
public readonly float HeightShift
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellFrame_Key"></a> Key

```csharp
public readonly PlanetCellKey Key
```

#### 値（Field Value）

 [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

### <a id="VirtualGeometry_World_PlanetCellFrame_MaximumLevel"></a> MaximumLevel

中心の角度の分数 n/2^(L+2) を小数部 96 ビットで正確に表せる最大の階層。

```csharp
public const int MaximumLevel = 94
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellFrame_Origin"></a> Origin

惑星のローカル座標での Cell の原点 = SphereOrigin + HeightShift·Direction(Cell の中心の方向の地表の高さの点)。頂点はここからの相対位置。

```csharp
public readonly Vector3 Origin
```

#### 値（Field Value）

 Vector3

### <a id="VirtualGeometry_World_PlanetCellFrame_SphereOrigin"></a> SphereOrigin

Cell の中心の方向の、半径 R の球面(高さ 0)上の点 R·p0/|p0|(p0=n+x0·u+y0·v)。ノイズの格子・波の位相・実データの方向の基点。

```csharp
public readonly Vector3 SphereOrigin
```

#### 値（Field Value）

 Vector3

### <a id="VirtualGeometry_World_PlanetCellFrame_TangentU"></a> TangentU

中心の面の座標の正接(等角写像の x0、y0)。

```csharp
public readonly Scalar TangentU
```

#### 値（Field Value）

 Scalar

### <a id="VirtualGeometry_World_PlanetCellFrame_TangentV"></a> TangentV

```csharp
public readonly Scalar TangentV
```

#### 値（Field Value）

 Scalar

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellFrame_TryCreate_VirtualGeometry_World_PlanetCellKey__Omni_Logical_Scalar__VirtualGeometry_World_PlanetCellFrame__"></a> TryCreate\(in PlanetCellKey, in Scalar, out PlanetCellFrame\)

```csharp
public static bool TryCreate(in PlanetCellKey key, in Scalar radius, out PlanetCellFrame frame)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`radius` Scalar

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellFrame_TryCreatePlane_VirtualGeometry_World_PlanetCellKey__Omni_Logical_Scalar__VirtualGeometry_World_PlanetCellFrame__"></a> TryCreatePlane\(in PlanetCellKey, in Scalar, out PlanetCellFrame\)

平面の Cell の値。一辺 extent(m)の正方形の平面(局所座標の XZ、原点が正方形の中心、法線 +Y)を、階層 L の 2^L×2^L の Cell に分けた 1 つ。
Cell の中心 = extent·(2x+1−2^L)/2^(L+1)(x は key.X が x、key.Y が z)を、Logical で正確に作る。球の面 +Y(<xref href="VirtualGeometry.World.CubeSphere" data-throw-if-not-resolved="false"></xref> の面 2)と同じ向き。
原点は持ち上げず(<xref href="VirtualGeometry.World.PlanetCellFrame.HeightShift" data-throw-if-not-resolved="false"></xref> = 0)、<xref href="VirtualGeometry.World.PlanetCellFrame.SphereOrigin" data-throw-if-not-resolved="false"></xref> は <xref href="VirtualGeometry.World.PlanetCellFrame.Origin" data-throw-if-not-resolved="false"></xref> と同じ、<xref href="VirtualGeometry.World.PlanetCellFrame.Direction" data-throw-if-not-resolved="false"></xref> は (0,1,0)。

```csharp
public static bool TryCreatePlane(in PlanetCellKey key, in Scalar extent, out PlanetCellFrame frame)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`extent` Scalar

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellFrame_TryNoiseLattice_Omni_Logical_Scalar__System_Int32_UnityEngine_Vector3Int__UnityEngine_Vector3__"></a> TryNoiseLattice\(in Scalar, int, out Vector3Int, out Vector3\)

波長の逆数 inverseWavelength·2^octave の格子で、原点の格子番号(下位 32 ビット、負の無限大方向へ切り捨て)と端数(0〜1)を返す。
格子番号は 2^32 で巡回する(ノイズの hash は uint で巡回するので、値は変わらない)。

```csharp
public bool TryNoiseLattice(in Scalar inverseWavelength, int octave, out Vector3Int lattice, out Vector3 fraction)
```

#### 引数（Parameters）

`inverseWavelength` Scalar

`octave` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`lattice` Vector3Int

`fraction` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellFrame_TryWavePhase_Omni_Logical_Vector3__Omni_Logical_Scalar__System_Single__"></a> TryWavePhase\(in Vector3, in Scalar, out float\)

単位方向 direction・波長の逆数 inverseWavelength の平面波の、原点での位相(周期の端数、0〜1)。
(direction·原点)/波長 を Logical で求めて端数だけを取るので、惑星が大きくても位相が潰れない。

```csharp
public bool TryWavePhase(in Vector3 direction, in Scalar inverseWavelength, out float fraction)
```

#### 引数（Parameters）

`direction` Vector3

`inverseWavelength` Scalar

`fraction` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellFrame_TryWithHeightShift_System_Single_VirtualGeometry_World_PlanetCellFrame__"></a> TryWithHeightShift\(float, out PlanetCellFrame\)

Origin を SphereOrigin から外向きに heightShift(m)だけ持ち上げた Cell の値を返す。
Origin·(shift/R) の比ではなく、単位方向 × shift で作る(R=10^20 m でも、固定小数点の絶対精度 2^-96 のまま足せる)。
heightShift は float のまま使う(float は Logical に正確に変換でき、GPU にも同じ値を渡せる)。有限でないときは false。

```csharp
public bool TryWithHeightShift(float heightShift, out PlanetCellFrame shifted)
```

#### 引数（Parameters）

`heightShift` [float](https://learn.microsoft.com/dotnet/api/system.single)

`shifted` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

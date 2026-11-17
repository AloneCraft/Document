# <a id="Omni_VirtualObject_VirtualObjectSelector"></a> Class VirtualObjectSelector

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Virtual Object の表現の選択（Docs/Plans/AsteriaVirtualObject.md の不変条件 1・2）。画面上の大きさ（画素）だけで表現の段（0 が最も粗い）を選ぶ。
段 i + 1 へ上がる画素の大きさ enter[i] は、対象ごとではなく段ごとの共通の値にできる（距離の m ではなく画素で決めるので、視野角や解像度が変わっても矛盾しない）。
ヒステリシス: 上がるには enter × hysteresis 以上、下がるには enter ÷ hysteresis 未満が要る（境で行き来しない）。
準備待ち: 上の段は準備ができている（ready）ときだけ選ぶ。できていなければ今の段のまま描き続ける（VG の「子が揃うまで親を描く」と同じ）。
Asteria の型には依存しない（後で VG へ統合するときにそのまま移せる）。

```csharp
public sealed class VirtualObjectSelector
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualObjectSelector](Omni.VirtualObject.VirtualObjectSelector.md)

## コンストラクター（Constructors）

### <a id="Omni_VirtualObject_VirtualObjectSelector__ctor_System_Double___System_Double_"></a> VirtualObjectSelector\(double\[\], double\)

```csharp
public VirtualObjectSelector(double[] enterPixels, double hysteresis = 1.25)
```

#### 引数（Parameters）

`enterPixels` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

段 i + 1 へ上がる画素の大きさ（昇順、正）。段の数は enterPixels.Length + 1。

`hysteresis` [double](https://learn.microsoft.com/dotnet/api/system.double)

1 以上。大きいほど段の境で行き来しにくい。

## プロパティ（Properties）

### <a id="Omni_VirtualObject_VirtualObjectSelector_LevelCount"></a> LevelCount

段の数。

```csharp
public int LevelCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_VirtualObject_VirtualObjectSelector_DistanceForPixels_System_Double_System_Double_System_Double_System_Double_"></a> DistanceForPixels\(double, double, double, double\)

直径 size（m）の対象が pixels（画素）に見える距離（m）。ProjectedPixels の逆（小さい角の近似でなく、正確な逆）。

```csharp
public static double DistanceForPixels(double size, double pixels, double fovRadians, double screenHeight)
```

#### 引数（Parameters）

`size` [double](https://learn.microsoft.com/dotnet/api/system.double)

`pixels` [double](https://learn.microsoft.com/dotnet/api/system.double)

`fovRadians` [double](https://learn.microsoft.com/dotnet/api/system.double)

`screenHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_VirtualObject_VirtualObjectSelector_Ideal_System_Double_"></a> Ideal\(double\)

ヒステリシスなしの段（画素の大きさだけで決まる、状態を持たない値。診断と初期化に使う）。

```csharp
public int Ideal(double pixels)
```

#### 引数（Parameters）

`pixels` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_VirtualObject_VirtualObjectSelector_LinearScreenSize_System_Single_System_Single_System_Single_"></a> LinearScreenSize\(float, float, float\)

長さ length が距離 distance で画面に占める大きさ（画素。小さい角の直線近似 length × projectionScale / distance）。
VG の <code>PlanetCellSelector.ScreenError</code>（quad の弧の長さ × 倍率 × 射影の倍率 ÷ 距離）はこの式で、VO の選択（Select）が使う画素の大きさと同じ尺度になる。

```csharp
public static float LinearScreenSize(float length, float distance, float projectionScale)
```

#### 引数（Parameters）

`length` [float](https://learn.microsoft.com/dotnet/api/system.single)

`distance` [float](https://learn.microsoft.com/dotnet/api/system.single)

`projectionScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_VirtualObject_VirtualObjectSelector_ProjectedPixels_System_Double_System_Double_System_Double_System_Double_"></a> ProjectedPixels\(double, double, double, double\)

半径 radius（m）の対象が、距離 distance（m）で画面の高さ screenHeight（画素）に占める直径（画素）。fovRadians は縦の視野角。

```csharp
public static double ProjectedPixels(double radius, double distance, double fovRadians, double screenHeight)
```

#### 引数（Parameters）

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`distance` [double](https://learn.microsoft.com/dotnet/api/system.double)

`fovRadians` [double](https://learn.microsoft.com/dotnet/api/system.double)

`screenHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_VirtualObject_VirtualObjectSelector_ProjectionScale_System_Single_System_Single_"></a> ProjectionScale\(float, float\)

縦の視野角 fovRadians・画面の高さ screenHeight（画素）の射影の倍率（画素 / 距離 1 あたりの長さ。長さ L が距離 d で L × 倍率 / d 画素に見える）。
VG の <code>PlanetSelectionView.ProjectionScale</code> と同じ意味。

```csharp
public static float ProjectionScale(float fovRadians, float screenHeight)
```

#### 引数（Parameters）

`fovRadians` [float](https://learn.microsoft.com/dotnet/api/system.single)

`screenHeight` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_VirtualObject_VirtualObjectSelector_Select_System_Double_System_Int32_System_Func_System_Int32_System_Boolean__"></a> Select\(double, int, Func<int, bool\>\)

次の段を返します。pixels は対象の画面上の大きさ（画素。NaN・負は 0 として最も粗い段）、current は今の段、ready は「その段が描ける状態か」（null なら常に true）。
一度に複数の段を上がれる（遠くから急に近づいたとき）。準備ができていない段で止まる（その下までで止まり、上は選ばない）。

```csharp
public int Select(double pixels, int current, Func<int, bool> ready = null)
```

#### 引数（Parameters）

`pixels` [double](https://learn.microsoft.com/dotnet/api/system.double)

`current` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`ready` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[int](https://learn.microsoft.com/dotnet/api/system.int32), [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

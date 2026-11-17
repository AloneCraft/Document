# <a id="Omni_Celestial_SchwarzschildLensTable"></a> Class SchwarzschildLensTable

Namespace: [Omni.Celestial](Omni.Celestial.md)  
Assembly: Omni.Celestial.Core.dll  

シュヴァルツシルト時空の光線が、半径 r の点から無限遠まで進む間に中心のまわりを回る角度 Δφ の表（単位は Rs = 1）。
ブラックホールのそばの点（例: 降着円盤の粒子）の見かけの位置を求めるのに使います: 点と観測者が中心から見て角 ψ だけ
離れているとき、Δφ = ψ となる光線が一次像、Δφ = 2π − ψ が中心の裏を回る二次像です。
GPU では、表を半径の行ごとに二分探索して Δφ − asin(b/D) = 目標の角（D は観測者の距離）となる b を求め、
観測者から見た光の向き（中心から asin(b/D) だけ傾いた向き）を作ります。
光線の軌道の式 (du/dφ)² = 1/b² − u² + u³（u = 1/r）を数値積分します。
横軸 s ∈ [0, 1) は光線を1本の単調な列に並べたもの: 前半は外向きに出る光線（衝突パラメーター b を 0 から、半径 r で
接線方向になる b_t = r/√(1 − 1/r) まで）、後半は一度内向きに進み、近点を回ってから出る光線（b を b_t から光子球の
b_c = 3√3/2 まで）。Δφ は s とともに単調に増え、s → 1 で発散します（光子球をまわる光）。
縦軸は r ∈ [RMin, RMax]。テクスチャ（RGHalf）: R = Δφ、G = b。

```csharp
public static class SchwarzschildLensTable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[SchwarzschildLensTable](Omni.Celestial.SchwarzschildLensTable.md)

## フィールド（Fields）

### <a id="Omni_Celestial_SchwarzschildLensTable_Columns"></a> Columns

```csharp
public const int Columns = 256
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Celestial_SchwarzschildLensTable_CriticalImpact"></a> CriticalImpact

光子球の衝突パラメーター（Rs 単位）。

```csharp
public const double CriticalImpact = 2.598076211353316
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Celestial_SchwarzschildLensTable_MaximumSweep"></a> MaximumSweep

テクスチャに書く Δφ の上限（rad）。光子球のそばで発散する値を半精度に収めます。

```csharp
public const double MaximumSweep = 60
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Celestial_SchwarzschildLensTable_RMax"></a> RMax

```csharp
public const float RMax = 14
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Celestial_SchwarzschildLensTable_RMin"></a> RMin

```csharp
public const float RMin = 1.6
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Celestial_SchwarzschildLensTable_Rows"></a> Rows

```csharp
public const int Rows = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Celestial_SchwarzschildLensTable_Texture"></a> Texture

表のテクスチャ（無ければ作る）。

```csharp
public static Texture2D Texture { get; }
```

#### 値（Property Value）

 Texture2D

## メソッド（Methods）

### <a id="Omni_Celestial_SchwarzschildLensTable_Create"></a> Create\(\)

```csharp
public static Texture2D Create()
```

#### 戻り値（Returns）

 Texture2D

### <a id="Omni_Celestial_SchwarzschildLensTable_Outward_System_Double_System_Double_"></a> Outward\(double, double\)

半径 r から外向きに無限遠まで: ∫_0^{1/r} du / √(1/b² − u² + u³)。

```csharp
public static double Outward(double r, double b)
```

#### 引数（Parameters）

`r` [double](https://learn.microsoft.com/dotnet/api/system.double)

`b` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Celestial_SchwarzschildLensTable_Periapsis_System_Double_System_Double_"></a> Periapsis\(double, double\)

半径 r から内向きに近点まで: ∫_{1/r}^{u_p} du / √(…)（u_p は 1/b² − u² + u³ = 0 の最小の正根）。

```csharp
public static double Periapsis(double r, double b)
```

#### 引数（Parameters）

`r` [double](https://learn.microsoft.com/dotnet/api/system.double)

`b` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Celestial_SchwarzschildLensTable_Sample_System_Double_System_Double_System_Double__System_Double__"></a> Sample\(double, double, out double, out double\)

表の1点: s から衝突パラメーター b と、半径 r から無限遠までに回る角度 Δφ。

```csharp
public static void Sample(double r, double s, out double sweep, out double impact)
```

#### 引数（Parameters）

`r` [double](https://learn.microsoft.com/dotnet/api/system.double)

`s` [double](https://learn.microsoft.com/dotnet/api/system.double)

`sweep` [double](https://learn.microsoft.com/dotnet/api/system.double)

`impact` [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Celestial_SchwarzschildLensTable_TangentImpact_System_Double_"></a> TangentImpact\(double\)

接線方向になる衝突パラメーター b_t（半径 r で光線が動径に垂直）。

```csharp
public static double TangentImpact(double r)
```

#### 引数（Parameters）

`r` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Celestial_SchwarzschildLensTable_TurningPoint_System_Double_"></a> TurningPoint\(double\)

近点の u（光子球の外を通る b &gt; b_c の光線だけ）。

```csharp
public static double TurningPoint(double b)
```

#### 引数（Parameters）

`b` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

# <a id="Omni_OmniVirtualShadowSettings"></a> Struct OmniVirtualShadowSettings

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

仮想シャドウマップの数値(Docs/Plans/VirtualShadowMaps.md)。

```csharp
public readonly struct OmniVirtualShadowSettings
```

## コンストラクター（Constructors）

### <a id="Omni_OmniVirtualShadowSettings__ctor_System_Int32_System_Double_System_Int32_System_Int32_System_Int32_System_Int32_System_Double_"></a> OmniVirtualShadowSettings\(int, double, int, int, int, int, double\)

```csharp
public OmniVirtualShadowSettings(int levels, double level0HalfExtentMeters, int pagesPerAxis, int pageTexels, int physicalPagesPerAxis, int pagesPerFrame, double minimumDepthRangeMeters)
```

#### 引数（Parameters）

`levels` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`level0HalfExtentMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`pagesPerAxis` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pageTexels` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`physicalPagesPerAxis` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pagesPerFrame` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`minimumDepthRangeMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

## フィールド（Fields）

### <a id="Omni_OmniVirtualShadowSettings_Level0HalfExtentMeters"></a> Level0HalfExtentMeters

段 0 の半幅(m)。1 段ごとに 2 倍。

```csharp
public readonly double Level0HalfExtentMeters
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_OmniVirtualShadowSettings_Levels"></a> Levels

段の数(段 0 が最も細かい)。

```csharp
public readonly int Levels
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowSettings_MinimumDepthRangeMeters"></a> MinimumDepthRangeMeters

光の向きの奥行きの範囲(m、基準点の前後)の下限。段の半幅の 4 倍と比べて大きい方を使う。

```csharp
public readonly double MinimumDepthRangeMeters
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_OmniVirtualShadowSettings_PageTexels"></a> PageTexels

1 ページの 1 辺のテクセル数。

```csharp
public readonly int PageTexels
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowSettings_PagesPerAxis"></a> PagesPerAxis

1 段の 1 辺のページ数。

```csharp
public readonly int PagesPerAxis
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowSettings_PagesPerFrame"></a> PagesPerFrame

1 フレームに描くページの上限。

```csharp
public readonly int PagesPerFrame
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowSettings_PhysicalPagesPerAxis"></a> PhysicalPagesPerAxis

物理ページの置き場の 1 辺のページ数(置き場の 1 辺 = これ × PageTexels)。

```csharp
public readonly int PhysicalPagesPerAxis
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_OmniVirtualShadowSettings_Default"></a> Default

初版の値: 16 段、段 0 の半幅 4 m、1 段 128² ページ × 128² テクセル(仮想 16384²)、置き場 64² ページ(8192²)、1 フレーム 64 ページ、奥行き 2 km 以上。

```csharp
public static OmniVirtualShadowSettings Default { get; }
```

#### 値（Property Value）

 [OmniVirtualShadowSettings](Omni.OmniVirtualShadowSettings.md)

### <a id="Omni_OmniVirtualShadowSettings_PagesPerLevel"></a> PagesPerLevel

```csharp
public int PagesPerLevel { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowSettings_PhysicalPageCount"></a> PhysicalPageCount

```csharp
public int PhysicalPageCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowSettings_PhysicalTexelsPerAxis"></a> PhysicalTexelsPerAxis

```csharp
public int PhysicalTexelsPerAxis { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowSettings_VirtualTexelsPerAxis"></a> VirtualTexelsPerAxis

```csharp
public int VirtualTexelsPerAxis { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_OmniVirtualShadowSettings_DepthRange_System_Int32_"></a> DepthRange\(int\)

段 k の奥行きの範囲(m、基準点の前後)。

```csharp
public double DepthRange(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_OmniVirtualShadowSettings_HalfExtent_System_Int32_"></a> HalfExtent\(int\)

段 k の半幅(m)。

```csharp
public double HalfExtent(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_OmniVirtualShadowSettings_Texel_System_Int32_"></a> Texel\(int\)

段 k の 1 テクセルの大きさ(m)。

```csharp
public double Texel(int level)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

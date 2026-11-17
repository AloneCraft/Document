# <a id="VirtualGeometry_Streaming_ResidentCellHeights"></a> Class ResidentCellHeights

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

浅い階層(<xref href="VirtualGeometry.Streaming.ResidentCellHeights.Level" data-throw-if-not-resolved="false"></xref>)の全ての Cell の格子を、最初に読み込んで手放さない「常駐する粗い層」。
細かい格子(<xref href="VirtualGeometry.Streaming.StreamedPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)が届いていない場所の高さを、接地・岩などの問い合わせに答える予備に使う
(<xref href="VirtualGeometry.World.PlanetFallbackHeightProvider" data-throw-if-not-resolved="false"></xref>)。VG の Cell を作る供給元には使わない。
揃うまでは、まだ持っていない方向に NaN を返す。<xref href="VirtualGeometry.Streaming.ResidentCellHeights.Tick" data-throw-if-not-resolved="false"></xref> を main thread で毎 frame 呼ぶ(揃ったら何もしない)。
補間は <xref href="VirtualGeometry.Streaming.StreamedPlanetHeightProvider" data-throw-if-not-resolved="false"></xref> と同じ双三次。格子は作られた後に変わらないので、別 thread から読んでよい。

```csharp
public sealed class ResidentCellHeights : IThreadSafePlanetHeightProvider, IPlanetHeightProvider, IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ResidentCellHeights](VirtualGeometry.Streaming.ResidentCellHeights.md)

#### 実装するインターフェース（Implements）

IThreadSafePlanetHeightProvider, 
IPlanetHeightProvider, 
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_Streaming_ResidentCellHeights__ctor_Omni_Streaming_StreamingHost_System_UInt32_System_Int32_System_Double_"></a> ResidentCellHeights\(StreamingHost, uint, int, double\)

```csharp
public ResidentCellHeights(StreamingHost host, uint layer, int level, double maximumAbsoluteHeightMeters)
```

#### 引数（Parameters）

`host` [StreamingHost](Omni.Streaming.StreamingHost.md)

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumAbsoluteHeightMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

## フィールド（Fields）

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_Priority"></a> Priority

取得の優先度(細かい格子の取得より低くする)。

```csharp
public float Priority
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## プロパティ（Properties）

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_ByteCount"></a> ByteCount

持っている格子のバイト数(復号後)。

```csharp
public long ByteCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_IsComplete"></a> IsComplete

```csharp
public bool IsComplete { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_Layer"></a> Layer

```csharp
public uint Layer { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_Level"></a> Level

```csharp
public int Level { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_ResidentCount"></a> ResidentCount

```csharp
public int ResidentCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_TotalCount"></a> TotalCount

この階層の Cell の数(6 × 4^Level)。

```csharp
public int TotalCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_UnavailableCount"></a> UnavailableCount

取得に失敗した・pack に無い Cell の数(0 でなければ、その場所は予備でも答えられない)。

```csharp
public int UnavailableCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

```csharp
public double SampleHeightMeters(double unitX, double unitY, double unitZ, double spacingMeters)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_Streaming_ResidentCellHeights_Tick"></a> Tick\(\)

届いた格子を受け取り、まだ届いていないものの取得を宣言する。main thread から毎 frame 呼ぶ。

```csharp
public void Tick()
```

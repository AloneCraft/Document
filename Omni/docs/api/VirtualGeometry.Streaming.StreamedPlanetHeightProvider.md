# <a id="VirtualGeometry_Streaming_StreamedPlanetHeightProvider"></a> Class StreamedPlanetHeightProvider

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

ストリーミングで確保した(<xref href="VirtualGeometry.Streaming.StreamedCellHeightSource.TryGetPinned(Omni.Streaming.StreamKey%40%2cVirtualGeometry.Streaming.CellHeightGrid%40)" data-throw-if-not-resolved="false"></xref>)階層 MaximumLevel の Cell の格子から、方向の高さを双三次補間で返す。
焼いた階層より細かい Cell を作る供給元として、<xref href="VirtualGeometry.World.PlanetAmplifiedHeightProvider" data-throw-if-not-resolved="false"></xref> の基(basis)に使う: 焼いた分解能までは実データ、その先は増幅ノイズ。
確保した格子の外(まだ届いていない・手放した)の方向は NaN を返し、Cell は作られない(偽の高さで埋めない)。
確保した格子は作られた後に変わらず、別 thread から読んでよい。補間は格子点で格子の値そのものになる。

```csharp
public sealed class StreamedPlanetHeightProvider : IPlanetHeightBoundsSource, IThreadSafePlanetHeightProvider, IPlanetGpuHeightInputSource, IPlanetHeightProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[StreamedPlanetHeightProvider](VirtualGeometry.Streaming.StreamedPlanetHeightProvider.md)

#### 実装するインターフェース（Implements）

IPlanetHeightBoundsSource, 
IThreadSafePlanetHeightProvider, 
IPlanetGpuHeightInputSource, 
IPlanetHeightProvider

## コンストラクター（Constructors）

### <a id="VirtualGeometry_Streaming_StreamedPlanetHeightProvider__ctor_VirtualGeometry_Streaming_StreamedCellHeightSource_System_Double_"></a> StreamedPlanetHeightProvider\(StreamedCellHeightSource, double\)

```csharp
public StreamedPlanetHeightProvider(StreamedCellHeightSource source, double maximumAbsoluteHeightMeters)
```

#### 引数（Parameters）

`source` [StreamedCellHeightSource](VirtualGeometry.Streaming.StreamedCellHeightSource.md)

`maximumAbsoluteHeightMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

## プロパティ（Properties）

### <a id="VirtualGeometry_Streaming_StreamedPlanetHeightProvider_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

高さの絶対値の上界(m)。Cell の選択の bounds に含める。

```csharp
public double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_StreamedPlanetHeightProvider_PrepareGpuHeightInput_VirtualGeometry_World_PlanetCellFrame__System_Int32_System_Double_System_Int32_VirtualGeometry_World_PlanetGpuHeightBasis__System_String__"></a> PrepareGpuHeightInput\(in PlanetCellFrame, int, double, int, out PlanetGpuHeightBasis, out string\)

同じcube面の各主tileから、CPUと同じclampを持つ係数をコピーする。haloの不足はPending。

```csharp
public PlanetGpuHeightInputStatus PrepareGpuHeightInput(in PlanetCellFrame frame, int gridQuads, double spacingMeters, int maximumPatches, out PlanetGpuHeightBasis input, out string reason)
```

#### 引数（Parameters）

`frame` PlanetCellFrame

`gridQuads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`spacingMeters` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximumPatches` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`input` PlanetGpuHeightBasis

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 PlanetGpuHeightInputStatus

### <a id="VirtualGeometry_Streaming_StreamedPlanetHeightProvider_SampleHeightMeters_System_Double_System_Double_System_Double_System_Double_"></a> SampleHeightMeters\(double, double, double, double\)

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

### <a id="VirtualGeometry_Streaming_StreamedPlanetHeightProvider_TryGetHeightRange_VirtualGeometry_World_PlanetCellFrame__System_Double_System_Double__System_Double__"></a> TryGetHeightRange\(in PlanetCellFrame, double, out double, out double\)

```csharp
public bool TryGetHeightRange(in PlanetCellFrame frame, double spacing, out double minimum, out double maximum)
```

#### 引数（Parameters）

`frame` PlanetCellFrame

`spacing` [double](https://learn.microsoft.com/dotnet/api/system.double)

`minimum` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximum` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

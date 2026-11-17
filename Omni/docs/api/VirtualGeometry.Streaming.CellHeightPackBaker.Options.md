# <a id="VirtualGeometry_Streaming_CellHeightPackBaker_Options"></a> Class CellHeightPackBaker.Options

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

```csharp
public sealed class CellHeightPackBaker.Options
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CellHeightPackBaker.Options](VirtualGeometry.Streaming.CellHeightPackBaker.Options.md)

## フィールド（Fields）

### <a id="VirtualGeometry_Streaming_CellHeightPackBaker_Options_Face"></a> Face

```csharp
public int Face
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CellHeightPackBaker_Options_Heights"></a> Heights

```csharp
public IPlanetHeightProvider Heights
```

#### 値（Field Value）

 IPlanetHeightProvider

### <a id="VirtualGeometry_Streaming_CellHeightPackBaker_Options_Layer"></a> Layer

```csharp
public uint Layer
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_Streaming_CellHeightPackBaker_Options_MaximumLevel"></a> MaximumLevel

```csharp
public int MaximumLevel
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CellHeightPackBaker_Options_Metadata"></a> Metadata

付随情報に足す値(出典、天体名など)。

```csharp
public readonly Dictionary<string, string> Metadata
```

#### 値（Field Value）

 [Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="VirtualGeometry_Streaming_CellHeightPackBaker_Options_RadiusMeters"></a> RadiusMeters

```csharp
public double RadiusMeters
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_Streaming_CellHeightPackBaker_Options_ShadingHeights"></a> ShadingHeights

法線に使う別の高さ(null なら持たない)。

```csharp
public IPlanetShadingHeightProvider ShadingHeights
```

#### 値（Field Value）

 IPlanetShadingHeightProvider

### <a id="VirtualGeometry_Streaming_CellHeightPackBaker_Options_Step"></a> Step

量子化の刻み(メートル)。int16 で ±32767·Step を表せる範囲に地形が収まること。全 pack で共通にする(継ぎ目のため)。

```csharp
public float Step
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

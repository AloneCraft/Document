# <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_Options"></a> Class CellAlbedoPackBaker.Options

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

```csharp
public sealed class CellAlbedoPackBaker.Options
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CellAlbedoPackBaker.Options](VirtualGeometry.Streaming.CellAlbedoPackBaker.Options.md)

## フィールド（Fields）

### <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_Options_Border"></a> Border

外周の余白の画素数。Size + 2·Border が 4 の倍数であること。

```csharp
public int Border
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_Options_Face"></a> Face

```csharp
public int Face
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_Options_Layer"></a> Layer

```csharp
public uint Layer
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_Options_LevelSampler"></a> LevelSampler

階層ごとの色の供給元(null なら全階層で <xref href="VirtualGeometry.Streaming.CellAlbedoPackBaker.Options.Sampler" data-throw-if-not-resolved="false"></xref>)。階層が浅い(粗い)ほど 1 画素が元画像の多くの画素に当たり、
1 点だけ拾うとエイリアシング(ごま塩状の点)になるので、元画像が細かいときは階層の画素の大きさに合わせて平均した値を返す供給元を渡す。

```csharp
public Func<int, DirectionColorSampler> LevelSampler
```

#### 値（Field Value）

 [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[int](https://learn.microsoft.com/dotnet/api/system.int32), [DirectionColorSampler](VirtualGeometry.Streaming.DirectionColorSampler.md)\>

### <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_Options_MaximumLevel"></a> MaximumLevel

```csharp
public int MaximumLevel
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_Options_Metadata"></a> Metadata

```csharp
public readonly Dictionary<string, string> Metadata
```

#### 値（Field Value）

 [Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_Options_Sampler"></a> Sampler

```csharp
public DirectionColorSampler Sampler
```

#### 値（Field Value）

 [DirectionColorSampler](VirtualGeometry.Streaming.DirectionColorSampler.md)

### <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_Options_Size"></a> Size

Cell を表す画素の数(1 辺)。

```csharp
public int Size
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_Options_TileSize"></a> TileSize

```csharp
public int TileSize { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

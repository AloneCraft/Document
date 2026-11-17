# <a id="VirtualGeometry_Streaming_CellHeightPackBaker"></a> Class CellHeightPackBaker

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

高さの供給元(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)を、Cell ごとの格子の高さ(<xref href="VirtualGeometry.Streaming.CellHeightGridCodec" data-throw-if-not-resolved="false"></xref>)にして pack(.otp)へ焼く。
格子点の方向は実行時の <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.GridDirections(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.Double%5b%5d%2cSystem.Double%5b%5d%2cSystem.Double%5b%5d)" data-throw-if-not-resolved="false"></xref> と同じなので、実行時に <xref href="VirtualGeometry.World.PlanetCellMeshBuilder.BuildFromHeights(VirtualGeometry.World.PlanetCellFrame%40%2cSystem.Double%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.ReadOnlySpan%7bSystem.Double%7d%2cSystem.Single%2cUnityEngine.Vector4%2cVirtualizedGeometry.VirtualGeometryPackedVertex%5b%5d%2cSystem.Int32%2cUnityEngine.Vector4%40%2cSystem.Double%40%2cSystem.Double%40)" data-throw-if-not-resolved="false"></xref> で作った
Cell は、供給元から直接作った Cell と(量子化の範囲で)一致する。階層 0〜MaximumLevel の全 Cell を、面ごとに1つの pack へ書く。
Editor にも Player にも依存しない(コマンドラインのツールからも動かせる)。

```csharp
public static class CellHeightPackBaker
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CellHeightPackBaker](VirtualGeometry.Streaming.CellHeightPackBaker.md)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_CellHeightPackBaker_BakeFace_VirtualGeometry_Streaming_CellHeightPackBaker_Options_System_IO_Stream_System_Action_System_Single__"></a> BakeFace\(Options, Stream, Action<float\>\)

面1つ分を output に書く。progress は 0〜1。

```csharp
public static PackWriteResult BakeFace(CellHeightPackBaker.Options options, Stream output, Action<float> progress = null)
```

#### 引数（Parameters）

`options` [CellHeightPackBaker](VirtualGeometry.Streaming.CellHeightPackBaker.md).[Options](VirtualGeometry.Streaming.CellHeightPackBaker.Options.md)

`output` [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)

`progress` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[float](https://learn.microsoft.com/dotnet/api/system.single)\>

#### 戻り値（Returns）

 [PackWriteResult](Omni.Streaming.Formats.PackWriteResult.md)

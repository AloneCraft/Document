# <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker"></a> Class CellAlbedoPackBaker

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

色の供給元(<xref href="VirtualGeometry.Streaming.DirectionColorSampler" data-throw-if-not-resolved="false"></xref>)を、Cell ごとの画像タイル(<xref href="Omni.Streaming.Formats.ImageTile" data-throw-if-not-resolved="false"></xref>、BC1)にして pack(.otp)へ焼く。
1 タイルは Cell を size×size の画素で表し、外周に border 画素の余白(隣の Cell の色)を持つ(全体は size + 2·border 四方で、4 の倍数)。
画素の位置は Cell の面の座標で等角に並ぶ(shader が面の UV から引く規則と同じ)。階層 0〜MaximumLevel の全 Cell を、面ごとに1つの pack へ書く。
同じ色の Cell は内容が同じなので、pack の中で1つにまとまる。

```csharp
public static class CellAlbedoPackBaker
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CellAlbedoPackBaker](VirtualGeometry.Streaming.CellAlbedoPackBaker.md)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_CellAlbedoPackBaker_BakeFace_VirtualGeometry_Streaming_CellAlbedoPackBaker_Options_System_IO_Stream_System_Action_System_Single__"></a> BakeFace\(Options, Stream, Action<float\>\)

```csharp
public static PackWriteResult BakeFace(CellAlbedoPackBaker.Options options, Stream output, Action<float> progress = null)
```

#### 引数（Parameters）

`options` [CellAlbedoPackBaker](VirtualGeometry.Streaming.CellAlbedoPackBaker.md).[Options](VirtualGeometry.Streaming.CellAlbedoPackBaker.Options.md)

`output` [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)

`progress` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[float](https://learn.microsoft.com/dotnet/api/system.single)\>

#### 戻り値（Returns）

 [PackWriteResult](Omni.Streaming.Formats.PackWriteResult.md)

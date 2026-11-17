# <a id="VirtualGeometry_Streaming_CellKeyMap"></a> Class CellKeyMap

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

VG の <xref href="VirtualGeometry.World.PlanetCellKey" data-throw-if-not-resolved="false"></xref>(96 bit の格子番号)と、ストリーミングのキー <xref href="Omni.Streaming.StreamKey" data-throw-if-not-resolved="false"></xref>(31 階層まで)の対応。

```csharp
public static class CellKeyMap
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CellKeyMap](VirtualGeometry.Streaming.CellKeyMap.md)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_CellKeyMap_ToCellKey_Omni_Streaming_StreamKey__"></a> ToCellKey\(in StreamKey\)

```csharp
public static PlanetCellKey ToCellKey(in StreamKey key)
```

#### 引数（Parameters）

`key` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 PlanetCellKey

### <a id="VirtualGeometry_Streaming_CellKeyMap_TryToStreamKey_System_UInt32_VirtualGeometry_World_PlanetCellKey__Omni_Streaming_StreamKey__"></a> TryToStreamKey\(uint, in PlanetCellKey, out StreamKey\)

階層が <xref href="Omni.Streaming.StreamKey.MaximumLevel" data-throw-if-not-resolved="false"></xref> を超える、または格子番号が 32 bit に収まらない Cell は false。

```csharp
public static bool TryToStreamKey(uint layer, in PlanetCellKey key, out StreamKey streamKey)
```

#### 引数（Parameters）

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`key` PlanetCellKey

`streamKey` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

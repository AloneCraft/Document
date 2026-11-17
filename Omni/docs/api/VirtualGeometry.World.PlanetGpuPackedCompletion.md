# <a id="VirtualGeometry_World_PlanetGpuPackedCompletion"></a> Struct PlanetGpuPackedCompletion

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

生成resultと圧縮recordを同じreadbackで返す。slot表全体は読み戻さない。

```csharp
public struct PlanetGpuPackedCompletion
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuPackedCompletion_Result"></a> Result

```csharp
public PlanetGpuGenerationResult Result
```

#### 値（Field Value）

 [PlanetGpuGenerationResult](VirtualGeometry.World.PlanetGpuGenerationResult.md)

### <a id="VirtualGeometry_World_PlanetGpuPackedCompletion_Storage"></a> Storage

```csharp
public PlanetTerrainStorageRecord Storage
```

#### 値（Field Value）

 [PlanetTerrainStorageRecord](VirtualGeometry.World.PlanetTerrainStorageRecord.md)

### <a id="VirtualGeometry_World_PlanetGpuPackedCompletion_Stride"></a> Stride

```csharp
public const int Stride = 112
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

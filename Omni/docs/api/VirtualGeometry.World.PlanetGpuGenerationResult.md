# <a id="VirtualGeometry_World_PlanetGpuGenerationResult"></a> Struct PlanetGpuGenerationResult

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Identity=(slot,version,status,poolEpoch)。HeightRange.zwはdispatchSerialの下位/上位16 bitを正確なfloat整数で返す。

```csharp
public struct PlanetGpuGenerationResult
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuGenerationResult_Bounds"></a> Bounds

```csharp
public Vector4 Bounds
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuGenerationResult_HeightRange"></a> HeightRange

```csharp
public Vector4 HeightRange
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuGenerationResult_Identity"></a> Identity

```csharp
public uint4 Identity
```

#### 値（Field Value）

 uint4

### <a id="VirtualGeometry_World_PlanetGpuGenerationResult_Stride"></a> Stride

```csharp
public const int Stride = 48
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuGenerationResult_TryGetDispatchSerial_System_UInt32__"></a> TryGetDispatchSerial\(out uint\)

```csharp
public bool TryGetDispatchSerial(out uint serial)
```

#### 引数（Parameters）

`serial` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

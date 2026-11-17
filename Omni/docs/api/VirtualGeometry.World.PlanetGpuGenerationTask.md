# <a id="VirtualGeometry_World_PlanetGpuGenerationTask"></a> Struct PlanetGpuGenerationTask

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

1 slotのGPU生成。patchの高さはbasis中心からの差、height.y/zは全高さ中心とHeightShiftとの差。

```csharp
public struct PlanetGpuGenerationTask
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuGenerationTask_FaceRange"></a> FaceRange

```csharp
public Vector4 FaceRange
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuGenerationTask_Height"></a> Height

```csharp
public Vector4 Height
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuGenerationTask_Identity"></a> Identity

```csharp
public uint4 Identity
```

#### 値（Field Value）

 uint4

### <a id="VirtualGeometry_World_PlanetGpuGenerationTask_NoiseRange"></a> NoiseRange

```csharp
public uint4 NoiseRange
```

#### 値（Field Value）

 uint4

### <a id="VirtualGeometry_World_PlanetGpuGenerationTask_PatchRanges"></a> PatchRanges

```csharp
public uint4 PatchRanges
```

#### 値（Field Value）

 uint4

### <a id="VirtualGeometry_World_PlanetGpuGenerationTask_Sphere"></a> Sphere

```csharp
public Vector4 Sphere
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuGenerationTask_Stride"></a> Stride

```csharp
public const int Stride = 96
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuGenerationTask_Create_VirtualGeometry_World_PlanetCellFrame__System_Single_System_Int32_System_Int32_System_Int32_System_Single_System_Single_System_Single_System_Int32_System_Int32_System_Int32_System_Int32_System_Int32_System_Int32_System_UInt32_System_UInt32_"></a> Create\(in PlanetCellFrame, float, int, int, int, float, float, float, int, int, int, int, int, int, uint, uint\)

nは8/16のみ。接地保護やslotの重複・寿命は呼出し側の生成batchが検査する。

```csharp
public static PlanetGpuGenerationTask Create(in PlanetCellFrame frame, float radius, int n, int slot, int version, float skirt, float geometryCenterResidual, float shadingCenterResidual, int geometryPatchBase, int geometryPatchCount, int shadingPatchBase, int shadingPatchCount, int octaveBase, int octaveCount, uint poolEpoch = 1, uint dispatchSerial = 0)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`slot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`version` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`skirt` [float](https://learn.microsoft.com/dotnet/api/system.single)

`geometryCenterResidual` [float](https://learn.microsoft.com/dotnet/api/system.single)

`shadingCenterResidual` [float](https://learn.microsoft.com/dotnet/api/system.single)

`geometryPatchBase` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`geometryPatchCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`shadingPatchBase` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`shadingPatchCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`octaveBase` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`octaveCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`poolEpoch` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`dispatchSerial` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [PlanetGpuGenerationTask](VirtualGeometry.World.PlanetGpuGenerationTask.md)

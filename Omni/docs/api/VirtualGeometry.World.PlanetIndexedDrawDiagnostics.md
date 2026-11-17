# <a id="VirtualGeometry_World_PlanetIndexedDrawDiagnostics"></a> Struct PlanetIndexedDrawDiagnostics

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

CameraのForwardへ提出した三角形数。画素被覆やGPU時間とは別の、frame付き非同期sample。

```csharp
public readonly struct PlanetIndexedDrawDiagnostics
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetIndexedDrawDiagnostics_Frame"></a> Frame

```csharp
public readonly int Frame
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetIndexedDrawDiagnostics_GridInstances"></a> GridInstances

```csharp
public readonly uint GridInstances
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualGeometry_World_PlanetIndexedDrawDiagnostics_IsValid"></a> IsValid

```csharp
public readonly bool IsValid
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetIndexedDrawDiagnostics_SelectedCells"></a> SelectedCells

```csharp
public readonly int SelectedCells
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetIndexedDrawDiagnostics_SkirtInstances"></a> SkirtInstances

```csharp
public readonly uint SkirtInstances
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetIndexedDrawDiagnostics_GridTriangles"></a> GridTriangles

```csharp
public long GridTriangles { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetIndexedDrawDiagnostics_SkirtTriangles"></a> SkirtTriangles

```csharp
public long SkirtTriangles { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetIndexedDrawDiagnostics_SubmittedTriangles"></a> SubmittedTriangles

```csharp
public long SubmittedTriangles { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

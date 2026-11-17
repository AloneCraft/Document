# <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot"></a> Class VirtualGeometrySharedSnapshot

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Immutableなindexと共有slotの所有。retire後も、全Cameraのreceipt完了まで位置を保持する。

```csharp
public sealed class VirtualGeometrySharedSnapshot : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometrySharedSnapshot](VirtualizedGeometry.VirtualGeometrySharedSnapshot.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_Generation"></a> Generation

```csharp
public long Generation { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_IndexCount"></a> IndexCount

```csharp
public int IndexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_Indices"></a> Indices

```csharp
public ReadOnlySpan<uint> Indices { get; }
```

#### 値（Property Value）

 [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[uint](https://learn.microsoft.com/dotnet/api/system.uint32)\>

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_Quarantined"></a> Quarantined

```csharp
public bool Quarantined { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_Released"></a> Released

```csharp
public bool Released { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_Retired"></a> Retired

```csharp
public bool Retired { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_VertexCount"></a> VertexCount

```csharp
public int VertexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_BeginDraw_System_Object_System_Int64_"></a> BeginDraw\(object, long\)

```csharp
public VirtualGeometrySharedDrawReceipt BeginDraw(object cameraEntityId, long submission)
```

#### 引数（Parameters）

`cameraEntityId` [object](https://learn.microsoft.com/dotnet/api/system.object)

`submission` [long](https://learn.microsoft.com/dotnet/api/system.int64)

#### 戻り値（Returns）

 [VirtualGeometrySharedDrawReceipt](VirtualizedGeometry.VirtualGeometrySharedDrawReceipt.md)

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_Lod_System_String_"></a> Lod\(string\)

```csharp
public int Lod(string pageId)
```

#### 引数（Parameters）

`pageId` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometrySharedSnapshot_TryGetTriangle_System_String_System_Int32_VirtualizedGeometry_VirtualGeometrySharedTriangle__"></a> TryGetTriangle\(string, int, out VirtualGeometrySharedTriangle\)

```csharp
public bool TryGetTriangle(string pageId, int triangle, out VirtualGeometrySharedTriangle value)
```

#### 引数（Parameters）

`pageId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`triangle` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` [VirtualGeometrySharedTriangle](VirtualizedGeometry.VirtualGeometrySharedTriangle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

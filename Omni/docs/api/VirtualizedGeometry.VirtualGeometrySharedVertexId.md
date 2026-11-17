# <a id="VirtualizedGeometry_VirtualGeometrySharedVertexId"></a> Struct VirtualGeometrySharedVertexId

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Sourceに依存しない正本位置の識別。隣接sourceは同じdomainと番号を合意して供給する。

```csharp
public readonly struct VirtualGeometrySharedVertexId : IEquatable<VirtualGeometrySharedVertexId>
```

#### 実装するインターフェース（Implements）

[IEquatable<VirtualGeometrySharedVertexId\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexId__ctor_System_Guid_System_UInt64_"></a> VirtualGeometrySharedVertexId\(Guid, ulong\)

```csharp
public VirtualGeometrySharedVertexId(Guid domain, ulong value)
```

#### 引数（Parameters）

`domain` [Guid](https://learn.microsoft.com/dotnet/api/system.guid)

`value` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexId_Domain"></a> Domain

```csharp
public readonly Guid Domain
```

#### 値（Field Value）

 [Guid](https://learn.microsoft.com/dotnet/api/system.guid)

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexId_Value"></a> Value

```csharp
public readonly ulong Value
```

#### 値（Field Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexId_Equals_VirtualizedGeometry_VirtualGeometrySharedVertexId_"></a> Equals\(VirtualGeometrySharedVertexId\)

```csharp
public bool Equals(VirtualGeometrySharedVertexId other)
```

#### 引数（Parameters）

`other` [VirtualGeometrySharedVertexId](VirtualizedGeometry.VirtualGeometrySharedVertexId.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexId_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometrySharedVertexId_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

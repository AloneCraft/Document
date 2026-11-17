# <a id="VirtualizedGeometry_VirtualGeometryPageFeedback"></a> Struct VirtualGeometryPageFeedback

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

選択がstreamingへ返すpage単位のfeedback。Missingは不足pageの要求、それ以外は利用中pageの保持。

```csharp
public readonly struct VirtualGeometryPageFeedback
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryPageFeedback__ctor_System_UInt32_System_Single_System_Boolean_"></a> VirtualGeometryPageFeedback\(uint, float, bool\)

```csharp
public VirtualGeometryPageFeedback(uint pageId, float priority, bool missing)
```

#### 引数（Parameters）

`pageId` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`missing` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryPageFeedback_Missing"></a> Missing

```csharp
public bool Missing { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryPageFeedback_PageId"></a> PageId

```csharp
public uint PageId { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="VirtualizedGeometry_VirtualGeometryPageFeedback_Priority"></a> Priority

```csharp
public float Priority { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

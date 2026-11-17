# <a id="VirtualizedGeometry_VirtualGeometryRenderDecision"></a> Struct VirtualGeometryRenderDecision

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

カメラ毎のfallback判断。専用geometryと通常Proxyの可視描画を排他的にする。

```csharp
public readonly struct VirtualGeometryRenderDecision
```

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryRenderDecision_Reason"></a> Reason

```csharp
public readonly string Reason
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryRenderDecision_UseVirtual"></a> UseVirtual

```csharp
public readonly bool UseVirtual
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryRenderDecision_UseProxy"></a> UseProxy

```csharp
public bool UseProxy { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryRenderDecision_Resolve_System_String_System_Boolean_System_Boolean_System_Boolean_"></a> Resolve\(string, bool, bool, bool\)

```csharp
public static VirtualGeometryRenderDecision Resolve(string unsupportedReason, bool rootReady, bool forceFallback, bool rejected)
```

#### 引数（Parameters）

`unsupportedReason` [string](https://learn.microsoft.com/dotnet/api/system.string)

`rootReady` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`forceFallback` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`rejected` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [VirtualGeometryRenderDecision](VirtualizedGeometry.VirtualGeometryRenderDecision.md)

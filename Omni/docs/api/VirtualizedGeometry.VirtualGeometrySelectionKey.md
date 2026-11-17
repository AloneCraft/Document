# <a id="VirtualizedGeometry_VirtualGeometrySelectionKey"></a> Struct VirtualGeometrySelectionKey

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

同じgeometryを共有しても、instanceとcameraの選択履歴は別keyで保持する。

```csharp
public readonly struct VirtualGeometrySelectionKey : IEquatable<VirtualGeometrySelectionKey>
```

#### 実装するインターフェース（Implements）

[IEquatable<VirtualGeometrySelectionKey\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometrySelectionKey__ctor_System_Int32_System_Int32_"></a> VirtualGeometrySelectionKey\(int, int\)

```csharp
public VirtualGeometrySelectionKey(int instance, int camera)
```

#### 引数（Parameters）

`instance` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`camera` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometrySelectionKey_Camera"></a> Camera

```csharp
public readonly int Camera
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometrySelectionKey_Instance"></a> Instance

```csharp
public readonly int Instance
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometrySelectionKey_Equals_VirtualizedGeometry_VirtualGeometrySelectionKey_"></a> Equals\(VirtualGeometrySelectionKey\)

```csharp
public bool Equals(VirtualGeometrySelectionKey other)
```

#### 引数（Parameters）

`other` [VirtualGeometrySelectionKey](VirtualizedGeometry.VirtualGeometrySelectionKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometrySelectionKey_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object value)
```

#### 引数（Parameters）

`value` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometrySelectionKey_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

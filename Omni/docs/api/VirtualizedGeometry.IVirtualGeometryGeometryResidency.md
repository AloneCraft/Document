# <a id="VirtualizedGeometry_IVirtualGeometryGeometryResidency"></a> Interface IVirtualGeometryGeometryResidency

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

選択とpage常駐の境界。実装は通常meshと同じStreamingControllerを使用する。

```csharp
public interface IVirtualGeometryGeometryResidency
```

## メソッド（Methods）

### <a id="VirtualizedGeometry_IVirtualGeometryGeometryResidency_IsReady_System_Int32_"></a> IsReady\(int\)

```csharp
bool IsReady(int id)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_IVirtualGeometryGeometryResidency_Request_System_Int32_System_Single_"></a> Request\(int, float\)

```csharp
void Request(int id, float priority)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_IVirtualGeometryGeometryResidency_Touch_System_Int32_System_Single_"></a> Touch\(int, float\)

```csharp
void Touch(int id, float priority)
```

#### 引数（Parameters）

`id` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

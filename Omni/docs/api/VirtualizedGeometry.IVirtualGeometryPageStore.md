# <a id="VirtualizedGeometry_IVirtualGeometryPageStore"></a> Interface IVirtualGeometryPageStore

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

```csharp
public interface IVirtualGeometryPageStore
```

## メソッド（Methods）

### <a id="VirtualizedGeometry_IVirtualGeometryPageStore_ReadAsync_System_Int32_System_Threading_CancellationToken_"></a> ReadAsync\(int, CancellationToken\)

```csharp
Task<VirtualGeometryPagePayload> ReadAsync(int page, CancellationToken token)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`token` [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)

#### 戻り値（Returns）

 [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task\-1)<[VirtualGeometryPagePayload](VirtualizedGeometry.VirtualGeometryPagePayload.md)\>

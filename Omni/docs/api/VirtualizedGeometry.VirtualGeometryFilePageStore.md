# <a id="VirtualizedGeometry_VirtualGeometryFilePageStore"></a> Class VirtualGeometryFilePageStore

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

指定offset/sizeだけを非同期FileStreamで読む。遅延注入は検証用。

```csharp
public sealed class VirtualGeometryFilePageStore : IVirtualGeometryPageStore
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryFilePageStore](VirtualizedGeometry.VirtualGeometryFilePageStore.md)

#### 実装するインターフェース（Implements）

[IVirtualGeometryPageStore](VirtualizedGeometry.IVirtualGeometryPageStore.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryFilePageStore__ctor_System_String_VirtualizedGeometry_VirtualGeometryStreamMetadata_System_Int32_"></a> VirtualGeometryFilePageStore\(string, VirtualGeometryStreamMetadata, int\)

```csharp
public VirtualGeometryFilePageStore(string path, VirtualGeometryStreamMetadata metadata, int delayMilliseconds = 0)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

`metadata` [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

`delayMilliseconds` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryFilePageStore_BytesRead"></a> BytesRead

```csharp
public long BytesRead { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryFilePageStore_ReadAsync_System_Int32_System_Threading_CancellationToken_"></a> ReadAsync\(int, CancellationToken\)

```csharp
public Task<VirtualGeometryPagePayload> ReadAsync(int page, CancellationToken token)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`token` [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)

#### 戻り値（Returns）

 [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task\-1)<[VirtualGeometryPagePayload](VirtualizedGeometry.VirtualGeometryPagePayload.md)\>

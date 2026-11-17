# <a id="VirtualizedGeometry_VirtualGeometryWebPageStore"></a> Class VirtualGeometryWebPageStore

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

WebGL では File を使えない(StreamingAssets は URL)。page archive を HTTP の Range 要求で、必要な page の範囲だけ取る。
サーバーが Range を無視して全体(200)を返す場合は、返ってきた全体から範囲を切り出す。

```csharp
public sealed class VirtualGeometryWebPageStore : IVirtualGeometryPageStore
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryWebPageStore](VirtualizedGeometry.VirtualGeometryWebPageStore.md)

#### 実装するインターフェース（Implements）

[IVirtualGeometryPageStore](VirtualizedGeometry.IVirtualGeometryPageStore.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryWebPageStore__ctor_System_String_VirtualizedGeometry_VirtualGeometryStreamMetadata_"></a> VirtualGeometryWebPageStore\(string, VirtualGeometryStreamMetadata\)

```csharp
public VirtualGeometryWebPageStore(string url, VirtualGeometryStreamMetadata metadata)
```

#### 引数（Parameters）

`url` [string](https://learn.microsoft.com/dotnet/api/system.string)

`metadata` [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryWebPageStore_BytesRead"></a> BytesRead

```csharp
public long BytesRead { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryWebPageStore_ReadAsync_System_Int32_System_Threading_CancellationToken_"></a> ReadAsync\(int, CancellationToken\)

```csharp
public Task<VirtualGeometryPagePayload> ReadAsync(int page, CancellationToken token)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`token` [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)

#### 戻り値（Returns）

 [Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task\-1)<[VirtualGeometryPagePayload](VirtualizedGeometry.VirtualGeometryPagePayload.md)\>

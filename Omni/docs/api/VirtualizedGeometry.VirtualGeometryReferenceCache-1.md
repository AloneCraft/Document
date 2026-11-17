# <a id="VirtualizedGeometry_VirtualGeometryReferenceCache_1"></a> Class VirtualGeometryReferenceCache<T\>

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

共有GPU資源の所有権を参照数とentry世代で管理し、reset後の古いleaseを無効化する。

```csharp
public sealed class VirtualGeometryReferenceCache<T> : IDisposable where T : class, IDisposable
```

#### 型引数（Type Parameters）

`T` 

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryReferenceCache<T\>](VirtualizedGeometry.VirtualGeometryReferenceCache\-1.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryReferenceCache_1_ResourceCount"></a> ResourceCount

```csharp
public int ResourceCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryReferenceCache_1_Acquire_System_String_System_Func__0__"></a> Acquire\(string, Func<T\>\)

```csharp
public VirtualGeometryReferenceCache<T>.Lease Acquire(string key, Func<T> factory)
```

#### 引数（Parameters）

`key` [string](https://learn.microsoft.com/dotnet/api/system.string)

`factory` [Func](https://learn.microsoft.com/dotnet/api/system.func\-1)<T\>

#### 戻り値（Returns）

 [VirtualGeometryReferenceCache](VirtualizedGeometry.VirtualGeometryReferenceCache\-1.md)<T\>.[Lease](VirtualizedGeometry.VirtualGeometryReferenceCache\-1.Lease.md)

### <a id="VirtualizedGeometry_VirtualGeometryReferenceCache_1_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualizedGeometry_VirtualGeometryReferenceCache_1_Reset"></a> Reset\(\)

```csharp
public void Reset()
```

# <a id="Omni_Streaming_ArrayBufferPool"></a> Class ArrayBufferPool

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

byte[] の既定のプール。2 の冪の大きさごとに返却を溜め、溜める総量に上限を持つ。

```csharp
public sealed class ArrayBufferPool : BufferPool
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[BufferPool](Omni.Streaming.BufferPool.md) ← 
[ArrayBufferPool](Omni.Streaming.ArrayBufferPool.md)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_ArrayBufferPool__ctor_System_Int64_"></a> ArrayBufferPool\(long\)

```csharp
public ArrayBufferPool(long retainLimitBytes = 67108864)
```

#### 引数（Parameters）

`retainLimitBytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

## プロパティ（Properties）

### <a id="Omni_Streaming_ArrayBufferPool_RetainedBytes"></a> RetainedBytes

```csharp
public long RetainedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_Streaming_ArrayBufferPool_Rent_System_Int32_"></a> Rent\(int\)

length byte 以上を指す Memory を持つバッファ(Length は length ちょうど)。参照は 1。

```csharp
public override PooledBuffer Rent(int length)
```

#### 引数（Parameters）

`length` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PooledBuffer](Omni.Streaming.PooledBuffer.md)

### <a id="Omni_Streaming_ArrayBufferPool_SizeClass_System_Int32_"></a> SizeClass\(int\)

```csharp
public static int SizeClass(int length)
```

#### 引数（Parameters）

`length` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

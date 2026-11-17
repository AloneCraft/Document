# <a id="Omni_Streaming_PooledBuffer"></a> Class PooledBuffer

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

参照カウントつきのバイト列。所有者(取得元・ストア・利用者)が <xref href="Omni.Streaming.PooledBuffer.Retain" data-throw-if-not-resolved="false"></xref>/<xref href="Omni.Streaming.PooledBuffer.Release" data-throw-if-not-resolved="false"></xref> で寿命を共有する。
参照が 0 になると <xref href="Omni.Streaming.PooledBuffer.OnReleased" data-throw-if-not-resolved="false"></xref> が呼ばれ、プールへ戻る(または解放される)。0 になった後は使えない。
派生クラスは Memory の実体(byte[]、NativeArray など)を決める。

```csharp
public abstract class PooledBuffer
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PooledBuffer](Omni.Streaming.PooledBuffer.md)

## プロパティ（Properties）

### <a id="Omni_Streaming_PooledBuffer_Length"></a> Length

```csharp
public int Length { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_PooledBuffer_Memory"></a> Memory

```csharp
public abstract Memory<byte> Memory { get; }
```

#### 値（Property Value）

 [Memory](https://learn.microsoft.com/dotnet/api/system.memory\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

### <a id="Omni_Streaming_PooledBuffer_ReadOnlyMemory"></a> ReadOnlyMemory

```csharp
public ReadOnlyMemory<byte> ReadOnlyMemory { get; }
```

#### 値（Property Value）

 [ReadOnlyMemory](https://learn.microsoft.com/dotnet/api/system.readonlymemory\-1)<[byte](https://learn.microsoft.com/dotnet/api/system.byte)\>

### <a id="Omni_Streaming_PooledBuffer_ReferenceCount"></a> ReferenceCount

```csharp
public int ReferenceCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Streaming_PooledBuffer_OnReleased"></a> OnReleased\(\)

```csharp
protected abstract void OnReleased()
```

### <a id="Omni_Streaming_PooledBuffer_Release"></a> Release\(\)

```csharp
public void Release()
```

### <a id="Omni_Streaming_PooledBuffer_Retain"></a> Retain\(\)

```csharp
public PooledBuffer Retain()
```

#### 戻り値（Returns）

 [PooledBuffer](Omni.Streaming.PooledBuffer.md)

### <a id="Omni_Streaming_PooledBuffer_Slice_System_Int32_System_Int32_"></a> Slice\(int, int\)

[offset, offset+length) を指す、同じ寿命を共有する view(親を保持する)。コピーしない。

```csharp
public PooledBuffer Slice(int offset, int length)
```

#### 引数（Parameters）

`offset` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`length` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PooledBuffer](Omni.Streaming.PooledBuffer.md)

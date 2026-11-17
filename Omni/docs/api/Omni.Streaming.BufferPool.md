# <a id="Omni_Streaming_BufferPool"></a> Class BufferPool

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

バイト列の借り出し先。実装は借りたバッファの <xref href="Omni.Streaming.PooledBuffer.Release" data-throw-if-not-resolved="false"></xref> で戻る先を決める。

```csharp
public abstract class BufferPool
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[BufferPool](Omni.Streaming.BufferPool.md)

#### 派生した型（Derived）

[ArrayBufferPool](Omni.Streaming.ArrayBufferPool.md)

## メソッド（Methods）

### <a id="Omni_Streaming_BufferPool_Rent_System_Int32_"></a> Rent\(int\)

length byte 以上を指す Memory を持つバッファ(Length は length ちょうど)。参照は 1。

```csharp
public abstract PooledBuffer Rent(int length)
```

#### 引数（Parameters）

`length` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PooledBuffer](Omni.Streaming.PooledBuffer.md)

# <a id="Omni_Streaming_IDecodedPayload"></a> Interface IDecodedPayload

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

展開済みの中身。<xref href="System.IDisposable.Dispose" data-throw-if-not-resolved="false"></xref> は、host が追い出したとき、かつ利用者の lease が全部戻ったときに1回だけ呼ぶ。

```csharp
public interface IDecodedPayload : IDisposable
```

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## プロパティ（Properties）

### <a id="Omni_Streaming_IDecodedPayload_ByteSize"></a> ByteSize

```csharp
long ByteSize { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

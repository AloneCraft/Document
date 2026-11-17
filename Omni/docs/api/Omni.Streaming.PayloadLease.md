# <a id="Omni_Streaming_PayloadLease"></a> Class PayloadLease

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

利用者が展開済みの中身を使っている間、host に追い出されないための参照。使い終わったら Dispose する(2回呼んでも1回分)。

```csharp
public sealed class PayloadLease : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PayloadLease](Omni.Streaming.PayloadLease.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## プロパティ（Properties）

### <a id="Omni_Streaming_PayloadLease_Key"></a> Key

```csharp
public StreamKey Key { get; }
```

#### 値（Property Value）

 [StreamKey](Omni.Streaming.StreamKey.md)

### <a id="Omni_Streaming_PayloadLease_Payload"></a> Payload

Dispose の後は null。

```csharp
public IDecodedPayload Payload { get; }
```

#### 値（Property Value）

 [IDecodedPayload](Omni.Streaming.IDecodedPayload.md)

## メソッド（Methods）

### <a id="Omni_Streaming_PayloadLease_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

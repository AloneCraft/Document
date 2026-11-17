# <a id="Omni_Streaming_IInterestObserver"></a> Interface IInterestObserver

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

取得元が、host の関心(いま欲しいキー)の変化を知りたいときに実装する(サーバーが送り込む型の取得元)。
受け取った中身は <xref href="Omni.Streaming.StreamingHost.DeliverContent(Omni.Streaming.ContentId%40%2cOmni.Streaming.PooledBuffer)" data-throw-if-not-resolved="false"></xref> で渡す。host の Tick の中から呼ばれる。

```csharp
public interface IInterestObserver
```

## メソッド（Methods）

### <a id="Omni_Streaming_IInterestObserver_InterestChanged_System_Collections_Generic_IReadOnlyCollection_Omni_Streaming_StreamKey__"></a> InterestChanged\(IReadOnlyCollection<StreamKey\>\)

```csharp
void InterestChanged(IReadOnlyCollection<StreamKey> wanted)
```

#### 引数（Parameters）

`wanted` [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection\-1)<[StreamKey](Omni.Streaming.StreamKey.md)\>

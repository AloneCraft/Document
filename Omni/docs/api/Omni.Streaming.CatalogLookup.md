# <a id="Omni_Streaming_CatalogLookup"></a> Enum CatalogLookup

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

```csharp
public enum CatalogLookup
```

## フィールド（Fields）

`Absent = 1` 

存在の表で「無い」。



`Found = 0` 

entry が有効。



`Pending = 2` 

答えに必要な目録をまだ読んでいる。後で問い合わせ直す。



`Unavailable = 3` 

答えられない(目録を読めなかった)。

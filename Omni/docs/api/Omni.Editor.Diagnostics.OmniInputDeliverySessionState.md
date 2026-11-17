# <a id="Omni_Editor_Diagnostics_OmniInputDeliverySessionState"></a> Enum OmniInputDeliverySessionState

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

入力到達ログのセッションの状態です。

```csharp
public enum OmniInputDeliverySessionState
```

## フィールド（Fields）

`Active = 1` 

要求したセッションが有効です。



`Expired = 3` 

寿命の上限で終わりました。



`Inactive = 0` 

セッションがありません（または要求したセッションを知りません）。



`Interrupted = 2` 

assembly の再読み込みで終わりました。



`Mismatch = 4` 

別のセッションが有効で、要求したセッションと一致しません。

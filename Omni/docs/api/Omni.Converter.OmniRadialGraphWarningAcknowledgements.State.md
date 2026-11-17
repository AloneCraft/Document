# <a id="Omni_Converter_OmniRadialGraphWarningAcknowledgements_State"></a> Enum OmniRadialGraphWarningAcknowledgements.State

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Graph の確認済みの状態です。

```csharp
public enum OmniRadialGraphWarningAcknowledgements.State
```

## フィールド（Fields）

`Acknowledged = 1` 

記録があり、今の内容と指紋が合う（警告を止める）。



`Changed = 2` 

記録はあるが、記録の後に Graph が変わった（警告が戻る）。



`None = 0` 

記録が無い。

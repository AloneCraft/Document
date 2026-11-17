# <a id="Omni_Converter_OmniCustomShaderConversionConfirmations_State"></a> Enum OmniCustomShaderConversionConfirmations.State

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

確認済みの状態です。

```csharp
public enum OmniCustomShaderConversionConfirmations.State
```

## フィールド（Fields）

`Changed = 2` 

記録はあるが、記録の後に元・出力・判定の版が変わった（青へ戻る）。



`Confirmed = 1` 

記録があり、今の元と出力の指紋が合う（緑）。



`None = 0` 

確認の記録が無い。

# <a id="Omni_Editor_Diagnostics_OmniObservationOutcome"></a> Enum OmniObservationOutcome

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

撮影・テスト・計測などの観測の結果です。値は外部ランナーの終了コードと一致します。

```csharp
public enum OmniObservationOutcome
```

## フィールド（Fields）

`Failed = 1` 

観測が有効で、検査が不合格でした。製品の不具合の証拠になり得ます。



`Passed = 0` 

観測が有効で、検査が合格しました。



`Unavailable = 2` 

観測そのものが無効でした。合格でも不合格でもない非成功です。

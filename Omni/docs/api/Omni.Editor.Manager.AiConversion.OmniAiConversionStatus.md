# <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStatus"></a> Enum OmniAiConversionStatus

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

自作 Shader 1 本の「AI 変換依頼」の状態です。Shaders タブのアイコンと詳細欄の見出しになります。

```csharp
public enum OmniAiConversionStatus
```

## フィールド（Fields）

`AiFailedAgain = 4` 

AI が元を直した後の判定も失敗した（n 回目）。



`AiNotApplicable = 3` 

AI 判定: 対応不可。AI が「書き換えない」と答え、元は依頼のときのまま。



`AiPending = 2` 

AI 依頼中。依頼の後に元がまだ変わっておらず、AI の結果（対応不可）も来ていない。



`Confirmed = 6` 

機械判定が成功し、利用者が確認済みにした内容と一致している。



`ConvertedUnconfirmed = 5` 

機械判定は成功したが、利用者がまだ「確認済み」にしていない（または確認の後に内容が変わった）。



`None = 0` 

判定結果も依頼も無い（まだ判定していない、または判定が今の内容に対するものではない）。



`Unconvertible = 1` 

変換不能。依頼が無く、機械判定が失敗している。

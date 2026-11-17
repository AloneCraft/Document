# <a id="Omni_Editor_Manager_RadialBakeStaleReason"></a> Enum RadialBakeStaleReason

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

<xref href="Omni.Editor.Manager.RadialBaker.IsBakeStale(UnityEngine.SceneManagement.Scene%2cOmni.RadialCamera%2cOmni.Editor.Manager.RadialBakeStaleReason%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>が返す陳腐化理由の分類です。
表示文言（多言語対応）とは切り離し、呼び出し側が文字列内容に依存せず分岐できるようにします。

```csharp
public enum RadialBakeStaleReason
```

## フィールド（Fields）

`BindingCountMismatch = 4` 

RadialBakeBinding とベイクデータの件数が一致しません。



`ContentChanged = 3` 

ベイク後にシーンの内容が変更されています。



`MissingBakeData = 1` 

ベイクデータが存在しません。



`MissingRendererReference = 5` 

RadialBakeBinding に Renderer 参照の欠落があります。



`None = 0` 

陳腐化していません。



`SchemaMismatch = 6` 

schema v2または決定的BVHの整合性が失われています。



`SettingsMismatch = 2` 

現在の RadialCamera 設定とベイク時の設定が一致しません。

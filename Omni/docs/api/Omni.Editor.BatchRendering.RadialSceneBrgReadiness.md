# <a id="Omni_Editor_BatchRendering_RadialSceneBrgReadiness"></a> Enum RadialSceneBrgReadiness

Namespace: [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)  
Assembly: Omni.Editor.dll  

ロード済みSceneのBRG描画準備を利用者へ示す分類です。

```csharp
public enum RadialSceneBrgReadiness
```

## フィールド（Fields）

`Failed = 4` 

直近の準備が失敗しています。Scene BRGは準備が成功するまで再構築・Rendererの引き継ぎ・
常駐データ更新を止めます（Fail Closed）。以前に準備済みの常駐描画は残り得ます。



`NotChecked = 1` 

このEditorセッションではまだ準備結果がありません。



`NotRequiredLegacy = 0` 

Legacy backendなので、描画にsidecarを必要としません。



`Preparing = 2` 

準備を予約済み、または実行中です。



`Ready = 3` 

直近の準備が成功しました。

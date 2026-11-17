# <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationTrigger"></a> Enum RadialSceneBrgPreparationTrigger

Namespace: [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)  
Assembly: Omni.Editor.dll  

準備を開始した契機です。

```csharp
public enum RadialSceneBrgPreparationTrigger
```

## フィールド（Fields）

`Automatic = 0` 

Scene・Asset・Undo等の通知から集約した自動準備です。



`Automation = 3` 

外部検証コマンドからの同期準備です。



`BuildScenes = 2` 

Build Settingsの有効Sceneを含む全体生成です。



`Manual = 1` 

Omni Managerからの明示的な再確認・再生成です。



`PlayMode = 4` 

Play開始直前の準備です。

# <a id="Omni_Editor_Manager_AiConversion_OmniAiRestoreChange"></a> Enum OmniAiRestoreChange

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

退避との比較の種類。

```csharp
public enum OmniAiRestoreChange
```

## フィールド（Fields）

`Created = 2` 

退避のときには無かったファイルが、今は有る（AI が作った。戻すと Unity のごみ箱へ移す）。



`Deleted = 3` 

退避のときにあったファイルが、今は無い（戻すと書き戻す）。



`Modified = 1` 

退避のときにあったファイルが、今は内容が違う（戻すと上書きする）。



`Unchanged = 0` 

今のファイルは退避と同じ（戻すことは無い）。

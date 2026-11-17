# <a id="Omni_Editor_Manager_TerrainShaderClosureStatus"></a> Enum TerrainShaderClosureStatus

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

Terrain Shader 依存閉包の失敗理由です。

```csharp
public enum TerrainShaderClosureStatus
```

## フィールド（Fields）

`ImportFailed = 5` 

公開済み Shader を Unity が読み込めませんでした。



`MissingDependency = 2` 

URP の必要ソースまたは参照が見つかりません。



`NotGenerated = 0` 

まだ生成されていません。



`PatchFailed = 3` 

ShaderLab 変換または必須頂点フックの検証に失敗しました。



`PublishFailed = 4` 

ステージ済みファイルを公開できませんでした。



`Ready = 1` 

全依存が生成済みです。



`UnsupportedMaterial = 6` 

TerrainLit 以外の Material を置換対象にしようとしました。

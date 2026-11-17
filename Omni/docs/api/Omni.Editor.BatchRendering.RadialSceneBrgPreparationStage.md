# <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationStage"></a> Enum RadialSceneBrgPreparationStage

Namespace: [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)  
Assembly: Omni.Editor.dll  

Scene BRG sidecar準備が止まった段階です。

```csharp
public enum RadialSceneBrgPreparationStage
```

## フィールド（Fields）

`CollectMaterials = 1` 

ロード済みSceneまたはBuild対象SceneのMaterial収集です。



`ConvertBrgShader = 6` 

Radial ShaderからBRG専用Shader本文を作る変換です。



`FinalizeManifest = 9` 

保存後の依存Hash確定とManifest更新です。



`ImportBrgShader = 7` 

生成したBRG ShaderのImportです。



`LoadManifest = 2` 

生成先フォルダーとEditor用Manifestの読込み・作成です。



`None = 0` 

失敗していません。



`PrepareRadialMaterial = 4` 

BRGより先に必要なRadial基礎Shaderの検証・生成です（Radial Materialの写しは作りません）。
段階の名前は、Omni Managerの表示とテストが参照するので変えていません。



`RenderObjectsCompatibility = 10` 

URP Render Objects overrideとScene BRGの互換性検査です。



`ResolveAuthoringMaterial = 3` 

Renderer上のMaterialを永続Authoring Materialへ戻す段階です。



`ResolveBrgShader = 5` 

sidecarの元になるRadial Shaderの解決です。



`WriteSidecar = 8` 

sidecar Materialの作成・更新です。

# <a id="Omni_Editor_BatchRendering_OmniLightProbeSpaceAuthoring"></a> Class OmniLightProbeSpaceAuthoring

Namespace: [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)  
Assembly: Omni.Editor.dll  

表示RootへLight Probe空間の明示契約を一貫して構成するEditor authoring境界です。
自動保存やBRG rebuildの直接要求は行わず、Space自身の変更通知へ委ねます。

```csharp
public static class OmniLightProbeSpaceAuthoring
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniLightProbeSpaceAuthoring](Omni.Editor.BatchRendering.OmniLightProbeSpaceAuthoring.md)

## メソッド（Methods）

### <a id="Omni_Editor_BatchRendering_OmniLightProbeSpaceAuthoring_TryEnsureContract_UnityEngine_GameObject_UnityEngine_Transform_System_Boolean_System_Boolean__System_String__"></a> TryEnsureContract\(GameObject, Transform, bool, out bool, out string\)

RequirementとSpaceを同じGameObjectへ配置し、baked rootを同期します。

```csharp
public static bool TryEnsureContract(GameObject displayRoot, Transform expectedBakedSpaceRoot, bool recordUndo, out bool changed, out string reason)
```

#### 引数（Parameters）

`displayRoot` GameObject

物理ベイク空間と表示空間を対応付けるRootです。

`expectedBakedSpaceRoot` Transform

Probeを焼いた空間のRootです。Unityワールド原点で焼いた場合はnullです。

`recordUndo` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

確認付きEditor操作ではtrue、生成器ではfalseです。

`changed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Sceneへ保存すべき変更を行った場合にtrueです。

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

失敗理由です。成功時は空文字列です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

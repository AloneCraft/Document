# <a id="Omni_Editor_Manager_OmniRegenerateAll"></a> Class OmniRegenerateAll

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

プロジェクト全体（Assets/ 配下の全シーン・全マテリアル）を対象に、
Omni ラッパーシェーダー／マテリアルを再生成します。
RadialInject.hlsl の CBUFFER 配置修正など、生成テンプレート側の変更を
既存の生成済みアセットへ反映するために使います。

```csharp
public static class OmniRegenerateAll
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRegenerateAll](Omni.Editor.Manager.OmniRegenerateAll.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniRegenerateAll_Run"></a> Run\(\)

```csharp
public static void Run()
```

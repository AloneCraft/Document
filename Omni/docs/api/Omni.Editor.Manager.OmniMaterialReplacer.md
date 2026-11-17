# <a id="Omni_Editor_Manager_OmniMaterialReplacer"></a> Class OmniMaterialReplacer

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

シーン内MaterialのShader切替・復元を管理します。<xref href="Omni.Converter.RadialMaterialApplier" data-throw-if-not-resolved="false"></xref> のラッパーです。

```csharp
public static class OmniMaterialReplacer
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniMaterialReplacer](Omni.Editor.Manager.OmniMaterialReplacer.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniMaterialReplacer_ApplyToScene"></a> ApplyToScene\(\)

現在のシーンの永続Material参照を保ったままShaderをOmni版へ切り替えます。

```csharp
public static (int renderers, int terrains) ApplyToScene()
```

#### 戻り値（Returns）

 \([int](https://learn.microsoft.com/dotnet/api/system.int32) [renderers](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.int32,system.int32\-.renderers), [int](https://learn.microsoft.com/dotnet/api/system.int32) [terrains](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.int32,system.int32\-.terrains)\)

### <a id="Omni_Editor_Manager_OmniMaterialReplacer_EnsureRadialCameraOnMain"></a> EnsureRadialCameraOnMain\(\)

MainCamera に RadialCamera が付いていることを確認します。

```csharp
public static void EnsureRadialCameraOnMain()
```

### <a id="Omni_Editor_Manager_OmniMaterialReplacer_ForceRevert"></a> ForceRevert\(\)

シーン内の Omni マテリアルを元に戻します。

<p>
根拠はマニフェストの逆引き（GUID + localId）なので、ドメインリロードや
Editor 再起動を跨いでも、別の誰かが適用したシーンでも戻せます。
解決できなかったスロットは必ず警告として報告されます。
</p>

```csharp
public static (int, int) ForceRevert()
```

#### 戻り値（Returns）

 \([int](https://learn.microsoft.com/dotnet/api/system.int32), [int](https://learn.microsoft.com/dotnet/api/system.int32)\)

### <a id="Omni_Editor_Manager_OmniMaterialReplacer_SaveSceneIfUserWantsTo"></a> SaveSceneIfUserWantsTo\(\)

シーン保存を促し、ユーザーがキャンセルしたら false を返します。

```csharp
public static bool SaveSceneIfUserWantsTo()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_OmniMaterialReplacer_Validate"></a> Validate\(\)

シーンの検証レポートを返します。

```csharp
public static string Validate()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

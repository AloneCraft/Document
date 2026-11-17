# <a id="Omni_Editor_Build_OmniDotsRadialGuard_IMaterialOwner"></a> Interface OmniDotsRadialGuard.IMaterialOwner

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

実行時にコードでEntityを作る所有者です。対数の切替の対象にするMaterialを報告し、切替後の作り直しを受けます。

```csharp
public interface OmniDotsRadialGuard.IMaterialOwner
```

## メソッド（Methods）

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_IMaterialOwner_CountRadialPositionedEntities"></a> CountRadialPositionedEntities\(\)

この所有者が対数の位置情報を書いているEntity Graphics描画Entityの数です。

```csharp
int CountRadialPositionedEntities()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_IMaterialOwner_EnumerateMaterials"></a> EnumerateMaterials\(\)

この所有者が使う永続Materialです。

```csharp
IEnumerable<Material> EnumerateMaterials()
```

#### 戻り値（Returns）

 [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Material\>

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_IMaterialOwner_OnMaterialsSwitched"></a> OnMaterialsSwitched\(\)

切替でMaterialのShaderが変わった後、描画を作り直します。

```csharp
void OnMaterialsSwitched()
```

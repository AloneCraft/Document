# <a id="Omni_Converter_IOmniExternalMaterialSource"></a> Interface IOmniExternalMaterialSource

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

ロード済みSceneのRenderer・Terrain・Decal Projectorからは見えない永続Materialを供給します。
閉じたSubSceneの依存Materialや、実行時にコードでEntityを作る所有者のMaterialが当たります。
供給元は<code>Register</code>で登録します（Converterは供給元のassemblyを参照しません）。

```csharp
public interface IOmniExternalMaterialSource
```

## メソッド（Methods）

### <a id="Omni_Converter_IOmniExternalMaterialSource_EnumerateMaterials"></a> EnumerateMaterials\(\)

切替の対象にする永続Materialを返します（nullや重複は呼び出し側が除きます）。

```csharp
IEnumerable<Material> EnumerateMaterials()
```

#### 戻り値（Returns）

 [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Material\>

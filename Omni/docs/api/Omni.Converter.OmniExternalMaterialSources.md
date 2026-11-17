# <a id="Omni_Converter_OmniExternalMaterialSources"></a> Class OmniExternalMaterialSources

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

外部Material供給元の登録簿です。

```csharp
public static class OmniExternalMaterialSources
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniExternalMaterialSources](Omni.Converter.OmniExternalMaterialSources.md)

## メソッド（Methods）

### <a id="Omni_Converter_OmniExternalMaterialSources_Enumerate"></a> Enumerate\(\)

登録された供給元の永続Materialを、重複なく返します。

```csharp
public static List<Material> Enumerate()
```

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<Material\>

### <a id="Omni_Converter_OmniExternalMaterialSources_Register_Omni_Converter_IOmniExternalMaterialSource_"></a> Register\(IOmniExternalMaterialSource\)

供給元を登録し、解除用のハンドルを返します。

```csharp
public static IDisposable Register(IOmniExternalMaterialSource source)
```

#### 引数（Parameters）

`source` [IOmniExternalMaterialSource](Omni.Converter.IOmniExternalMaterialSource.md)

#### 戻り値（Returns）

 [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

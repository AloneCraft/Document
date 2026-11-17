# <a id="Omni_Converter_Guarantees_OmniTemplateSets"></a> Class OmniTemplateSets

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

Shader Graph と VFX の変換器が読む、パッケージの雛形の組です。
生成器の C# は重いので含めません（必要になったら IncludeGeneratorSources として足す拡張点です）。

```csharp
public static class OmniTemplateSets
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniTemplateSets](Omni.Converter.Guarantees.OmniTemplateSets.md)

## フィールド（Fields）

### <a id="Omni_Converter_Guarantees_OmniTemplateSets_ShaderGraph17_6"></a> ShaderGraph17\_6

```csharp
public const string ShaderGraph17_6 = "sg-17_6"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniTemplateSets_Vfx17_6"></a> Vfx17\_6

```csharp
public const string Vfx17_6 = "vfx-17_6"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniTemplateSets_TryGetDefinition_System_String_System_Collections_Generic_IReadOnlyList_System_String___System_Collections_Generic_IReadOnlyList_System_String___"></a> TryGetDefinition\(string, out IReadOnlyList<string\>, out IReadOnlyList<string\>\)

```csharp
public static bool TryGetDefinition(string id, out IReadOnlyList<string> roots, out IReadOnlyList<string> extensions)
```

#### 引数（Parameters）

`id` [string](https://learn.microsoft.com/dotnet/api/system.string)

`roots` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`extensions` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

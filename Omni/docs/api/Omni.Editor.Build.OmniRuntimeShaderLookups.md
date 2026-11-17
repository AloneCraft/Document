# <a id="Omni_Editor_Build_OmniRuntimeShaderLookups"></a> Class OmniRuntimeShaderLookups

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

読み込み済みのアセンブリが <xref href="Omni.OmniRuntimeShaderLookupAttribute" data-throw-if-not-resolved="false"></xref> で宣言した、実行時に
<code>Shader.Find</code> で名前から探す Shader の一覧です。開発用ビルドの Shader 間引き（<xref href="Omni.Editor.Build.OmniBuildShaderScope" data-throw-if-not-resolved="false"></xref>）が
これを残します。宣言は探すコードを持つアセンブリ自身が持つので、製品は他のアセンブリの Shader 名を持ちません。
コード中の <code>Shader.Find("...")</code> の文字列が、そのアセンブリの宣言に含まれることは、テストが検査します。

```csharp
public static class OmniRuntimeShaderLookups
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRuntimeShaderLookups](Omni.Editor.Build.OmniRuntimeShaderLookups.md)

## プロパティ（Properties）

### <a id="Omni_Editor_Build_OmniRuntimeShaderLookups_All"></a> All

読み込み済みの全アセンブリの宣言。

```csharp
public static IReadOnlyList<OmniRuntimeShaderLookups.Lookup> All { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniRuntimeShaderLookups](Omni.Editor.Build.OmniRuntimeShaderLookups.md).[Lookup](Omni.Editor.Build.OmniRuntimeShaderLookups.Lookup.md)\>

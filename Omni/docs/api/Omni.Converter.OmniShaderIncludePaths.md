# <a id="Omni_Converter_OmniShaderIncludePaths"></a> Class OmniShaderIncludePaths

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

ShaderLab／HLSL の <code>#include</code> のパスを扱います。本体のシェーダーは置き場所に依存しないよう、
同じ本体の中の HLSL を含むファイルからの相対パスで include します。本体のシェーダーの本文を別の場所
（例: <code>Assets/Radial/BRG/Shaders</code> の sidecar）へ写すときは、相対パスが解決できなくなるので、
元のファイルの位置を基準にした資産パスへ直してから写します。

```csharp
public static class OmniShaderIncludePaths
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniShaderIncludePaths](Omni.Converter.OmniShaderIncludePaths.md)

## メソッド（Methods）

### <a id="Omni_Converter_OmniShaderIncludePaths_AbsolutizeRelativeIncludes_System_String_System_String_"></a> AbsolutizeRelativeIncludes\(string, string\)

<code class="paramref">text</code> の相対 <code>#include</code> を、<code class="paramref">sourceAssetPath</code>（本文の元のファイルの資産パス）
を基準にした資産パス（<code>Assets/...</code>、<code>Packages/...</code>）へ直します。既に <code>Assets/</code>、<code>Packages/</code> で
始まる include は変えません。解決できない（根を越える）相対パスは、そのまま残します。

```csharp
public static string AbsolutizeRelativeIncludes(string text, string sourceAssetPath)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sourceAssetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniShaderIncludePaths_IsRooted_System_String_"></a> IsRooted\(string\)

<code class="paramref">includePath</code> が <code>Assets/</code> か <code>Packages/</code> で始まる資産パスなら true です。

```csharp
public static bool IsRooted(string includePath)
```

#### 引数（Parameters）

`includePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

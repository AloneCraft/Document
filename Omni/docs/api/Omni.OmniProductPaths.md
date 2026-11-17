# <a id="Omni_OmniProductPaths"></a> Class OmniProductPaths

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Omni本体の置き場所を1か所で解決します。開発プロジェクトでは<code>Assets/Omni/Core</code>、利用者のプロジェクトでは
UPMの<code>Packages/com.omni.rendering</code>です。本体の資産パスをコードや生成シェーダーへ書くときは、
文字列の直書きではなく<xref href="Omni.OmniProductPaths.Combine(System.String)" data-throw-if-not-resolved="false"></xref>を通します。Playerでは資産パスを使わないので
開発時の値のままです。

```csharp
public static class OmniProductPaths
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniProductPaths](Omni.OmniProductPaths.md)

## フィールド（Fields）

### <a id="Omni_OmniProductPaths_DefaultDemoRoot"></a> DefaultDemoRoot

デモのunitypackageの既定の取り込み先です。

```csharp
public const string DefaultDemoRoot = "Assets/Samples/Omni/0.1.0/Demos"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniProductPaths_DevelopmentDemoRoot"></a> DevelopmentDemoRoot

開発プロジェクトでのデモの置き場です（本体の兄弟フォルダ）。

```csharp
public const string DevelopmentDemoRoot = "Assets/Omni/Demos"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniProductPaths_DevelopmentRoot"></a> DevelopmentRoot

開発プロジェクトでの本体の根です。

```csharp
public const string DevelopmentRoot = "Assets/Omni/Core"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniProductPaths_PackageName"></a> PackageName

UPMとして配るときのパッケージ名です。

```csharp
public const string PackageName = "com.omni.rendering"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_OmniProductPaths_AbsoluteRoot"></a> AbsoluteRoot

本体の根のファイルシステム上の絶対パス（区切りは<code>/</code>、末尾の区切りなし）。

```csharp
public static string AbsoluteRoot { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniProductPaths_DemoRoot"></a> DemoRoot

デモの置き場の資産パス（末尾の区切りなし）。開発プロジェクトでは<code>Assets/Omni/Demos</code>、利用者のプロジェクトでは
デモのunitypackageの取り込み先<code>Assets/Samples/Omni/&lt;version&gt;/Demos</code>です。デモが無ければ、取り込み先の既定値を返します。

```csharp
public static string DemoRoot { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniProductPaths_IsPackage"></a> IsPackage

本体がUPMのpackageとして入っているならtrueです。

```csharp
public static bool IsPackage { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniProductPaths_Root"></a> Root

本体の根の資産パス（末尾の区切りなし）。

```csharp
public static string Root { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_OmniProductPaths_Combine_System_String_"></a> Combine\(string\)

本体の根からの相対パス（<code>Runtime/Sharders/RadialInject.hlsl</code>など）を資産パスにします。

```csharp
public static string Combine(string relativePath)
```

#### 引数（Parameters）

`relativePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniProductPaths_CombineAbsolute_System_String_"></a> CombineAbsolute\(string\)

本体の根からの相対パスをファイルシステム上の絶対パスにします。

```csharp
public static string CombineAbsolute(string relativePath)
```

#### 引数（Parameters）

`relativePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniProductPaths_DemoPath_System_String_"></a> DemoPath\(string\)

デモの置き場からの相対パス（<code>EarthToMoon/EarthToMoon.unity</code>など）を資産パスにします。

```csharp
public static string DemoPath(string relativePath)
```

#### 引数（Parameters）

`relativePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniProductPaths_FromDevelopmentPath_System_String_"></a> FromDevelopmentPath\(string\)

開発プロジェクトの配置（<code>Assets/Omni/Core/...</code>）で保存された資産パスを、現在の配置へ読み替えます。
Sceneなどに保存された文字列のパスを、packageとして入った本体でも使えるようにします。
本体の下でないパスは、そのまま返します。

```csharp
public static string FromDevelopmentPath(string path)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniProductPaths_IsDemoPath_System_String_"></a> IsDemoPath\(string\)

資産パスがデモの置き場の下なら true です。

```csharp
public static bool IsDemoPath(string assetPath)
```

#### 引数（Parameters）

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniProductPaths_IsUnder_System_String_System_String_"></a> IsUnder\(string, string\)

資産パスが本体の根の下（<code class="paramref">relativeFolder</code>の下）にあるかを返します。
<code class="paramref">relativeFolder</code>が空なら本体全体です。

```csharp
public static bool IsUnder(string assetPath, string relativeFolder = "")
```

#### 引数（Parameters）

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`relativeFolder` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniProductPaths_ToAbsolute_System_String_"></a> ToAbsolute\(string\)

本体の根の下にある資産パスを、ファイルシステム上の絶対パスにします。

```csharp
public static string ToAbsolute(string assetPath)
```

#### 引数（Parameters）

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

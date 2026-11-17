# <a id="Omni_OmniRuntimeShaderLookupAttribute"></a> Class OmniRuntimeShaderLookupAttribute

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

このアセンブリが Player の実行時に <code>Shader.Find</code> で名前から探す Shader を宣言します。
名前で探す Shader は Scene の依存に現れないので、開発用ビルドの Shader 間引きが外さないよう、
探すコードを持つアセンブリ自身が理由つきで宣言します（製品が他のアセンブリの Shader 名を持たないため）。

```csharp
[AttributeUsage(AttributeTargets.Assembly, AllowMultiple = true)]
public sealed class OmniRuntimeShaderLookupAttribute : Attribute, _Attribute
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) ← 
[OmniRuntimeShaderLookupAttribute](Omni.OmniRuntimeShaderLookupAttribute.md)

#### 実装するインターフェース（Implements）

[\_Attribute](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.\_attribute)

## コンストラクター（Constructors）

### <a id="Omni_OmniRuntimeShaderLookupAttribute__ctor_System_String_System_String_"></a> OmniRuntimeShaderLookupAttribute\(string, string\)

```csharp
public OmniRuntimeShaderLookupAttribute(string shaderName, string reason)
```

#### 引数（Parameters）

`shaderName` [string](https://learn.microsoft.com/dotnet/api/system.string)

<code>Shader.Find</code> に渡す名前。

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

Scene の依存に現れないのに必要な理由。

## プロパティ（Properties）

### <a id="Omni_OmniRuntimeShaderLookupAttribute_Reason"></a> Reason

Scene の依存に現れないのに必要な理由。

```csharp
public string Reason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniRuntimeShaderLookupAttribute_ShaderName"></a> ShaderName

<code>Shader.Find</code> に渡す名前。

```csharp
public string ShaderName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

# <a id="Omni_Editor_Build_OmniRuntimeShaderLookups_Lookup"></a> Struct OmniRuntimeShaderLookups.Lookup

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

実行時に名前で探す Shader 1件。

```csharp
public readonly struct OmniRuntimeShaderLookups.Lookup
```

## コンストラクター（Constructors）

### <a id="Omni_Editor_Build_OmniRuntimeShaderLookups_Lookup__ctor_System_String_System_String_System_String_"></a> Lookup\(string, string, string\)

```csharp
public Lookup(string shaderName, string assemblyName, string reason)
```

#### 引数（Parameters）

`shaderName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`assemblyName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Editor_Build_OmniRuntimeShaderLookups_Lookup_AssemblyName"></a> AssemblyName

宣言したアセンブリの名前。

```csharp
public string AssemblyName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Build_OmniRuntimeShaderLookups_Lookup_Reason"></a> Reason

Scene の依存に現れないのに必要な理由。

```csharp
public string Reason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Build_OmniRuntimeShaderLookups_Lookup_ShaderName"></a> ShaderName

<code>Shader.Find</code> に渡す名前。

```csharp
public string ShaderName { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

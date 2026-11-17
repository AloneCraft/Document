# <a id="Omni_Converter_Guarantees_OmniVersionSupportFinding"></a> Class OmniVersionSupportFinding

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

対応範囲の外にある、導入済みの Unity またはパッケージの版です。

```csharp
public sealed class OmniVersionSupportFinding
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniVersionSupportFinding](Omni.Converter.Guarantees.OmniVersionSupportFinding.md)

## コンストラクター（Constructors）

### <a id="Omni_Converter_Guarantees_OmniVersionSupportFinding__ctor_System_String_System_String_System_String_System_Boolean_"></a> OmniVersionSupportFinding\(string, string, string, bool\)

```csharp
public OmniVersionSupportFinding(string subject, string installed, string supported, bool newer)
```

#### 引数（Parameters）

`subject` [string](https://learn.microsoft.com/dotnet/api/system.string)

`installed` [string](https://learn.microsoft.com/dotnet/api/system.string)

`supported` [string](https://learn.microsoft.com/dotnet/api/system.string)

`newer` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## プロパティ（Properties）

### <a id="Omni_Converter_Guarantees_OmniVersionSupportFinding_Installed"></a> Installed

```csharp
public string Installed { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniVersionSupportFinding_Newer"></a> Newer

導入した版が、対応範囲より新しいとき true。

```csharp
public bool Newer { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniVersionSupportFinding_Subject"></a> Subject

表示名（Unity、URP など）。

```csharp
public string Subject { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniVersionSupportFinding_Supported"></a> Supported

変換規約を検証した版の範囲を、利用者向けに書いた文字列です。

```csharp
public string Supported { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

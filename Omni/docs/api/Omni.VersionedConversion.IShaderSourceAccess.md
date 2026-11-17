# <a id="Omni_VersionedConversion_IShaderSourceAccess"></a> Interface IShaderSourceAccess

Namespace: [Omni.VersionedConversion](Omni.VersionedConversion.md)  
Assembly: Omni.VersionedConversion.dll  

版別変換器がシェーダーの論理パスを読み取る境界です。

```csharp
public interface IShaderSourceAccess
```

## メソッド（Methods）

### <a id="Omni_VersionedConversion_IShaderSourceAccess_Exists_System_String_"></a> Exists\(string\)

```csharp
bool Exists(string logicalPath)
```

#### 引数（Parameters）

`logicalPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VersionedConversion_IShaderSourceAccess_IsEngineInclude_System_String_"></a> IsEngineInclude\(string\)

```csharp
bool IsEngineInclude(string rawIncludePath)
```

#### 引数（Parameters）

`rawIncludePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VersionedConversion_IShaderSourceAccess_ReadAllText_System_String_"></a> ReadAllText\(string\)

```csharp
string ReadAllText(string logicalPath)
```

#### 引数（Parameters）

`logicalPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

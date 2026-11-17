# <a id="Omni_Converter_Guarantees_OmniRadialContractVersion"></a> Class OmniRadialContractVersion

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

生成物が include する本体の HLSL（Radial の約束）の版です。
本体のファイルは元と出力の指紋に入れず、ここだけに入れます。約束を変えたら、表の行は
「約束が変わった」として検査のみ合格に下がります。中身を変えずに意味だけ変えるときは <xref href="Omni.Converter.Guarantees.OmniRadialContractVersion.Epoch" data-throw-if-not-resolved="false"></xref> を上げます。

```csharp
public static class OmniRadialContractVersion
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniRadialContractVersion](Omni.Converter.Guarantees.OmniRadialContractVersion.md)

## フィールド（Fields）

### <a id="Omni_Converter_Guarantees_OmniRadialContractVersion_Epoch"></a> Epoch

```csharp
public const int Epoch = 1
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_Guarantees_OmniRadialContractVersion_RelativeDirectory"></a> RelativeDirectory

```csharp
public const string RelativeDirectory = "Runtime/Sharders"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniRadialContractVersion_TryCompute_Omni_Converter_Guarantees_OmniFingerprint__System_String__"></a> TryCompute\(out OmniFingerprint, out string\)

```csharp
public static bool TryCompute(out OmniFingerprint fp, out string error)
```

#### 引数（Parameters）

`fp` [OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

# <a id="Omni_Converter_OmniRadialOutputMigration_Result"></a> Struct OmniRadialOutputMigration.Result

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

移行の結果です。

```csharp
public readonly struct OmniRadialOutputMigration.Result
```

## プロパティ（Properties）

### <a id="Omni_Converter_OmniRadialOutputMigration_Result_Failed"></a> Failed

移動に失敗した資産の数（元の場所に残しています）。

```csharp
public int Failed { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniRadialOutputMigration_Result_ManifestRenamed"></a> ManifestRenamed

台帳の記録を付け替えた数。

```csharp
public int ManifestRenamed { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniRadialOutputMigration_Result_Moved"></a> Moved

移動した資産の数。

```csharp
public int Moved { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

# <a id="Omni_Converter_RadialSourceResolver_BackfillResult"></a> Struct RadialSourceResolver.BackfillResult

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

マニフェストの逆引き情報（v2 で追加）が空のエントリを、パス規則から埋めます。
埋まらないものは<b>空のまま残し、削除も再生成強制もしません</b>。

```csharp
public readonly struct RadialSourceResolver.BackfillResult
```

## プロパティ（Properties）

### <a id="Omni_Converter_RadialSourceResolver_BackfillResult_AlreadyRecorded"></a> AlreadyRecorded

```csharp
public int AlreadyRecorded { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSourceResolver_BackfillResult_Filled"></a> Filled

```csharp
public int Filled { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSourceResolver_BackfillResult_Unresolved"></a> Unresolved

```csharp
public int Unresolved { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

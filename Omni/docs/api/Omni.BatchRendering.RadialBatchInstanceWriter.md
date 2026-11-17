# <a id="Omni_BatchRendering_RadialBatchInstanceWriter"></a> Class RadialBatchInstanceWriter

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

BRG instance dataへ書き込める値の受け口です。

```csharp
public sealed class RadialBatchInstanceWriter
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialBatchInstanceWriter](Omni.BatchRendering.RadialBatchInstanceWriter.md)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialBatchInstanceWriter_SetFloat_System_Int32_System_Single_"></a> SetFloat\(int, float\)

float値を永続instance dataへ設定します。

```csharp
public void SetFloat(int propertyId, float value)
```

#### 引数（Parameters）

`propertyId` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_BatchRendering_RadialBatchInstanceWriter_SetVector_System_Int32_UnityEngine_Vector4_"></a> SetVector\(int, Vector4\)

Vector4値を永続instance dataへ設定します。

```csharp
public void SetVector(int propertyId, Vector4 value)
```

#### 引数（Parameters）

`propertyId` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` Vector4

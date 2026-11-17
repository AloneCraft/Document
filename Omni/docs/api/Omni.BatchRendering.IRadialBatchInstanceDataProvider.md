# <a id="Omni_BatchRendering_IRadialBatchInstanceDataProvider"></a> Interface IRadialBatchInstanceDataProvider

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

非標準のper-instance値をBRGへ渡すProviderです。
Textureはinstance overrideできないため、floatとVectorだけを登録時またはMarkDirty時に書きます。

```csharp
public interface IRadialBatchInstanceDataProvider
```

## メソッド（Methods）

### <a id="Omni_BatchRendering_IRadialBatchInstanceDataProvider_WriteInstanceData_Omni_BatchRendering_RadialBatchInstanceWriter_"></a> WriteInstanceData\(RadialBatchInstanceWriter\)

対象instanceの永続値を書き込みます。

```csharp
void WriteInstanceData(RadialBatchInstanceWriter writer)
```

#### 引数（Parameters）

`writer` [RadialBatchInstanceWriter](Omni.BatchRendering.RadialBatchInstanceWriter.md)

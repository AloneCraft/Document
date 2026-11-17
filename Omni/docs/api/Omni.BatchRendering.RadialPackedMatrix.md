# <a id="Omni_BatchRendering_RadialPackedMatrix"></a> Struct RadialPackedMatrix

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

Unity標準GPUDrivenと同じ48 byteのDOTS packed matrixです。

```csharp
public struct RadialPackedMatrix
```

## フィールド（Fields）

### <a id="Omni_BatchRendering_RadialPackedMatrix_Packed0"></a> Packed0

packed matrixの先頭4成分です。

```csharp
public Vector4 Packed0
```

#### 値（Field Value）

 Vector4

### <a id="Omni_BatchRendering_RadialPackedMatrix_Packed1"></a> Packed1

packed matrixの中間4成分です。

```csharp
public Vector4 Packed1
```

#### 値（Field Value）

 Vector4

### <a id="Omni_BatchRendering_RadialPackedMatrix_Packed2"></a> Packed2

packed matrixの末尾4成分です。

```csharp
public Vector4 Packed2
```

#### 値（Field Value）

 Vector4

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialPackedMatrix_FromMatrix_UnityEngine_Matrix4x4__"></a> FromMatrix\(in Matrix4x4\)

UnityのMatrix4x4をDOTS shaderが読む4x3配置へ変換します。

```csharp
public static RadialPackedMatrix FromMatrix(in Matrix4x4 matrix)
```

#### 引数（Parameters）

`matrix` Matrix4x4

#### 戻り値（Returns）

 [RadialPackedMatrix](Omni.BatchRendering.RadialPackedMatrix.md)

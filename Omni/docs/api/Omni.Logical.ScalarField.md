# <a id="Omni_Logical_ScalarField"></a> Struct ScalarField

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>をUnityの<xref href="UnityEngine.SerializeField" data-throw-if-not-resolved="false"></xref>で直接保持できるようにする
シリアライズ用ラッパーです。

<p>
<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>自体は<code>readonly struct</code>で書き込み可能フィールドを持たないため
Unityの標準シリアライザでは扱えません。このラッパーは<xref href="Omni.Logical.IntRaw.ToLimbArray" data-throw-if-not-resolved="false"></xref>/
<xref href="Omni.Logical.IntRaw.FromSerializedLimbs(System.UInt64%5b%5d)" data-throw-if-not-resolved="false"></xref>を介して、シリアライズ時にlimb配列へパックし、
デシリアライズ時に<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>へ復元します（旧形式Q95.32の2 limbも同じ数値として読みます）。
利用側は暗黙変換で通常の<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>と同様に読み書きできます。
</p>

```csharp
[Serializable]
public struct ScalarField : ISerializationCallbackReceiver
```

#### 実装するインターフェース（Implements）

ISerializationCallbackReceiver

## メソッド（Methods）

### <a id="Omni_Logical_ScalarField_FromString_System_String_"></a> FromString\(string\)

任意精度の10進文字列からフィールドを構築します。変換に失敗した場合はゼロになります。

```csharp
public static ScalarField FromString(string text)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [ScalarField](Omni.Logical.ScalarField.md)

### <a id="Omni_Logical_ScalarField_OnAfterDeserialize"></a> OnAfterDeserialize\(\)

<p>Implement this callback to transform data back into runtime data types after an object is deserialized.</p>

```csharp
public void OnAfterDeserialize()
```

### <a id="Omni_Logical_ScalarField_OnBeforeSerialize"></a> OnBeforeSerialize\(\)

<p>Implement this callback to transform data into serializable data types immediately before an object is serialized.</p>

```csharp
public void OnBeforeSerialize()
```

## 演算子（Operators）

### <a id="Omni_Logical_ScalarField_op_Implicit_Omni_Logical_ScalarField__Omni_Logical_Scalar"></a> implicit operator Scalar\(ScalarField\)

<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>への暗黙変換です。

```csharp
public static implicit operator Scalar(ScalarField field)
```

#### 引数（Parameters）

`field` [ScalarField](Omni.Logical.ScalarField.md)

#### 戻り値（Returns）

 [Scalar](Omni.Logical.Scalar.md)

### <a id="Omni_Logical_ScalarField_op_Implicit_Omni_Logical_Scalar__Omni_Logical_ScalarField"></a> implicit operator ScalarField\(Scalar\)

<xref href="Omni.Logical.Scalar" data-throw-if-not-resolved="false"></xref>からの暗黙変換です。

```csharp
public static implicit operator ScalarField(Scalar value)
```

#### 引数（Parameters）

`value` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [ScalarField](Omni.Logical.ScalarField.md)

# <a id="Omni_Editor_State_OrthoLogGridDataType"></a> Enum OrthoLogGridDataType

Namespace: [Omni.Editor.State](Omni.Editor.State.md)  
Assembly: Omni.Editor.dll  

Orthographic対数グリッド（<xref href="Omni.Editor.State.OmniViewState.OrthoLogGridEnabled" data-throw-if-not-resolved="false"></xref>）の画面端が
どのデータ型の表現可能な最大値・最小値に対応するかを選びます（ScaleView_Plan Q節）。

```csharp
public enum OrthoLogGridDataType
```

## フィールド（Fields）

`Float = 0` 

画面端が<code>float.MaxValue</code>に対応します。



`Logic = 1` 

画面端が<code>Omni.Logical.Scalar.MaxValue</code>に対応します。

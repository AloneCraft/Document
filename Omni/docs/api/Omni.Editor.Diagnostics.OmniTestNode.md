# <a id="Omni_Editor_Diagnostics_OmniTestNode"></a> Struct OmniTestNode

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

テスト結果の木の 1 節点です（名前空間・fixture・パラメーター化メソッド・test case のどれでも）。

```csharp
[Serializable]
public struct OmniTestNode
```

## コンストラクター（Constructors）

### <a id="Omni_Editor_Diagnostics_OmniTestNode__ctor_System_String_System_Int32_"></a> OmniTestNode\(string, int\)

```csharp
public OmniTestNode(string fullName, int executedLeafCount)
```

#### 引数（Parameters）

`fullName` [string](https://learn.microsoft.com/dotnet/api/system.string)

`executedLeafCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniTestNode_executedLeafCount"></a> executedLeafCount

この節点の配下（自身を含む）で、合格か不合格になった test case の数です。

```csharp
public int executedLeafCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniTestNode_fullName"></a> fullName

```csharp
public string fullName
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

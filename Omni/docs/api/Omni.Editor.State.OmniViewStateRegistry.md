# <a id="Omni_Editor_State_OmniViewStateRegistry"></a> Class OmniViewStateRegistry

Namespace: [Omni.Editor.State](Omni.Editor.State.md)  
Assembly: Omni.Editor.dll  

Scene ViewごとのOmni表示状態を管理します。
InstanceIDと弱参照を使用し、破棄済みEditorオブジェクトを保持しません。

```csharp
[InitializeOnLoad]
public static class OmniViewStateRegistry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniViewStateRegistry](Omni.Editor.State.OmniViewStateRegistry.md)

## メソッド（Methods）

### <a id="Omni_Editor_State_OmniViewStateRegistry_ClearTransientStates"></a> ClearTransientStates\(\)

Domain Reload、Assembly Reload、Editor終了時に一時状態を破棄します。

```csharp
public static void ClearTransientStates()
```

### <a id="Omni_Editor_State_OmniViewStateRegistry_GetOrCreate_UnityEngine_Object_"></a> GetOrCreate\(Object\)

指定したScene Viewの状態を取得し、未登録なら新規作成します。

```csharp
public static OmniViewState GetOrCreate(Object owner)
```

#### 引数（Parameters）

`owner` Object

状態を所有するEditorオブジェクト。nullは指定できません。

#### 戻り値（Returns）

 [OmniViewState](Omni.Editor.State.OmniViewState.md)

ownerに対応する一時的な表示状態。

### <a id="Omni_Editor_State_OmniViewStateRegistry_PruneDestroyedOwners"></a> PruneDestroyedOwners\(\)

破棄済みのScene Viewに属する状態を削除します。

```csharp
public static int PruneDestroyedOwners()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

削除した状態数。

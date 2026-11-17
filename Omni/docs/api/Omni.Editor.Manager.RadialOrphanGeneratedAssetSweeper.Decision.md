# <a id="Omni_Editor_Manager_RadialOrphanGeneratedAssetSweeper_Decision"></a> Enum RadialOrphanGeneratedAssetSweeper.Decision

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

```csharp
public enum RadialOrphanGeneratedAssetSweeper.Decision
```

## フィールド（Fields）

`Delete = 0` 

元が消えており、どこからも参照されていない。ごみ箱へ移す。



`KeptReferenced = 1` 

元は消えているが参照されているため残す。



`Unverifiable = 2` 

元の有無を確定できないため残す。

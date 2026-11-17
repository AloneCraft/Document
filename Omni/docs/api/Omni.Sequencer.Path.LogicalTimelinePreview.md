# <a id="Omni_Sequencer_Path_LogicalTimelinePreview"></a> Class LogicalTimelinePreview

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

トラックの <code>GatherProperties</code> から、結び先の受け手へ登録を頼む。

```csharp
public static class LogicalTimelinePreview
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[LogicalTimelinePreview](Omni.Sequencer.Path.LogicalTimelinePreview.md)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalTimelinePreview_AddLogicalTransform_UnityEngine_Timeline_IPropertyCollector_Omni_Logical_Transform_"></a> AddLogicalTransform\(IPropertyCollector, Transform\)

Logical の Transform と、それが書く Unity の Transform を登録する(Logical の位置・回転・縮尺の raw と、表示の Transform)。

```csharp
public static void AddLogicalTransform(IPropertyCollector driver, Transform logical)
```

#### 引数（Parameters）

`driver` IPropertyCollector

`logical` Transform

### <a id="Omni_Sequencer_Path_LogicalTimelinePreview_End_System_Object_"></a> End\(object\)

トラックのミキサーが壊されたとき(Edit Mode だけ)、結び先へプレビューの終わりを知らせる。

```csharp
public static void End(object bound)
```

#### 引数（Parameters）

`bound` [object](https://learn.microsoft.com/dotnet/api/system.object)

### <a id="Omni_Sequencer_Path_LogicalTimelinePreview_Gather_UnityEngine_Timeline_TrackAsset_UnityEngine_Playables_PlayableDirector_UnityEngine_Timeline_IPropertyCollector_"></a> Gather\(TrackAsset, PlayableDirector, IPropertyCollector\)

<code class="paramref">track</code> の結び先が <xref href="Omni.Sequencer.Path.ILogicalTimelinePreview" data-throw-if-not-resolved="false"></xref> を実装していれば、登録を頼む。
中継(<xref href="Omni.Sequencer.Path.LogicalTimelineSinkRelay" data-throw-if-not-resolved="false"></xref>)は実行時だけの物なので登録しない。

```csharp
public static void Gather(TrackAsset track, PlayableDirector director, IPropertyCollector driver)
```

#### 引数（Parameters）

`track` TrackAsset

`director` PlayableDirector

`driver` IPropertyCollector

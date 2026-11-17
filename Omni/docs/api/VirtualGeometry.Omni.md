# <a id="VirtualGeometry_Omni"></a> Namespace VirtualGeometry.Omni

### クラス（Classes）

 [OmniPlanetPlacement](VirtualGeometry.Omni.OmniPlanetPlacement.md)

面(惑星)を Omni の Logical 座標に置き、Radial 対数描画で描く <xref href="VirtualGeometry.World.IPlanetPlacement" data-throw-if-not-resolved="false"></xref>。
面の GameObject(<xref href="VirtualGeometry.World.PlanarTerrainSource" data-throw-if-not-resolved="false"></xref> など <xref href="VirtualGeometry.World.PlanetLayerSource" data-throw-if-not-resolved="false"></xref> と同じもの)に Omni の Logical.Transform と一緒に付ける。
位置の正本は Logical で、float にするのは eye からの相対差にした後だけ。
cull は eye を原点とする world 軸の物理空間で行い、HZB は使わない(深度が対数写像のため)。
Cell ごとに、Omni が precise な Renderer に書くのと同じ物体ごとの値を MaterialPropertyBlock へ書く。
material には Omni の Radial shader を元にした .vgshader を使う。

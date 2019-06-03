bl_info = {
    "name": "POLYHEDRA",
    "author": "Larionov_Alexey",
    "version": (0, 21),
    "blender": (2, 75, 0),
    "location": "View3D > Add > Mesh > POLYHEDRA",
    "description": "Generate mesh Archimedean solids and Kepler-Poinsot_solids",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
    }
import sys
import os

if "bpy" in locals():
    import importlib
    importlib.reload(archimedean_solid)
    importlib.reload(polypanelui)
    importlib.reload(kepler_poinsot_solid)
else:
    from polyhedra import archimedean_solid
    from polyhedra import polypanelui
    from polyhedra import kepler_poinsot_solid

import bpy


def register():
    ###arch
    bpy.utils.register_class(archimedean_solid.CreateCuboctahedron)
    bpy.utils.register_class(archimedean_solid.CreateIcosidodecahedron)
    bpy.utils.register_class(archimedean_solid.CreateSnubDodecahedron)
    bpy.utils.register_class(archimedean_solid.CreateRhombicuboctahedron)
    bpy.utils.register_class(archimedean_solid.CreateTruncatedCuboctahedron)
    bpy.utils.register_class(archimedean_solid.CreateTruncatedIcosidodecahedron)
    bpy.utils.register_class(archimedean_solid.CreateRhombIcosIdodecahedron)
    bpy.utils.register_class(archimedean_solid.CreateTruncatedIcosahedron)
    bpy.utils.register_class(archimedean_solid.CreateTruncatedCube)
    bpy.utils.register_class(archimedean_solid.CreateTruncatedDodecahedron)
    bpy.utils.register_class(archimedean_solid.CreateTruncatedOctahedron)
    bpy.utils.register_class(archimedean_solid.CreateTruncatedTetrahedron)
    bpy.utils.register_class(archimedean_solid.CreateSnubCubeLeft)
    bpy.utils.register_class(archimedean_solid.CreateSnubCubeRight)
    ###kepl
    bpy.utils.register_class(kepler_poinsot_solid.CreateGreatDodecahedron)
    bpy.utils.register_class(kepler_poinsot_solid.CreateGreatStellatedDodecahedron)
    bpy.utils.register_class(kepler_poinsot_solid.CreateGreatIcosahedron)
    bpy.utils.register_class(kepler_poinsot_solid.CreateSmallStellatedDodecahedron)
    ###UI
    bpy.utils.register_class(polypanelui.Larionov_polyhedra)

def unregister():
    ###arch
    bpy.utils.unregister_class(archimedean_solid.CreateCuboctahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateIcosidodecahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateSnubDodecahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateRhombicuboctahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateTruncatedCuboctahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateTruncatedIcosidodecahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateRhombIcosIdodecahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateTruncatedIcosahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateTruncatedCube)
    bpy.utils.unregister_class(archimedean_solid.CreateTruncatedDodecahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateTruncatedOctahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateTruncatedTetrahedron)
    bpy.utils.unregister_class(archimedean_solid.CreateSnubCubeLeft)
    bpy.utils.unregister_class(archimedean_solid.CreateSnubCubeRight)
    ###kepl
    bpy.utils.unregister_class(kepler_poinsot_solid.CreateGreatDodecahedron)
    bpy.utils.unregister_class(kepler_poinsot_solid.CreateGreatStellatedDodecahedron)
    bpy.utils.unregister_class(kepler_poinsot_solid.CreateGreatIcosahedron)
    bpy.utils.unregister_class(kepler_poinsot_solid.CreateSmallStellatedDodecahedron)
    ###UI
    bpy.utils.unregister_class(polypanelui.Larionov_polyhedra)

if __name__ == "__main__":
    register()    
    

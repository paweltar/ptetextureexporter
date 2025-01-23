bl_info = {
    "name": "Papercraft Texture Exporter",
    "author": "Twoje Imię",
    "version": (0, 0, 1), # Wersja pluginu - początek 0.0.1
    "blender": (4, 3, 0), # Minimalna wersja Blendera
    "location": "N-Panel", # Umiejscowienie panelu (zakładka N)
    "description": "Plugin do transferu tekstur i eksportu UV do PDF dla papercraft",
    "warning": "",
    "doc_url": "",
    "category": "Object", # Kategoria w menu Add-ons
}

import bpy

class PTE_Panel(bpy.types.Panel):
    """Panel Papercraft Texture Exporter"""
    bl_label = "Papercraft Texture Exporter" # Nazwa panelu widoczna w UI
    bl_idname = "VIEW3D_PT_pte_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Papercraft" # Zakładka w N-panelu

    def draw(self, context):
        layout = self.layout
        layout.label(text="Witaj w PTE!") # Na początek tylko tekst powitalny

def register():
    bpy.utils.register_class(PTE_Panel)

def unregister():
    bpy.utils.unregister_class(PTE_Panel)

if __name__ == "__main__":
    register()
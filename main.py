import os
import shutil
directory=input("Enter pack folder name: ")
pack_title=input("Enter pack title:  ")
pack_desc=input("Enter the pack description: ")
#pack_namespace=input("Enter the pack namespace (Type minecraft for a vanillia resource pack): ")

def pack_version_check():
  try:
    pack_version=int(input("""1. 1.6.2 to 1.8.9
2. 1.9 to 1.10.2
3. 1.11 to 1.12.2
4. 1.13 to 1.14.4
5. 1.15 to 1.16.1
6. 1.16.2 to 1.16.5
7. 1.17 to 1.17.1
8. 1.18 to 1.18.2
9. 1.19
Enter the pack version: """))
    if pack_version > 0 and pack_version < 10:
      return pack_version
    else:
      print("Invalid value")
      print("")
      pack_version_check()
  except:
    print("Not a number")
    print("")
    pack_version_check()
  
pack_version=pack_version_check()

folders=["./"+directory+"/assets",
        "./"+directory+"/assets/minecraft",
        "./"+directory+"/assets/minecraft/textures",
        "./"+directory+"/assets/minecraft/textures/block",
        "./"+directory+"/assets/minecraft/textures/colormap",
        "./"+directory+"/assets/minecraft/textures/effect",
        "./"+directory+"/assets/minecraft/textures/entity",
        "./"+directory+"/assets/minecraft/textures/environment",
        "./"+directory+"/assets/minecraft/textures/font",
        "./"+directory+"/assets/minecraft/textures/gui",
        "./"+directory+"/assets/minecraft/textures/item",
        "./"+directory+"/assets/minecraft/textures/map",
        "./"+directory+"/assets/minecraft/textures/misc",
        "./"+directory+"/assets/minecraft/textures/models",
        "./"+directory+"/assets/minecraft/textures/models/armor",
        "./"+directory+"/assets/minecraft/textures/painting",
        "./"+directory+"/assets/minecraft/textures/particle",
        "./"+directory+"/assets/minecraft/textures/gui/advancements",
        "./"+directory+"/assets/minecraft/textures/gui/container",
        "./"+directory+"/assets/minecraft/textures/gui/presets",
        "./"+directory+"/assets/minecraft/textures/gui/title",
        "./"+directory+"/assets/minecraft/textures/gui/title/background"

         ]
folders_extended=[
         "./"+directory+"/assets/minecraft/blockstates",
         "./"+directory+"/assets/minecraft/font",
         "./"+directory+"/assets/minecraft/icons",
         "./"+directory+"/assets/minecraft/lang",
         "./"+directory+"/assets/minecraft/models",
         "./"+directory+"/assets/minecraft/particles",
         "./"+directory+"/assets/minecraft/sounds",
         "./"+directory+"/assets/minecraft/shaders",
         "./"+directory+"/assets/minecraft/texts",
         ]
  
complex=input("You will only modify textures and not things like font (T/F): ")
def choose_complexity():
  if complex=="F":
    folders.extend(folders_extended)
  elif complex=="T":
    pass
  else:
    print("Invalid Response")
    choose_complexity()
    
choose_complexity()

os.mkdir(directory)
for path in folders:
  os.mkdir(path)

packmcmeta=open("pack.mcmeta","w+")
packmcmeta.write(
'{"pack":{"pack_format": '+str(pack_version)+',"description":"'+pack_desc+'"}}')
packmcmeta.close()
shutil.move("./pack.mcmeta","./"+directory)

print("")
print("Folder Created, you can now start creating image or text files to start working on your resource pack")
print("Feel free to move it out of this folder and put it anywhere on your computer")

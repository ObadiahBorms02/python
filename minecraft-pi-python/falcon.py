from mcpi.minecraft import Minecraft
from mcpi import block

air = 0
iron_block = 42
lapis_lazuli_block = 22


radius = 15
radius1 = 12
radius2 = 12


mc = Minecraft.create("127.0.0.1", 4711)
playerPos = mc.player.getPos()
x, y, z = mc.player.getPos()  
#return mc
	

def body():
	
	for x in range(radius*-1,radius2): #Creates box
		for y in range(radius*0, 1):
			for z in range(radius*-1,radius2):
				if x**2 + z**2 < radius**2: #Creates curvature for the sphere
					mc.setBlock(playerPos.x + x, playerPos.y + y + 0, playerPos.z - z - 3, iron_block)
				
	for x in range(radius*-1,radius): #Creates box
		for y in range(radius*0, 3):
			for z in range(radius*-1,radius):
				if x**2 + z**2 < radius**2: #Creates curvature for the sphere
					mc.setBlock(playerPos.x + x, playerPos.y + y - 3, playerPos.z - z - 3, iron_block)

	for x in range(radius*-1,radius1): #Creates box
		for y in range(radius*0, 1):
			for z in range(radius*-1,radius1):
				if x**2 + z**2 < radius**2: #Creates curvature for the sphere
					mc.setBlock(playerPos.x + x, playerPos.y + y - 4, playerPos.z - z - 3, iron_block)

	for x in range(radius*-5, 1): #Creates box
		for y in range(radius*0, 1):
			for z in range(radius*-5,1):
				if x**2 + z**2 < radius**2: #Creates curvature for the sphere
					mc.setBlock(playerPos.x + x, playerPos.y + y - 2, playerPos.z - z - 3, lapis_lazuli_block)
body()
def a1():
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-3, y-2, z-16, x+14, y, z+1, iron_block)
	mc.setBlocks(x, y-2, z-14, x+16, y, z+1, iron_block)
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-3, y-2, z-15, x+15, y+1, z+1, air)	
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-3, y-2, z-15, x+13, y, z+1, iron_block)
	mc.setBlocks(x, y-2, z-13, x+15, y, z+1, iron_block)
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-3, y-2, z-14, x+14, y+1, z+1, air)	
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-3, y-2, z-14, x+12, y, z+1, iron_block)
	mc.setBlocks(x, y-2, z-12, x+14, y, z+1, iron_block)
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-3, y-2, z-13, x+13, y+1, z+1, air)
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-3, y-2, z-13, x+11, y, z+1, iron_block)
	mc.setBlocks(x, y-2, z-11, x+13, y, z+1, iron_block)
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-3, y-2, z-12, x+12, y+1, z+1, air)
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-3, y, z-16, x+16, y, z+1, air)
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-3, y-3, z-12, x+10, y, z+1, iron_block)
	mc.setBlocks(x, y-3, z-11, x+12, y, z+1, iron_block)
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x, y-3, z, x+18, y, z+6, iron_block)
	
	x, y, z = mc.player.getPos()
	mc.setBlocks(x, y, z, x+18, y, z+6, air)
	mc.setBlocks(x, y, z, x+18, y, z+5, iron_block)
	mc.setBlocks(x, y, z, x+18, y, z, air)
	mc.setBlocks(x, y, z, x+12, y, z+6, iron_block)
	
	#x, y, z = mc.player.getPos()
	#mc.setBlocks(x-1, y, z-13, x+10, y, z+1, iron_block)
	
	
a1()
#def main():
	#init()
	#mc = Minecraft.create("127.0.0.1",4711)
	#mc.player.getPos()
	#return mc
	#playerPos = mc.player.getPos()
	#x, y, z = mc.player.getPos()
	#body(mc,x+0,y+0,z+0)
	#a1(mc,x+0,y-43,z+0)
	
	
#main()	



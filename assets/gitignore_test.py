print(SynthDefs)

print (Scale.names())
Scale.default ="indian"

p1 >> pluck([1,4,3,7,[3,5,7,9]])
#p1.stop()
p2 >> glass(oct=4, dur=[1/2, 1/4,1,1,1])
#p3.stop()
p3 >> play("f-e-n-g-j-u-a-n[-----]")
#p3.stop()

Clock.bpm = 160

Clock.clear()
print(Clock)

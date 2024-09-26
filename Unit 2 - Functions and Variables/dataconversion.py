# Start by copying this code block into a new file called dataconversion.py in your unit 2 folder. This is an ungraded activity.

# Successfully convert all of the following variables to another type and print the result
# If the conversion prints without errors, you did the conversion correctly

a = 115         #int -> string
b = 3.14        #float -> string
c = "68"        #string -> int
d = "True"      #string -> boolean
e = True        #boolean -> string
f = False       #boolean -> string
g = '10110111'  #byte -> int
h = "2.54"      #string -> float
i = 100         #int -> float
j = 10.0        #float -> int
k = 254         #int -> byte

a_str = str(a)
c_num = int(c)
b_str = str(b)
d_bool = bool(d)
e_str = str(e)
f_str = str(f)
g_int = int(g, 2)
h_float = float(h)
i_float = float(i)
j_int = int(j)
k_byte = bin(254)

print(a_str)
print(c_num)
print(b_str)
print(d_bool)
print(e_str)
print(f_str)
print(g_int)
print(h_float)
print(i_float)
print(j_int)
print(k_byte)